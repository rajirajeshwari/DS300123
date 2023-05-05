class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.solutions = []

    def solve(self):
        self._solve_helper(0)
        return self.solutions

    def _solve_helper(self, row):
        if row == self.N:
            solution = []
            for i in range(self.N):
                solution.append(''.join('Q' if self.board[i][j] == 1 else '.' for j in range(self.N)))
            self.solutions.append(solution)
            return True

        found_solution = False
        for col in range(self.N):
            if self._is_safe(row, col):
                self.board[row][col] = 1
                found_solution = self._solve_helper(row+1) or found_solution
                self.board[row][col] = 0
        return found_solution

    def _is_safe(self, row, col):
        for i in range(self.N):
            if self.board[row][i] == 1 or self.board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if self.board[i][j] == 1:
                return False
        return True
n = 4
solver = NQueens(n)
solutions = solver.solve()

print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
for solution in solutions:
    print()
    for row in solution:
        print(row)
