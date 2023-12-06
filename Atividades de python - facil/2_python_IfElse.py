import math
import os
import random
import re
import sys

def main():

    n = int(input())

    confere = n%2

    if confere == 0 and n >= 2 and n <=5 :
        {
            print("Not Weird")
        }
    elif confere == 0 and n>=6 and n <= 20 :
        {
            print("Weird")
        }
    elif confere ==0 and n > 20:
        {
            print("Not Weird")
        }
    elif confere != 0:
        print("Weird")

main()
