T = [
    5,
    7,
    1,
    0,
    11,
    32,
    15,
    12,
]

print(T)


def algorithm_1(T, k, n):
    H = [0] * (k + 1)
    S = [0] * n

    for i in range(k + 1):
        H[i] = 0

    for j in range(n):
        H[T[j]] += 1

    for i in range(1, k + 1):
        H[i] += H[i - 1]

    for j in range(n - 1, -1, -1):
        S[H[T[j]] - 1] = T[j]
        H[T[j]] -= 1

    print(S)


algorithm_1(T, 32, 8)
