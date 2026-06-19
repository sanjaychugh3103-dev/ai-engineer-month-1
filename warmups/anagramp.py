
def compare_strings(a: str, b: str) -> bool:
    counts = {}

    if len(a) == len(b):
        for char in a:
            counts[char] = counts.get(char, 0) + 1

        for char in b:
            if char in counts:
                counts[char] -= 1
                if counts[char] < 0:
                    return False
            else:
                return False

        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

is_equal = compare_strings(string1, string2)
print("Result:", is_equal)
