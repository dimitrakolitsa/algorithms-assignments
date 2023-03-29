A = ["Dimitra", "Dimitra", "Giannis", "Dimitra", "Alexis", "Giannis", "Dimitra"]


def pollSquare(A):
    maxCounter = 0
    mostVoted = []

    for i in A:
        iCounter = 0

        for j in A:
            if i == j:
                iCounter += 1

        if iCounter > maxCounter:
            maxCounter = iCounter
            mostVoted.append(i)
        elif (iCounter == maxCounter) and (i not in mostVoted):
            mostVoted.append(i)
            # print(mostVoted)

    if maxCounter > (len(A) / 2):
        print("The following candidate has more than 50% of the votes:")
        print(mostVoted[0])
    else:
        print("No candidate has more than 50% of the votes")


pollSquare(A)
