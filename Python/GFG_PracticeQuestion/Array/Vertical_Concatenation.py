# Given a String Matrix, perform column-wise concatenation of strings, handling variable lists lengths.
import numpy

string = numpy.array([["Gfg", "good"], ["is", "for"]] )
print("Before: ", string)
concate_1 = numpy.array(string[0,:])
concate_2 = numpy.array(string[1,:])
print("After: ",concate_1+concate_2)