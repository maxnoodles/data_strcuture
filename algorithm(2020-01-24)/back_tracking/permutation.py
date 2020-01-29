
class Permutation:

    def __init__(self):
        self.res = []
        self.used = []

    def generate_permutation(self, nums):
        if not nums:
            return self.res
        p = []
        self.used = [False for _ in nums]
        self._generate_permutation(nums, 0, p)
        return self.res

    def _generate_permutation(self, nums, index, p):
        if index == len(nums):
            _p = p[:]
            self.res.append(_p)
            print(f'get p: {p}, return')
            return

        for i in range(len(nums)):
            if not self.used[i]:
                print(f'nums = {nums}, i = {i}, use {nums[i]}, index = {index}')
                p.append(nums[i])
                self.used[i] = True
                print(f'push p = {p}, used = {self.used}')
                self._generate_permutation(nums, index+1, p)
                p.pop()
                self.used[i] = False
                print(f'pop p = {p}, used = {self.used}', end='\n')

        return


if __name__ == '__main__':
    p = Permutation()
    res = p.generate_permutation([1, 2, 3])
    print(res)
