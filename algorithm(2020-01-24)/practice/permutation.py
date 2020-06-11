
class Permutation:

    def __init__(self):
        self.res = []
        self.user = [False for _ in range(3)]

    def gen_permutation(self, nums):
        if not len(nums):
            return
        self._gen_permutation(nums, 0, [])
        return self.res

    def _gen_permutation(self, nums, index, p):

        if index == len(nums):
            _p = p[:]
            self.res.append(_p)
            return

        for i in range(len(nums)):
            if not self.user[i]:
                p.append(nums[i])
                self.user[i] = True
                self._gen_permutation(nums, index+1, p)
                p.pop()
                self.user[i] = False
        return

7
if __name__ == '__main__':
    p = Permutation()
    res = p.gen_permutation([1, 2, 3])
    print(res)