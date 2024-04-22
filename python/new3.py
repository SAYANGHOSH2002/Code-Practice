def find_X(A, B):
    X = 0
    diff = A ^ B  # XOR of A and B

    for i in range(30, -1, -1):
        bit_diff = (diff >> i) & 1

        if bit_diff == 1:
            X |= (1 << i)

    return X

# Read the number of test cases
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    X = find_X(A, B)
    print(X)
