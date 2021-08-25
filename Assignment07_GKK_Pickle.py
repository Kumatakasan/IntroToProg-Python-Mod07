# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# G.Kumataka, 8.20.2021, Started basic functions
# G.Kumataka, 8.23.2021, Finalized script and commented
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'Names.dat'
lstCustomer = []
strChoice = ""

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = []
    with open(file_name, 'ab') as objFile:
        pickle.dump(list_of_data, objFile)
        print("Contents were appended to File!")
        print()

def read_data_from_file(file_name):
    objFileData = []  # Creates a new list
    with open(file_name, 'rb') as objFile:
        while True:
            try:
                objFileData.append(pickle.load(objFile))  # This command loads the full data list.
            except EOFError:
                break
        return objFileData
# Presentation ------------------------------------ #
# This is a simple program that asks for a user to input a ID number and name.
# Then the program saves the ID and name in a pickle format.
# Once saved the file is read back with all the contents.

intId = int(input("Please enter an ID: "))
strName = input("Please enter a Name: ")
lstCustomer = [intId, strName]  # Saving as list

save_data_to_file(strFileName, lstCustomer)  # Calling save function

print("Now reading contents from binary file!")
newList = read_data_from_file(strFileName)  # Calling read function and saving variable
print(newList)
