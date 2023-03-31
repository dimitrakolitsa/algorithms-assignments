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


# ======================================= METHOD 1: NO COMPARISONS ===================================#
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

    if leftCandidate != None:
        mostVotedCandidate = leftCandidate
    else:
        mostVotedCandidate = rightCandidate

    if countTotal(A, mostVotedCandidate) > len(A) / 2:
        return mostVotedCandidate
    else:
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


# ======================================= METHOD 2: WITH COMPARISONS ===================================#


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def pollCount(A):
    mergeSort(A)
    # print(A)
    counter = [0] * len(A)
    maxCounter = 0
    mostVoted = ""
    j = 0

    for i in range(len(A)):
        if i == 0:
            counter[j] += 1
            if counter[j] > maxCounter:
                maxCounter = counter[j]
                mostVoted = A[i]

        elif A[i] == A[i - 1]:
            counter[j] += 1
            if counter[j] > maxCounter:
                maxCounter = counter[j]
                mostVoted = A[i]

        else:
            counter[j + 1] += 1
            j += 1

    if maxCounter > (len(A) / 2):
        print("The following candidate has more than 50% of the votes:", mostVoted)
    else:
        print("No candidate has more than 50% of the votes")


pollCount(A)
