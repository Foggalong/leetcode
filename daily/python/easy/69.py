#!/usr/bin/env python3

titles = ['Name', 'Address', 'Description']
entries = [
    ['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
    ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
    ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']
]

maxs = [max(len(e[i]) for e in entries+titles) for i in range(len(titles))]


def entryprint(entry):
    line = "|"
    for i in range(len(entry)):
        line += " " + entry[i] + " "*(maxs[i] - len(entry[i])) + " |"
    print(line)


divider = "".join(["+-" + ("-" * m) + "-" for m in maxs]) + "+"


print(divider)
entryprint(titles)
for entry in entries:
    print(divider)
    entryprint(entry)
print(divider)
