def is_palindrome(s: str) -> bool:
    stack = []

    for char in s:
        stack.append(char)

    for char in s:
        if char != stack.pop():
            return False

    return True
  
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")
