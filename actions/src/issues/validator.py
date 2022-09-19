from issues import Issue


class IssueValidator:
    def __init__(self, issue: Issue) -> None:
        self.issue = issue

    def validateUrl(self, url):
        pass

    def validate(self):
        pass


