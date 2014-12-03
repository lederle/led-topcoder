'''
You are given a String code containing a message composed entirely 
of decimal digits ('0'-'9'). Each digit consists of some number of 
dashes (see diagram below). A "check function" of a message is 
defined as the total number of dashes in the message. Return the 
value of the check function for the message represented in code.
'''

class CheckFunction:
    def newFunction(self, code):
        checks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
        return sum([checks[int(key)] for key in code])
