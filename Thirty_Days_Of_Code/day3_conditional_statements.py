#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    #Odd - Weird
    if N % 2 == 1:
        print("Weird")
    #Even 2-6 Not Weird
    elif N in range(2,6):
        print("Not Weird")
    #Even 6-20 Weird
    elif N in range(6,21):
        print("Weird")
    #Even above 20 Not Weird
    else:
        print("Not Weird")  
