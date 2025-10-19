def add_spaces(s, count):
    return s + ' ' * count

def full_justify(words, max_width):
    ans = []
    ind = 0
    n = len(words)

    while ind < n:
        chars_length = len(words[ind])
        last = ind + 1

        while last < n:
            if chars_length + 1 + len(words[last]) > max_width:
                break
            chars_length += 1 + len(words[last])
            last += 1

        diff = last - ind - 1
        s = ""

        if diff == 0 or last == n:
            for i in range(ind, last):
                s += words[i]
                if i < last - 1:
                    s += ' '
            s = add_spaces(s, max_width - len(s))
        else:
            spaces = (max_width - chars_length) // diff
            rem_spaces = (max_width - chars_length) % diff
            for i in range(ind, last):
                s += words[i]
                if i < last - 1:
                    count_spaces = spaces + (1 if i - ind < rem_spaces else 0)
                    s = add_spaces(s, 1 + count_spaces)

        ans.append(s)
        ind = last

    return ans


# ---- User input section ----
n = int(input("Enter number of words: "))
words = input("Enter words separated by space: ").split()
max_width = int(input("Enter max width: "))

result = full_justify(words, max_width)

print("\nJustified Text:")
for line in result:
    print(f'"{line}"')
