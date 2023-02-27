#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # myFile = open("textfile.txt", "w+")

    
    # Open the file for appending text to the end
    # myFile = open("textfile.txt", "a+")

    # # write some lines of data to the file
    # for i in range(10):
    #     myFile.write("This is some new text\n")
    
    # # close the file when done
    # myFile.close()
    
    # Open the file back up and read the contents
    myFile = open("textfile.txt", "r")
    if myFile.mode=='r':
        # contents = myFile.read()
        # print(contents)
        fl = myFile.readlines()
        for x in fl:
            print(x) 

    
if __name__ == "__main__":
    main()
