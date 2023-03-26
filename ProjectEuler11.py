# Function to import the data from the txt file and return a list
#
def import_data():
    f = open('ProjectEuler11.txt', 'r')
    file = f.read()
    file = file.replace('\n', '')
    file = file.split(' ')
    file = [int(i) for i in file]
    return file