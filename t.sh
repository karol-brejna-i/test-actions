#! /bin/bash
komunikat='{"success": false, "messages": ["No issue body.", "kupa dyzia."]}'
echo $komunikat
messages=$(echo "${komunikat}" | jq -r '.messages[] | @base64')

for row in $messages; do
    _jq() {
        echo ${row} | base64 --decode
    }
    echo $(_jq)
done