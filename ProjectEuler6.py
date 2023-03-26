# Create a function that will find the sum of the square of the first 100 natural numbers

def sum_of_squares():
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i**2
    return sum_of_squares

# Create a function that will find the square of the sum of the first 100 natural numbers

def square_of_sum():
    square_of_sum = 0
    for i in range(1, 101):
        square_of_sum += i
    return square_of_sum**2

# Create a function that will find the difference between the sum of the squares and the square of the sums.

def difference():
    return square_of_sum() - sum_of_squares()

# Print the difference.

print(difference())