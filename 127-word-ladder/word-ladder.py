from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    L = len(beginWord)
    patterns = defaultdict(list)

    for word in word_set:
        for i in range(L):
            pat = word[:i] + "*" + word[i+1:]
            patterns[pat].append(word)

    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps

        for i in range(L):
            pat = word[:i] + "*" + word[i+1:]
            for nei in patterns.get(pat, []):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, steps + 1))
            patterns[pat] = []
    return 0


if __name__ == "__main__":
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))        # 0
    print(ladderLength("a", "c", ["a","b","c"]))                              # 2