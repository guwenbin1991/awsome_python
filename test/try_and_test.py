from typing import List


class Solution(object):

    def get_nth_setted_bit_position(self, k:int, arr:List[int]) -> int:
        count = 0
        for i, n in enumerate(arr):
            if n == 1:
                count = count + 1
                if count == k:
                    return i
        return -1
    
    def threeEqualParts(self, arr:List[int]):
        '''
        get the postions
        '''
        total = sum(arr)

        if total == 0:
            return (0, len(arr) - 1)
        
        if total % 3 != 0:
            return (-1, -1)

        k = total // 3
        print(k)
        start = self.get_nth_setted_bit_position(1, arr)
        mid = self.get_nth_setted_bit_position(k+1, arr)
        end = self.get_nth_setted_bit_position(2*k + 1, arr)

        while end < len(arr) and arr[start] == arr[mid] == arr[end]:
            start = start + 1
            mid = mid + 1
            end = end + 1
        
        if end == len(arr):
            return start-1, mid
        else:
            return -1, -1

def main():
    '''
    '''
    A = [0, 1]
    B = [0,1,0,0,0,0,1]
    # print(equal_arrlist(A, B))
    i = 0
    C = [0,0,1,1,0]
    D = [1,0,1,0,1]
    solution_three = Solution()
    print(solution_three.threeEqualParts(D))
    # print(solution_three.get_nth_setted_bit_position(2, D))
    # print(D[1:3])
    # print(solution_three.get_real_value([0,0,0]))



if __name__ == '__main__':
    main()
