
#r+ open the file in read as well as write mode
with open("file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()