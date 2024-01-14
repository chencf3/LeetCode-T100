'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''


### 方法一：取第一行，再逆时针旋转matrix，改变matrix的值
# 时间复杂度：没分析出来，但应该大于O(m * n)...
# 空间复杂度：O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix[0]
            matrix = [[matrix[i][j] for i in range(1, len(matrix))] for j in range(len(matrix[0]) - 1, -1, -1)]
        return res


### 方法二：不改变matrix，设置上下左右4个边界值
# 时间复杂度：O(m * n)
# 空间复杂度：O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            # 最上面的一行从左往右取数
            for j in range(left, right + 1):
                res.append(matrix[up][j])
            if up == down:
                break
            up += 1
            # 最右边的一列从上往下取数
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            if left == right:
                break
            right -= 1
            # 最下面的一行从右往左取数
            for j in range(right, left - 1, -1):
                res.append(matrix[down][j])
            if up == down:
                break
            down -= 1
            # 最左边的一列从下往上取数
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            if left == right:
                break
            left += 1
        return res