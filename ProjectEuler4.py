# Create function that will create palindrome numbers and add them to a list.
#
def palindrome():
    palindrome_list = []
    for i in range(100, 999):
        for j in range(100, 1000):
            if str(i*j) == str(i*j)[::-1]:
                palindrome_list.append(i*j)
    return palindrome_list

# Create function that will find the largest number in the list.

def largest_palindrome():
    return max(palindrome())

# Print the largest palindrome number.

print(largest_palindrome())
