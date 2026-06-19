user_input = input("Enter a string: ")
char_count = {}

for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
result = -1


for key, value in char_count.items():
    if value > 1:
        result = -1
        break
    if value == 1:
        result = (key, value)
        break

print(result)

def find_key_position(result: dict, user_input: str) -> int:
    # Find the key with value 1
    target_key = None
    for key, value in d.items():
        if value == 1:
            target_key = key
            break

    if target_key is None:
        return -1

    # Find the position of that key in the string
    for i in range(len(s)):
        if s[i:i + len(target_key)] == target_key:
            return i

    return -1