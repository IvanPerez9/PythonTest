'''
Created on 19 ago. 2018

@author: ivan1

 logarithmic search, with a sorted array 
 
'''

def BinarySearch_Recursive (array , x):
    if (array[-1]> x):
        mid = len(array) // 2;
        if (array[mid] == x):
            return True
        if (array[mid]> x):
            return BinarySearch_Recursive(array[:mid], x)
        return BinarySearch_Recursive(array[mid:], x)
    else:
        return False;


            