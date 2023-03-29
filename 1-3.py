A = [
    "Dimitra",
    "Dimitra",
    "Dimitra",
    "Dimitra",
    "Alexis",
    "Dimitra",
    "Giannis",
    "Giannis",
    "Giannis",
    "Dimitra",
]


def pollHashmap(A):
    votesMap = {}
    maxCount = 0
    mostVoted = []

    for i in A:
        if i not in votesMap:
            votesMap[i] = 1
        else:
            votesMap[i] += 1

    for candidate, votes in votesMap.items():
        if votes > maxCount:
            maxCount = votes
            mostVoted = [candidate]
        elif votes == maxCount and candidate not in mostVoted:
            mostVoted.append(candidate)

    if maxCount > len(A) / 2:
        print("The following candidates have at least 50% of the votes:")
        print(mostVoted[0])
    else:
        print("No candidate has more than 50% of the votes")


pollHashmap(A)
