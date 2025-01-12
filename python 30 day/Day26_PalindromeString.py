# Check for Palindrome String
# Check if a given string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

# Example usage
string = "madam"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
