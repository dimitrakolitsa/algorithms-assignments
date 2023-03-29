A = [
    "Dimitra",
    "Alexis",
    "Dimitra",
    "Giannis",
    "Giannis",
    "Giannis",
    "Dimitra",
    "Giannis",
    "Giannis",
    "Giannis",
    "Giannis",
    "Giannis",
    "Giannis",
    "Giannis",
    "Giannis",
    "Giannis",
]


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
        print("The following candidate has more than 50% of the votes:")
        print(mostVoted)
    else:
        print("No candidate has more than 50% of the votes")


pollCount(A)
