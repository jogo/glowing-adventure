#!/usr/bin/python3

import collections
import glob


# Run from openstack git org directory

# Format
# Rule: [repo]
result = collections.defaultdict(list)

for file in glob.glob("*/tox.ini"):
    repo = file.split('/')[0]
    with open(file) as f:
        for line in f.readlines():
            if line.startswith("ignore"):
                ignore = line.split('=')[1].strip().split(',')
                for rule in ignore:
                    if "H" not in rule:
                        # We only care about hacking rules
                        continue
                    result[rule].append(repo)

print("rule: number of ignores")
for k in result:
    print("%s: %s" % (k, len(result[k])))
    print("--  %s" % result[k])
