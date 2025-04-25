from bisect import bisect_left

INF = float('inf')

def go(x, i, f, a, b, dp):
    if x < 0:
        return 0
    if dp[i][x] != -1:
        return dp[i][x]

    idx_a = bisect_left(f[i], f[i][x] - a) - 1
    idx_b = bisect_left(f[i], f[i][x] - b) - 1

    cost_a = go(idx_a, i, f, a, b, dp) + a if idx_a >= 0 else INF
    cost_b = go(idx_b, i, f, a, b, dp) + b if idx_b >= 0 else INF

    dp[i][x] = min(cost_a, cost_b)
    return dp[i][x]

def solve_case(n, c, a, b, values):
    f = [[], []]
    f[0] = values
    f[1].append(f[0][-1])  # Primeiro valor de f[1] é o último de f[0]

    for i in range(1, n):
        f[1].append(f[0][i - 1] + c)

    dp = [[-1] * n for _ in range(2)]  # Inicializa dp com -1
    return min(go(n - 1, 0, f, a, b, dp), go(n - 1, 1, f, a, b, dp))

def main():
    results = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            line = line.split()
            n, c, a, b = map(int, line[:4])
            values = list(map(int, line[4:]))
            results.append(solve_case(n, c, a, b, values))
        except EOFError:
            break

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
