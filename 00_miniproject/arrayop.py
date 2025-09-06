"""
There will be an array. and some operation need to perform
1. Add Element end of the Array
2. Add Elemet in any position
3. Remove Last Element
4. Remove any index
5. Print The Array
"""

import numpy as np

ls = np.array([], dtype="int32")


def addEleLast(n):
    global ls
    ls = np.append(ls, n)
    print(f"-> {n} Added At Last position\n")


def addEleAtAnyPos(pos, number):
    global ls
    if pos <= len(ls):
        ls = np.insert(ls, pos, number)
        print(f"-> {number} Added At position {pos}\n")
    else:
        print("Invalid index\n")


def removeFromLast():
    global ls
    if len(ls) != 0:
        print(f"Deleting value {ls[len(ls)-1]}")
        ls = np.delete(ls, len(ls) - 1)
    else:
        print("-> The Array Doesnot have any single Value.")


def remFromAnyIndx(idx):
    global ls
    if idx < len(ls):
        print(f"Deleting value {ls[idx]}")
        ls = np.delete(ls, idx)
    else:
        print("-> Putted wrong index")


def printArr(n):
    print("The Array is[", end=" ")
    for item in n:
        print(item, end=" ")
    print("]\n")


while True:
    try:
        print("\t\tMain Menu")
        print(
            "1. Add Element end of the Array\n2. Add Elemet in any position\n3. Remove Last Element\n4. Remove any index\n5. Print The Array\n6. Exit"
        )
        choice = int(input("-> Enter Your Choice: "))
        if choice == 1:
            inp = int(input("-> Enter Number for insert Last: "))
            addEleLast(inp)
        elif choice == 2:
            idx = int(input("-> Enter index: "))
            number = int(input("-> Enter number: "))
            addEleAtAnyPos(idx, number)
        elif choice == 3:
            removeFromLast()
        elif choice == 4:
            idx = int(input("-> Enter index: "))
            remFromAnyIndx(idx)
        elif choice == 5:
            printArr(ls)
        elif choice == 6:
            print("[ Thanks for uses ]")
            break
        else:
            print("-> Wrong Choice, Enter Again")
            continue
    except:
        print("Something went Wrong\n")
        continue
