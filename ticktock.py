# - Tick Tock (2022)
# Simple python interview programming example by BeardyMike
# https://github.com/BeardyMike
import time
number = 1
while number < 1001:
    # this is the value we'll print, this makes sure its empty
    output =""
    # is number a tick?
    if number % 3 == 0:
        # add tick to the output variable
        output +="tick"
    # is number a tock?    
    if number % 5 == 0:
        # add tock to the output variable
        output +="tock"
    # is number a tuck?    
    if number % 7 == 0:
        # add tuck to the output variable
        output +="tuck"
    # is number a tack?    
    if number % 9 == 0:
        # add tack to the output variable
        output +="tack"    
    # is number 69?    
    if number == 69:
        # add nice to the output variable
        output ="" 
        output +="nice"    
    # is number 420?    
    if number == 420:
        # add blazin to the output variable
        output =""
        output +="blazin"    
    # add the actual value of number in (brackets)
    if output !="":
        output += "("    
        output += str(number)   
        output += ")"    
    # if output is empty, then output equals number
    if output =="":
        output = number
    # print the result for all to see
    print(output)
    # increment i by 1
    number += 1
    # add a teeny tiny pause so you can see the magic happening
    time.sleep(0.01)