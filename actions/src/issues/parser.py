from collections import deque

from issues import Issue

FIELDS_MAPPING = {
    "Decision": "decision",
    "Justification": "summary",
    "Repo URL": "project_url",
    "Alternative project name": "project_name",
    "What is the project type?": "project_type",
    "What is the project license?": "license",
    "Connect IQ Store URL": "appstore_url",
    "Tested in the simulator?": "simulator",
    "Tested on an actual device?": "device",
    "Quality of the code?": "sourcecode",
    "Description of the project": "description",
    "Additional info": "additional"
}
FIELDS_TYPES = {
    "Decision": "input",  # single text value
    "Justification": "input",
    "Repo URL": "input",
    "Alternative project name": "input",
    "What is the project type?": "multiple",  # multiple values, delimited by comma
    "What is the project license?": "radio",  # single value
    "Connect IQ Store URL": "input",
    "Tested in the simulator?": "input",
    "Tested on an actual device?": "input",
    "Quality of the code?": "checkboxes",  # multiple values, <ul><li> structure
    "Description of the project": "input",
    "Additional info": "input"
}
KNOWN_HEADERS = ["### Decision", "### Justification", "### Repo URL", "### What is the project type?",
                 "### Alternative project name",
                 "### What is the project license?", "### Connect IQ Store URL",
                 "### Tested in the simulator?", "### Tested on an actual device?", "### Quality of the code?",
                 "### Description of the project", "### Additional info"]


class IssueParser:

    @staticmethod
    def clear_string(string: str) -> str:
        return string.strip()

    @staticmethod
    def clear_markdown(string: str) -> str:
        result = IssueParser.replace_end_of_line(string)
        return result.replace('\n\n', '\n')

    @staticmethod
    def read_markdown_from_file(file):
        with open(file, "r") as f:
            data = f.read()
        return IssueParser.clear_markdown(data)

    @staticmethod
    def replace_end_of_line(text, replace_with='\n'):
        return text.replace('\\r\\n', '\\n').replace('\r\n', '\n').replace('\\n', replace_with)

    @staticmethod
    def extract_body(q):
        result = ""
        while q and not ((line := q.popleft()).startswith("###") and line in KNOWN_HEADERS):
            result += line + "\n"

        if line.startswith("###"):
            q.appendleft(line)

        return result[:-1] if result.endswith("\n") else result

    @staticmethod
    def interpret_input_value(value):
        return None if value == "_No response_" or not value else value

    @staticmethod
    def interpret_multiple_value(value):
        return None if value == "_No response_" or not value else value.split(", ")

    @staticmethod
    def interpret_radio_value(value):
        return None if value == "_No response_" or not value else value

    @staticmethod
    def interpret_checkboxes_value(body):
        result = []
        if body == "_No response_":
            return result
        lines = body.splitlines()
        for line in lines:
            if line.startswith("- [x]"):
                result.append(line[6:])
        return result

    @staticmethod
    def parse_body(body: str, field_type: str):
        value = None
        body = IssueParser.clear_string(body)
        if field_type == "input":
            value = IssueParser.interpret_input_value(body)
        elif field_type == "multiple":
            value = IssueParser.interpret_multiple_value(body)
        elif field_type == "radio":
            value = IssueParser.interpret_radio_value(body)
        elif field_type == "checkboxes":
            value = IssueParser.interpret_checkboxes_value(body)
        else:
            raise Exception(f"Unknown field type: {field_type}")
        return value

    @staticmethod
    def from_markdown(md: str) -> Issue:

        result = None
        lines = md.splitlines()

        # Initialize LIFO Queue
        q = deque(lines)
        while q:
            line = q.popleft()
            l = IssueParser.clear_string(line)
            if l.startswith("###"):
                key = l[4:]
                mapping = FIELDS_MAPPING[key]
                field_type = FIELDS_TYPES[key]
                # print(f"processing: '{key}' (mapped to '{mapping}' of type '{field_type}')")
                body = IssueParser.extract_body(q)
                value = IssueParser.parse_body(body, field_type)
                if value:
                    if not result:
                        result = Issue()
                    setattr(result, mapping, value)
        return result
