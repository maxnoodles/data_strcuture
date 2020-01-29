
class LetterCombinations:

    def __init__(self):
        self.res = []
        self.letter_map = [
            ' ',   # 0
            '',    # 1
            'abc',  # 2
            'def',  # 3
            'ghi',  # 4
            'jkl',  # 5
            'mno',  # 6
            'pqrs',  # 7
            'tuv',  # 8
            'wxyz'  # 9
        ]
        self.count = 1

    def letter_combinations(self, digits):
        if not digits:
            return []
        self._find_combination(digits, 0, '')
        return self.res

    def _find_combination(self, digits, index, s):
        self.count += 1
        print(f'{index} : {s}')
        if index == len(digits):
            self.res.append(s)
            print(f'get {s}, return')
            return
        c = digits[index]
        assert(0 <= int(c) <= 9 and c != 1)
        letters = self.letter_map[int(c)]
        for i in letters:
            print(f'digits[{index}] = {c}, use {i}')
            self._find_combination(digits, index+1, s + i)

        print(f'digits[{index}] = {c} complete, return')
        return


if __name__ == '__main__':
    c = LetterCombinations()
    res = c.letter_combinations('234')
    print(res)
    print(c.count)
