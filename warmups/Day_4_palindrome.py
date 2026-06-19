user_string = input("Enter a string: ")
print(user_string)
alphanumeric = [char.lower() for char in user_string if char.isalnum()]
print(alphanumeric)
reversed_list = alphanumeric[::-1]
print(reversed_list)
if alphanumeric == reversed_list:
    print("Palindrome!")
else:
    print("Not a palindrome.")