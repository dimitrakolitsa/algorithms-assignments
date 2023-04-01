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

# ==================================== 1st WAY FOR O(N) with hashmap ============================================ #

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

# ==================================== 2nd WAY FOR O(N) without hashmap ============================================ #

def pollMajority(A):
    mostVoted = A[0] #let's say A[0] is the most-voted candidate
    counter = 1  #counter>0 means majority of votes
    for i in range(1, len(A)):
        if A[i] == mostVoted:  #if the next candidate is the same as the
            counter += 1       #mostVoted increment counter by 1 (add a vote)
        else:
            counter -= 1   #if the next candidate is different, decrease counter by 1
            if counter == 0:  #if there is a tie of votes
                mostVoted = A[i]   #changes the most-voted candidate to A[i]
                counter = 1        #and gives them 1 vote (resets the counter)

    counter = 0  #counts the votes of the most-voted candidate
    for vote in A:
        if vote == mostVoted:
            counter += 1

   #checks if the mostVoted has more than half of the total votes
    if counter > len(A) // 2:
        return mostVoted
    else:
        return "no majority"


print(pollMajority(A))