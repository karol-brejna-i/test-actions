from additional_info.appstoreextract import AppStoreExtractor
from issues import Issue
from issues.parser import IssueParser
from issues.validator import IssueValidator
from utils.jsonutils import read_json_from_file

# update the path for tests
GIHUB_CONTEXT_FILE = '../data/GITHUB_CONTEXT.json'
# update the path for tests
URL = "https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0"

FOLDER_PATH = ""


def test_appstore_extract():
    extractor = AppStoreExtractor(URL)
    extractor.fetch_page()
    info = extractor.get_all()
    print(info)


def test_data_from_github_context():
    # obtain the json file with GITHUB_CONTEXT
    data = read_json_from_file(GIHUB_CONTEXT_FILE)  # for development purposes, read it from a file

    # get issue body
    md = IssueParser.clear_markdown(data["event"]["issue"]["body"])

    # DEBUG/TESTING
    # FILE = 'actions/issue_body_radio_and_problematic_header.md'
    # md = IssueParser.read_markdown_from_file(FILE)
    # write to file, for review
    with open("body.cleaned.md", 'w') as f:
        f.write(md)

    # Create the issue object
    issue = IssueParser.from_markdown(md)
    print('-------------')
    print(issue)


def test_issue_validator_url():
    i = Issue()
    t = IssueValidator(i)
    result = t.validate_url("https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0")
    print(result)
    result = t.validate_url("https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0",
                            test_fetch=True)
    print(result)

    result = t.validate_url("https://alamakota.niemozliwe")
    print(result)
    result = t.validate_url("https://alamakota.niemozliwe", test_fetch=True)
    print(result)


def test_issue_validator():
    i = Issue(summary="test",
              project_url="https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0",
              project_type="app", description="test")
    t = IssueValidator(i)
    result = t.validate_required_fields()
    print(result)

    # set up all formally required fields:
    # ["decision", "summary", "project_url", "project_type", "sourcecode", "description"]
    i = Issue(decision="Ok", summary="test",
              project_url="https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0",
              project_type="app", description="test")
    t = IssueValidator(i)
    result = t.validate_required_fields()
    print(result)

    # set up all required fields, including testing information (on device or in the simulator)
    i = Issue(decision="Ok", summary="test",
              project_url="https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0",
              project_type="app", description="test", device="Garmin Fenix 6")
    t = IssueValidator(i)
    result = t.validate_required_fields()
    print(result)

    # set up all required fields, including testing information (on device or in the simulator)
    i = Issue(decision="", summary="",
              project_url="https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0",
              project_type="app", description="test", device="Garmin Fenix 6")
    t = IssueValidator(i)
    result = t.validate()
    print(result)

    i = Issue(decision="", summary="",
              project_url="https://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0",
              project_type="app", description="test", device="Garmin Fenix 6", appstore_url="http://badurl")
    t = IssueValidator(i)
    result = t.validate()
    print(result)

def main():
    # test_data_from_github_context()
    # test_appstore_extract()
    test_issue_validator()
    # test_issue_validator_url()


if __name__ == '__main__':
    main()
