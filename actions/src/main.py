from additional_info.appstoreextract import AppStoreExtractor
from issues import Issue
from issues.parser import IssueParser
from issues.validator import IssueValidator
from utils.jsonutils import readJsonFromFile

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
    data = readJsonFromFile(GIHUB_CONTEXT_FILE)  # for development purpposes, read it from a file

    # get issue body
    md = IssueParser.clear_markdown(data["event"]["issue"]["body"])

    # DEBUG/TESTING
    # FILE = 'actions/issue_body_radio_and_problematic_header.md'
    # md = IssueParser.readMarkdownFromFile(FILE)
    # write to file, for review
    # with open("body.cleaned.md", 'w') as f:
    #     f.write(md)

    # Create the issue object
    issue = IssueParser.from_markdown(md)
    print('-------------')
    print(issue)


def main():
    # test_data_from_github_context()
    # test_appstore_extract()

    t = IssueValidator(Issue())
    print(t.validateUrl("httsps://apps.garmin.com/en-US/apps/11c2548e-8878-497f-809b-ea640e54ca43#0"))


if __name__ == '__main__':
    main()
