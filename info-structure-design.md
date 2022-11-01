## Metadata structure design
Not all options/information will be presented to the end-user
we need to find a way to hold additional info somewhere.
This info can be both some input data (like who suggested the project, when it was added, what was the justification, etc.),
as well some additional data injected from external sources (like number of GitHub stars, forks, last commit, etc.).

The information can be used for housekeeping purposes (historical reference, improving the process),
but also to construct life UI, were you could filter, search, vote for items.


## Description design

Trying different options for presenting projects/material list:
- list with sub-items
- list with text (key: value, key: value)
- header and text
- table



### list with sub-item


    Take a look at: https://www.w3schools.com/charsets/ref_utf_misc_symbols.asp
Items:

- [entry_name](entry_url) [category1, category2] - entry_description
  - GitHub: &#9282;100 &#9733;4 &#128065;3 	&#x1F4C5; 🗓2022.10.10 11:10
  - IQ Store: 🔗\<URL>, \<category> 📅\<lastUpdatedAt> ☆\<rating>/\<votes> ⇩100
- [matco/badminton](https://github.com/matco/badminton/) [Watch App] - Badminton score tracker for Garmin watches
  - GitHub: &#9282;8 &#9733;15 👁 &#128065;5 	&#x1F4C5; 🗓2022.10.10 11:10
  - IQ Store: 🔗<https://apps.garmin.com/pl-PL/apps/51606451-57e2-4f99-9420-2ba5a80b5df6>, Device App, 📅2022.10.03 ☆3.7/90 ⇩27926
