# Function that reads in a txt file and puts each single digit into a list
#
def read_file():
    f = open('ProjectEuler8.txt', 'r')
    file = f.read()
    file = file.replace('\n', '')
    file = list(file)
    return file

# Function that takes the list and multiplies the 13 adjacent digits together and stores the result in a list
#
def multiply_list():
    file = read_file()
    product_list = []
    for i in range(0, len(file) - 12):
        product = 1
        for j in range(0, 13):
            product *= int(file[i + j])
        product_list.append(product)
    return product_list

# Function that finds the largest number in the list
#
def largest_product():
    product_list = multiply_list()
    largest_product = 0
    for i in range(0, len(product_list)):
        if product_list[i] > largest_product:
            largest_product = product_list[i]
    return largest_product

# Print the largest number in the list
#
print(largest_product())

