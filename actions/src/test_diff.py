from utils.diff import parse

DIFF_FILE="../../pr-11-diff.txt"
DIFF_FILE="../../diff-1line.txt"

# read diff file
with open(DIFF_FILE, 'r') as f:
    diff = f.read()
    print(diff)


# parse diff file
parsed = parse(diff)
print(parsed)