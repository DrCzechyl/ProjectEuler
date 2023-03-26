import csv

data = []

# open the text file for reading
with open("ProjectEuler11.txt", "r") as txtfile:
    # create a CSV reader object
    reader = csv.reader(txtfile, delimiter="\t")

    # read the data into a 2D list
    for row in reader:
        data.append(row)

# print the data to verify that it was read correctly
# print(data)


# Function to step thru data and print each number
def print_data():
    for i in range(0, 19):
        for j in range(0, 19):
            print(data[i][j], end=' ')
        print() 

print_data()
