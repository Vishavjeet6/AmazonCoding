import sys

class Solution(object):
    def optimal_utilization(self, a, b, target):
        """
        :type a: List[List[int]]
        :type a: List[List[int]]
        :type target: int
        :rtype: List[int]
        """

        temp_value = -sys.maxsize - 1
        a_value_list = sorted(a, key=lambda x: x[1])
        b_value_list = sorted(b, key=lambda x: x[1])
        left = 0
        right = len(b_value_list) - 1
        res = []

        while left < len(a_value_list) and right >= 0:
            sum_value = a_value_list[left][1] + b_value_list[right][1]

            if sum_value > target:
                right -= 1
            else:
                if temp_value <= sum_value:
                    if temp_value < sum_value:
                        res = []
                        temp_value = sum_value
                    
                    res.append([a_value_list[left][0], b_value_list[right][0]])
                    count = right

                    while count > 0 and b_value_list[count][1] == b_value_list[count - 1][1]:
                        res.append([a_value_list[left][0], b_value_list[count - 1][0]])
                        count -= 1

                left += 1

        if not res:
            res = [[]]

        return res

def main():
    a = [[1, 2], [2, 4],[3,6]]
    b = [[1, 2]]
    target = 7
    solution = Solution()
    res = solution.optimal_utilization(a, b, target)
    print(res)
    print(solution.optimal_utilization([[1,3],[2,5],[3,7],[4,10]],[[1,2],[2,3],[3,4],[4,5]],10))

if __name__ == "__main__": 
    main()