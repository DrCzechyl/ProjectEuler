# Create functions that will check if a number is prime

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
# Create a loop that steps by 1 and checks if the number is prime. If it is, add it to a list. When the list is 10001 items long, print the last item in the list.

def prime_list():
    prime_list = []
    i = 1
    while len(prime_list) < 10001:
        if is_prime(i) == True:
            prime_list.append(i)
        i += 1
    return prime_list

# Print the last item in the list.

print(prime_list()[-1])