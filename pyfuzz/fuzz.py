#importing random module
import random
import math
import qrcode
import os

# Import custom modules
import enumerate_utils
import generator
from logger import FuzzLogger


#stores random character to be used for fuzzing
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \"\'!#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~"
i = 0
j = 0
k = 0
specific = ""
randomrange = 0
selectfuzz = 0
data =""

iterations = 10
depth = 1

log = FuzzLogger.initializeLogging()

# Fuzz the function
def fuzzFunction(functions):

    count = 0

    for function in functions:
        i = 0
        function_name =     function[0]
        arg_count =         function[1]
        function_address =  function[2]

        # Generate random input and fuzz
        while count < iterations:
            inputs = []

            for i in range(0, arg_count):
                inputs.append(generator.generateRandomBytes())
            
            res = []

            try:
                res = function_address(*inputs)
            except Exception as err:

                error_state = {
                    "Function Name" : function_name,
                    "Input"         : inputs,
                    "Error Message" : repr(err)
                }

                log.info(repr(error_state))


            children = enumerate_utils.checkChildObject(res)

            if children != []:
                enumerate_utils.enumerateChildFunctions(qrcode, children, res, depth)

            count += 1

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

def fuzzInt():
    print("yeet")

def main():

    functions = enumerate_utils.enumerateLibraryFunctions(qrcode)
    functions_and_param_count = enumerate_utils.enumerateFunctionArgs(functions)

    fuzzFunction(functions_and_param_count)

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
    
    #calls fuzz functions based on inputs
    if selectfuzz == 1:
        numf()
    if selectfuzz == 2:
        alphanum()
    if selectfuzz == 3:
        alphanumspec()

if __name__ == "__main__":
    main()
    
