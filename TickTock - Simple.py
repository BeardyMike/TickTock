# - TickTock (2022) - interview python code example by BeardyMike, designed to be easily expandable
import time
number = 1
while number < 101:
    output =""                                  # this makes sure output is empty before we begin
    if number % 3 == 0:                         # is number a tick?
        output +="tick"                         # add tick to the output variable
    if number % 5 == 0:                         # is number a tock?    
        output +="tock"                         # add tock to the output variable
    if number == 69:                            # is number 69?    
        output =""                              # empties output
        output +="Nice!"                        # add Nice! to the output variable
    if output !="":                             # check if output is empty                           
        output += "(" + str(number) + ")"       # add the actual value of number in (brackets)
    if output =="":                             # if output is empty, then output equals number
        output = number
    print(output)                               # print the result for all to see
    number += 1                                 # increment i by 1
    time.sleep(0.01)                            # add a teeny tiny pause so you can see the magic happening