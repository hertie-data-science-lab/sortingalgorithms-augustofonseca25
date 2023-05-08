# -*- coding: utf-8 -*-
"""
# Group Members
Team members:

- Augusto Fonseca - 225984@students.hertie-school.org
- Danial Riaz - 201678@students.hertie-school.org
- Fernando Corral - 222836@students.hertie-school.org
- Rodrigo Dornelles - 228446@students.hertie-school.org
"""
from math import log10, floor

def bucketSort(array):
    bucket = []
    list_max = max(array) # Check the maximum element
    list_min = min(array) # Check the minimum element
    exponent_max = get_exponent(list_max) # the scientific notation exponent of the maximum number
    exponent_min = get_exponent(list_min) # the scientific notation exponent of the minimum number


    if len(array) == 1: #Base case - If it`s a single-element array, returns the array
        return array
    else: # For any other case, sort it!

        # Create empty buckets
        for i in range(10): # 10 empty buckets
            bucket.append([])

        # Insert elements into their respective buckets
        for j in array: # For each element
            '''
            To define the bucket, let's divide each element of the array by 10 raised to the 
            power of the difference between the exponents of the scientific number of the maximum and minimum element. 
            This will define which numerical order will be searched (units, tens, hundreds...)
            So we obtain that digit by dividing by 10 and getting the remainder.
            '''
            index_b = (j // (10 ** (exponent_max - exponent_min))) % 10
            bucket[index_b].append(j) # include in the respective bucket


        # Sort the elements of each bucket
        for i in range(10): # For each bucket
            if len(set(bucket[i])) > 1: #Check if it`s not a single-element bucket and also if it contains different elements
                bucket[i] = bucketSort(bucket[i])# Calls the method recursively to the specific bucket


        # Get the sorted elements
        k = 0
        for i in range(10):
            for j in range(len(bucket[i])):
                array[k] = bucket[i][j]
                k += 1
        return array


def get_exponent(number): # Method do get the exponent of a number
    base10 = log10(abs(number)) #calculates the base-10 logarithm of a given number
    return floor(base10) #rounds the result down




