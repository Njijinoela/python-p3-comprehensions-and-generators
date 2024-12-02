#!/usr/bin/env python3

def return_evens(num_list):
    evens = []  # Create a new list to store even numbers

    for n in num_list:  # Loop through the input list
        if n % 2 == 0:  # Check if the number is even
            evens.append(n)  # Append the even number to the list

    return evens  # Return the list of even numbers


        

def make_exclamation(sentence_list):
    return [sentence +"!" for sentence in sentence_list]
