from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_index_by_char: Dict[str, int] = {}
        window_start_index: int = 0
        max_window_length: int = 0

        for window_end_index, current_char in enumerate(s):
            if current_char in last_seen_index_by_char:
                previous_index: int = last_seen_index_by_char[current_char]
                if previous_index >= window_start_index:
                    # Move the start just after the previous index of current_char
                    window_start_index = previous_index + 1

            last_seen_index_by_char[current_char] = window_end_index
            current_window_length: int = window_end_index - window_start_index + 1
            if current_window_length > max_window_length:
                max_window_length = current_window_length

        return max_window_length


if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(solver.lengthOfLongestSubstring("bbbbb"))     # 1
    print(solver.lengthOfLongestSubstring("pwwkew"))    # 3


