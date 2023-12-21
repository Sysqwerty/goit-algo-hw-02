from collections import deque


def is_palindrom(str: str) -> bool:
    processed_str = str.replace(" ", "").lower()
    print(f"String to check: {str}")
    char_deque = deque(processed_str)

    while len(char_deque) > 1:
        print(''.join(char_deque))
        if char_deque.popleft() != char_deque.pop():
            return False
        print(''.join(char_deque))

    return True


if __name__ == '__main__':
    print(is_palindrom("A man a plan a canal Panama"))
    # print(is_palindrom('asdsa'))
    # print(is_palindrom('qwerrewq'))
    # print(is_palindrom('Zxz'))
    # print(is_palindrom('nB mbn'))
    # print(is_palindrom('qwertyabcwq'))
