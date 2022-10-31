## Description design

Trying different options for presenting projects/material list: 
- list with sub-items 
- list with text (key: value, key: value)
- header and text 
- table

## Metadata structure design 
Not all options/information will be presented to the end-user 
we need to find a way to hold additional info somewhere.
This info can be both some input data (like who suggested the project, when it was added, what was the justification, etc.),
as well some additional data injected from external sources (like number of GitHub stars, forks, last commit, etc.). 

The information can be used for housekeeping purposes (historical reference, improving the process),
but also to construct life UI, were you could filter, search, vote for items. 
