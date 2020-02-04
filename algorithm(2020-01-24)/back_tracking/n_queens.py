
class NQueens:

    def __init__(self):
        self.res = []
        self.col = []
        self.dia1 = []
        self.dia2 = []

    def solve_n_queens(self, n):
        row = []
        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2*n-1)]
        self.dia2 = [False for _ in range(2*n-1)]
        self.put_queen(n, 0, row)
        return self.res

    # 尝试在一个 n 皇后问题中，摆放第 index 行的皇后位置
    def put_queen(self, n, index, row):
        if index == n:
            self.res.append(self.generate_board(n, row))
            return

        for i in range(n):
            # 尝试将第 index 行的皇后摆放在第 i 列
            if not self.col[i] and not self.dia1[i+index] and not self.dia2[index-i+n-1]:
                self.col[i], self.dia1[i+index], self.dia2[index-i+n-1] = True, True, True
                row.append(i)
                self.put_queen(n, index+1, row)
                self.col[i], self.dia1[i+index], self.dia2[index-i+n-1] = False, False, False
                row.pop()
        return

    def generate_board(self, n, row):
        board = [['.' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            board[i][row[i]] = 'Q'
        return board


if __name__ == '__main__':
    n = NQueens()
    res = n.solve_n_queens(4)
    for i in res:
        for j in i:
            print(j)
        print('\n')
