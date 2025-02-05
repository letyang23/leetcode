
# leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()
        length = len(self.l)
        if length % 2 == 0:
            return (self.l[length // 2 - 1] + self.l[length // 2]) / 2
        else:
            return self.l[length // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())