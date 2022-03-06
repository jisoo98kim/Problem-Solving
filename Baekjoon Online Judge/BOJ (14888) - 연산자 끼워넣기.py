# Link: https://www.acmicpc.net/source/40937057

# get the count for numbers
N = int(input())
# get the sequence
seq = list(map(int, input().split()))
# get the counts for each operator
a, s, m, d = map(int, input().split())

# Set the initial max & min values to below (s.t. "any# > max / any# < min")
max_value = -1e9
min_value = 1e9

# DFS -> Recursive Func.
def dfs(seqs, cnt, add, sub, mul, div):
    global max_value, min_value

    # if we received all seq, calculate max and min values
    if cnt == N:
        max_value = max(max_value, seqs)
        min_value = min(min_value, seqs)
        return
    else:
        # Addition
        if add > 0:
            dfs(seqs + seq[cnt], cnt + 1, add - 1, sub, mul, div)

        # Subtraction
        if sub > 0:
            dfs(seqs - seq[cnt], cnt + 1, add, sub - 1, mul, div)

        # Multiplication
        if mul > 0:
            dfs(seqs * seq[cnt], cnt + 1, add, sub, mul - 1, div)

        # Division
        if div > 0:
            dfs(int(seqs / seq[cnt]), cnt + 1, add, sub, mul, div - 1)

if __name__ == '__main__':
    # Call DFS func.
    dfs(seq[0], 1, a, s, m, d)

    # Print result
    print(max_value)
    print(min_value)
