import json
import os

import click

from issues.parser import IssueParser
from issues.validator import IssueValidator


@click.command()
@click.option('--github-context-json', required=False, help='JSON string with GITHUB_CONTEXT object')
def validate(github_context_json) -> str:
    if not github_context_json:
        # context not given, read from env variables
        github_context_json = os.getenv('GITHUB_CONTEXT')

    result = {"success": False, "messages": []}

    if github_context_json:
        # print("github context json:")
        # print(github_context_json)
        print("we have the context, let's convert it to the json object")
        data = json.loads(github_context_json)

        body = data["event"]["issue"]["body"]
        if body:
            md = IssueParser.clear_markdown(body)
            issue = IssueParser.from_markdown(md)

            t = IssueValidator(issue)
            validation_messages = t.validate()
            if validation_messages:
                result = {"success": False, "messages": validation_messages}
        else:
            result = {"success": False, "messages": ["No issue body."]}

    else:
        result = {"success": False, "messages": ["No GITHUB_CONTEXT!"]}
    aaa = json.dumps(result)
    click.echo(aaa)

    click.echo(f"::set-output name=result::{aaa}")


if __name__ == '__main__':
    validate()
