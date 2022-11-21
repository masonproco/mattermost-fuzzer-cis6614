#importing random module
import random

#stores random character to be used for fuzzing
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \"\'!#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~"
i = 0
j = 0
k = 0
specific = ""
randomrange = 0
selectfuzz = 0
data =""
print(characters)


#takes user input about string lenghts
print("Enter the minimum number of characters for inputs...")
min = int(input())
print("Enter the maximum number of characters for inputs...")
max = int(input())
print("Does fuzzing target require specific characters? Y/N")
specific = input()
if specific == "Y" or specific == "y" or specific == "yes" or specific == "Yes":
    print ("Indicate where in the string characters are required\nEnter a '*' for characters that are to be randomized")
    print ("Enter other characters to format the string\nExample for date format: **/**/****")
    data = input()
while selectfuzz !=1 and selectfuzz !=2 and selectfuzz !=3:
    print("Enter a number to indicate type of fuzzing\n1 = Numeric fuzzing with integers")
    print("2 = Alphanumeric fuzzing output as a string\n3 = Alpanumeric fuzzing with special characters, output as a string")
    selectfuzz = int(input())
    if selectfuzz !=1 and selectfuzz !=2 and selectfuzz !=3:
        print("Please enter 1, 2 or 3")


#going to to add the ablility to select characters that must be within the strings

def numf():
    i = 0
    global characters
    global data
    while i < 10000:
        k = 0
        j = random.randint(min, max)
        while k < j:
            #sets data to random chars from characters (incudes ints, outputs ints)
            if data[k] == "*" or data[k] == None:
                data = data + characters[random.randint(51,61)]
            k += 1
        data = int(data)
        print (data)
        i = i + 1
        data = ""

def alphanum():
    i = 0
    global characters
    global data
    while i < 10000:
        k = 0
        j = random.randint(min, max)
        while k < j:
            #sets data to random chars from characters (incudes alphanumric characters)
            if data[k] == "*" or data[k] == None:
                data = data + characters[random.randint(0,61)]
            k += 1
        print (data)
        i = i + 1
        data = ""

def alphanumspec():
    i = 0
    global characters
    global data
    while i < 10000:
        k = 0
        j = random.randint(min, max)
        while k < j:
            #sets data to random chars from characters (incudes alphanumric+special characters)
            if data[k] == "*" or data[k] == None:
                datalst = list(data)
                datalst[k] = characters[random.randint(0,96)]
                
        print (data)
        i = i + 1
        data = ""

#calls fuzz functions based on inputs
if selectfuzz == 1:
    numf()
if selectfuzz == 2:
    alphanum()
if selectfuzz == 3:
    alphanumspec()

    
#pass string to target program


