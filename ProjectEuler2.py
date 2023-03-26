# Create function that will create fibonacci sequence and adds it to a list. Do not go over 4 million.

def fibo():
    fibo_list = [1,2]
    while fibo_list[-1] < 4000000:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

# Create function that will add all even numbers in the list.

def even_sum():
    sum = 0
    for i in fibo():
        if i % 2 == 0:
            sum += i
    return sum

# Print the sum of all even numbers in the list.

print(even_sum())
