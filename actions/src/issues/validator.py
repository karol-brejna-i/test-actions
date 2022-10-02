import validators as validators

from issues import Issue


class IssueValidator:
    def __init__(self, issue: Issue) -> None:
        self.issue = issue

    def validateUrl(self, url):
        return validators.url(url)

    def validate(self):
        pass


