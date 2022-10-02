class Issue:

    def __init__(self, decision: str = None, summary: str = None, project_url: str = None,
                 project_type: list[str] = None,
                 license=None, appstore_url=None, simulator: str = None, device: str = None,
                 sourcecode: list[str] = None, description: str = None, additional: str = None) -> None:
        self.decision = decision
        self.summary = summary
        self.project_url = project_url
        self.project_type = project_type
        self.license = license
        self.appstore_url = appstore_url
        self.simulator = simulator
        self.device = device
        self.sourcecode = sourcecode
        self.description = description
        self.additional = additional

    def __str__(self):
        return f"Decision: '{self.decision}', Summary: '{self.summary}', Project URL: '{self.project_url}', " \
               f"Project Type: '{self.project_type}', License: '{self.license}', Appstore URL: '{self.appstore_url}', " \
               f"Simulator: '{self.simulator}', Device: '{self.device}', Sourcecode: '{self.sourcecode}', " \
               f"Description: '{self.description}', Additional: '{self.additional}'"
