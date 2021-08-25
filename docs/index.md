# Assignment 07
*GKumataka, 08.23.2021
*Foundations of Programming - Python

## Introduction
In This document I will be going over the process I used in completing assignment 07 of the course “Foundations of Programming: Python” by instructor Randall Root.  The assignment is to create a custom program showing use of “pickle” and binary formats.  Also including creating own exception handling.  

## Pickling
Pickling is a way to serialize and deserialize data.  It works with binary files.  The major advantage to using pickling is that it doesn’t require any other code to do this serialization.  Binary files are harder to read, although pickling does not encrypt data.  Binary files are typically smaller in file size, so maybe an advantage when working with large datasets.

## Try/Exceptions
This type of code is used to keep the program running and giving user feedback if something is wrong with the code.  This could be because the input is not an integer.  This is so that the code can run without failing.  Custom exceptions can be made to give the user more feedback about the problem.

## Creating the Program
We were tasked with creating our own program with no specific requirements.  I decided to follow the Lab7.1_starter.py for the main pickling demo.  This sample asked to take in an ID number and assign it to a name.  Then I moved onto another script for an easier demo of exception handling in python using the previous assignment of doing some math.  This involved making sure the inputs are integers and catching the dividing by zero error.
Figure 1 shows some code for the pickling demo. Figure 2 shows the output of the pickling demo code.  Figure 3 shows the math processing code to check the input and to do the math.  Figure 4 shows the main part of the math script.  Figure 5 shows the math script having a successful run and output some math.  Figure 6 shows the response when the input is not a number.  Figure 7 shows the response when division by zero happens.
