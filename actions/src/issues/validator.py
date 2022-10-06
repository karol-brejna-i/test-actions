import requests
import validators as validators
from issues import Issue
from issues.parser import FIELDS_MAPPING
from typing import List, Tuple

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

REQUIRED_FIELDS = ["decision", "summary", "project_url", "project_type", "description"]

REVERSE_FIELDS_MAPPING = {v: k for k, v in FIELDS_MAPPING.items()}


class IssueValidator:
    """
    - URLs (project, App Store)
    - Is the proposed project already on the list (either "proper" one or rejected projects list)
    - Was a known device entered?
    - Is required info entered (for example, the project should be tested in the simulator or on a device)
    - Is declared license the same as defined in the project settings

    """

    def __init__(self, issue: Issue) -> None:
        self.issue = issue

    def validate_url(self, url, test_fetch=False):
        result = False
        try:
            result = validators.url(url)
            if test_fetch:
                try:
                    response = requests.get(url, headers=HEADERS)
                    result = response.status_code == 200
                except requests.exceptions.RequestException as e:
                    result = False
        except validators.ValidationFailure:
            pass
        return result

        return validators.url(url)

    def validate_tested(self) -> bool:
        """
        The proposed project should be tested either in the simulator or on the device.
        """
        result: bool = self.issue.simulator is not None or self.issue.device is not None
        return result

    def validate_required_fields(self) -> Tuple[bool, List[str]]:
        """
        Check if all required fields are filled
        :param issue:
        :return:
        """
        empty_fields = [REVERSE_FIELDS_MAPPING[field] for field in REQUIRED_FIELDS if not getattr(self.issue, field)]
        if empty_fields:
            return False, empty_fields
        else:
            return True, []

    def compose_validation_result(self, tested_ok, required_fields_ok, empty_fields, project_url_ok, appstore_url_ok):
        messages = []
        if not tested_ok:
            messages.append("The proposed project should be tested either in the simulator or on the device.")
        if not required_fields_ok:
            messages.append(f"Required fields are not filled: {', '.join(empty_fields)}.")
        if not project_url_ok:
            messages.append("Project URL is not valid!")
        if not appstore_url_ok:
            messages.append("Provided Connect IQ Store URL is not valid!")
        return messages

    def validate(self):
        tested_ok = self.validate_tested()
        required_fields_ok, empty_fields = self.validate_required_fields()
        project_url_ok = self.validate_url(self.issue.project_url, test_fetch=True)
        appstore_url_ok = True if not self.issue.appstore_url else self.validate_url(self.issue.appstore_url,
                                                                                     test_fetch=True)

        return self.compose_validation_result(tested_ok, required_fields_ok, empty_fields, project_url_ok,
                                              appstore_url_ok)
