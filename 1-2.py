A = [
    "Dimitra",
    "Alexis",
    "Dimitra",
    "Giannis",
    "Giannis",
    "Giannis",
    "Dimitra",
    "Dimitra",
    "Dimitra",
]


def pollCountLog(A):
    if len(A) == 1:
        return A[0]

    left = A[: len(A) // 2]
    right = A[len(A) // 2 :]

    leftMost = pollCountLog(left)
    rightMost = pollCountLog(right)

    if leftMost == rightMost:
        return leftMost

    leftCandidate = countMost(A, leftMost)
    rightCandidate = countMost(A, rightMost)

    if countTotal(A, leftCandidate) > len(A) / 2:
        return leftCandidate
    elif countTotal(A, rightCandidate) > len(A) / 2:
        return rightCandidate

    return None


def countMost(A, candidate):
    count = 0
    for i in A:
        if i == candidate:
            count += 1
        else:
            count -= 1
    if count > 0:
        return candidate
    else:
        return None


def countTotal(A, candidate):
    count = 0
    for i in A:
        if i == candidate:
            count += 1
    return count


winner = pollCountLog(A)
if winner is not None:
    print("The following candidate has more than 50% of the votes:", winner)
else:
    print("No candidate has more than 50% of the votes")
