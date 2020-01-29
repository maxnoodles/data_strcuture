
class WordSearch:

    def __init__(self):
        self.d = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]
        self.m = 0
        self.n = 0
        self.visited = []

    # board 搜索的二维数组, word 搜索词
    def exist(self, board, word):
        self.m = len(board)
        assert self.m > 0
        self.n = len(board[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search_world(board, word, 0, i, j):
                    return True
        return False
    # 从 board[start_x][start_y] 开始, 寻找 word[index...word.size()]
    def search_world(self, board, word, index, start_x, start_y):

        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        if board[start_x][start_y] == word[index]:
            self.visited[start_x][start_y] = True
            # 从 start_x, start_y 出发，向四个方向寻找
            for i in self.d:
                new_x = start_x + i[0]
                new_y = start_y + i[1]
                if self.in_area(new_x, new_y) and not self.visited[new_x][new_y]:
                    if self.search_world(board, word, index+1, new_x, new_y):
                        return True
            self.visited[start_x][start_y] = False
        return False

    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n


if __name__ == '__main__':
    w = WordSearch()
    board = [
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd']
    ]
    # board = [
    #     ['a', 'b'],
    #     ['a', 'b'],
    # ]
    res = w.exist(board, 'abcdc')
    print(res)


