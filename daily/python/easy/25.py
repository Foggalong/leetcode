#!/usr/bin/python3

votes = [1, 3, 1, 4, 3, 2, 2, 1, 2, 1, 3, 2]
counts = {c: votes.count(c) for c in set(votes)}

winner = [(0, 0)]
for count in counts:
    if counts[count] > winner[0][1]:
        winner = [(count, counts[count])]
    elif counts[count] == winner[0][1]:
        winner.append((count, counts[count]))

if len(winner) > 1:
    tied = ", ".join(str(c[0]) for c in winner)
    print("Candidates {} are tied with {} votes".format(tied, winner[0][1]))
else:
    print("Candidate {} won with {} votes!".format(winner[0][0], winner[0][1]))
