# New Issue/PR validation

When a dedicated issue is created
using ["Project proposal" form template](../.github/ISSUE_TEMPLATE/project_template.yml), we can use GitHub actions to
validate the data and enrich it with some additional information.

What we can validate:

- URLs (project, App Store)
- Is the proposed project already on the list (either "proper" one or rejected projects list)
- Was a known device entered?
- Is required info entered (for example, the project should be tested in the simulator or on a device)
- Is declared license the same as defined in the project settings

Some information can be added to the issue (for example in a form of a comment):

- proposed project metadata, like watchers, forks, stars, last update date, license and others (archived or not, empty
  or not, etc.)
- number of downloads in the store

This could help with the decision on Issue/PR approval.

Some other stuff can be done with GH actions, either on PR merge, issue creation or periodically:

- we could count number of proposals per user (accepted/total) - this would allow to appreciate the best contributors (
  mention in README, etc.)
- update the Issue form (for example, adding new elements to a dropdown list of devices)

## Obtaining additional information

Knowing what do we want to validate and what information we could add, let's consider how to get the extra data.

### What information do we have?

- issue body markdown - event.issue.body from GitHub context
- issue creator (author) login - actor, triggering_actor, event.issue.user.login from GitHub context; (we don't have the
  email); TODO: check how it looks when the issue is edited
- REST endpoint to retrieve creator (author) email - "url": "https://api.github.com/users/karol-brejna-i"
- license info - event.repository.license from GitHub context ("key": "apache-2.0", "name": "Apache License 2.0", "
  spdx_id": "Apache-2.0")

### App Store data

From the Connect IQ Store, for a given app, we can get:

- app type
- number of downloads
- average rating and number of ratings