def segfunc(x, y):
    return max(x, y)

ide_ele = 0

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    # k番目の要素をxに更新
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    # l以上r未満の区間から取得
    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


N, Q = map(int, input().split())

a = [0] * (N+1)
seg = SegTree(a, segfunc, ide_ele)
for _ in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        _, pos, x = que
        seg.update(pos, x)
    elif que[0] == 2:
        _, l, r = que
        print(seg.query(l, r))
