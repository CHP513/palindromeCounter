# Charles (Chip) Brady
# September 2026
# This project takes in a string and returns the number of palindromes within it

# Prompt to ask for palindrome
s = input("Input (potential) Palindrome: ")


# TODO 2 Create function to count palindrome
def palindrome(s):
    # Create dictionary
    palindrome_count = 0

    # Check Substrings
    for start in range (len(s)):
        for end in range (start+1, len(s) +1):
            sub_s = s[start:end]

            # Check if substring is a palindrome
            if sub_s == sub_s[::-1]:
                palindrome_count += 1

    return palindrome_count

# Call palindrome function
print (f"Number of palindromes is {palindrome(s)}")