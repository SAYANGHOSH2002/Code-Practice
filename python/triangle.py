def print_pattern(N):
    for i in range(N):
        spaces = " " * (2 * N - 2 * i - 2)
        slashes = " /" * i
        underscores = "_ " * (2 * N - 2 * i - 2)
        print(f"{spaces}{slashes}{underscores}{slashes}\\")

N = int(input("Enter the number of lines (N): "))
print_pattern(N)
