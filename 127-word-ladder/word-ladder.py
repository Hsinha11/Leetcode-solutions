from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not present, no valid sequence
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Standard BFS
        queue = deque()
        queue.append((beginWord, 1))  # (current_word, path_length_in_words)
        visited = set([beginWord])

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            # Generate all one-letter transformations
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i+1:]
                original_char = word[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original_char:
                        continue
                    candidate = prefix + c + suffix
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, length + 1))

        return 0

if __name__ == "__main__":
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))        # 0
    print(ladderLength("a", "c", ["a","b","c"]))                              # 2
