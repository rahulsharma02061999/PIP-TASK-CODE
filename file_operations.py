'''opening file in write mode'''
#opening the information.txt file
file = open("information.txt","w")
#adding content to the file which will overwrite the previous data
file.write("This is my to do task list:\n")
file.write("1.I have to wake up early in the morning\n2.I have to go for running\n3.I have to learn python\n")
#Closing the file
file.close()

'''Opening the file in read mode'''
#Here I am opening a information.txt file 
file = open("information.txt","r")
#Reading the content of the file
content = file.read()
#printing the content
print(content)
#closing the file
file.close()

'''appending data to the file'''
with open("information.txt","a") as file:
    file.write("4.I have to send daily Status.\n")


'''again opening the file to check wether data is added or not'''
with open("information.txt","r") as file:
    content = file.read()
    print(content)

'''adding many lines at the same time'''
lines = ["5. I have to eat healthy\n", "6. I have to focous on my work"]
with open("information.txt","a") as file:
    file.writelines(lines)

'''again opening the file to check wether data is added or not'''
with open("information.txt", "r") as file:
    print(file.read())

'''This is how we can save notes to a file and also we can maintain a to do list and read it later'''

