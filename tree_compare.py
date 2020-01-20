#!/usr/bin/env python3

""" Command line interface
    Args: 2 files to compare as a json objects
"""

import sys, os, argparse
from compare import Compare
import functions

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('File1')
    parser.add_argument('File2')

    options = parser.parse_args()

    #InputFiles
    file1 = options.File1
    file2 = options.File2
    
    #Object1 to compare
    obj1 = functions.t_read(file1)
    
    #Object2 to compare
    obj2 = functions.t_read(file2)
    
    #output file1
    f1= open("output/tree1_out.txt","w") 
    
    #initiate compare
    comp = Compare(obj1, obj2,f1)
    f1.close();

    #output file2
    f2= open("output/tree2_out.txt","w") 
    comp = Compare(obj2, obj1,f2)
    f2.close()

if __name__== "__main__":
     main()