from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result: List[int] = [0] * n

        # Left-to-right pass: accumulate cost to bring balls from the left
        balls_on_left = 0
        moves_from_left = 0
        for i in range(n):
            result[i] += moves_from_left
            if boxes[i] == '1':
                balls_on_left += 1
            moves_from_left += balls_on_left

        # Right-to-left pass: accumulate cost to bring balls from the right
        balls_on_right = 0
        moves_from_right = 0
        for i in range(n - 1, -1, -1):
            result[i] += moves_from_right
            if boxes[i] == '1':
                balls_on_right += 1
            moves_from_right += balls_on_right

        return result


if __name__ == "__main__":
    # Simple sanity checks
    print(Solution().minOperations("110"))        # [1, 1, 3]
    print(Solution().minOperations("001011"))    # [11, 8, 5, 4, 3, 4]

