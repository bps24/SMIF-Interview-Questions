"""
    Logic Question.py 
    Author: Byrce Streeper
    Date: 3/6/2020

    input: nested list
    output: integer or float
    description: returns the sum of each individual list, given some 
        exceptions that multiply some indices by a give factor.
"""


#returns sum of a nested list with certain exceptions
def sum_ssmif(nestlist):
    lst=[]

    #iterates through each list in the nested list
    for n in range(len(nestlist)):

        #condition to sort even and odd indices of lists
        if n%2==0:
            lst.append(calc_sum(nestlist[n],9,6,2))
        else:
            lst.append(calc_sum(nestlist[n],7,4,3))
    return calc_sum(lst,4,5,0)

#helper method to sum a list given the start number, end number, and   
def calc_sum(lst, start, end, factor):

    #instantiate boolean variables to keep track of when indices should be multiplied
    occur=False
    mult=False
    count=0
    
    #iterate through every entry
    for num in lst:

        #change booleans when the start number first appears
        if num==start and not occur:
            mult=True
            occur=True

        #add the entry to a running count
        if mult:
            count+=num*factor
        else:
            count+=num

        #change back the booleans once the end number appears 
        if num==end and occur and mult:
            mult=False

    #if end number never appears
    if mult:
        return sum(lst)
    
    return count

