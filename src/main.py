# the sorting algorithms take *slight* inspiration from the task instructions

# Imports
import random
import turtle
import time
import pytest

# Constants
DEFAULT_LIST = [3, 4, 1, 2, 1, 1, 4, 5, 1, 3, 45, 66, 6, 1, 3, 5, 4, 3, 2, 1, 5, 3, 2, 1, 5, 515, -41]
SQUARE_SIZE = 50
SLEEP_DELAY = 1

# Options
input_list_mode = False

random_list_length = 5

def randomlist():
    A = []
    for _ in range(0, 10):
        A.append(random.randint(-100, 100))
    return A

# insertion sort
def isort(A: list):
    if len(A) <= 1:
        return A
    i = 1
    while(i < len(A)):
        x = A[i]
        j = i - 1
        while(j >= 0 and A[j] > x):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x
        i += 1
    return A

def isortg(A: list):
    if len(A) <= 1:
        return A
    i = 1
    while(i < len(A)):
        x = A[i]
        j = i - 1
        while(j >= 0 and A[j] > x):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x
        update()
        i += 1
    return A


# selection sort
def ssort(A: list):
    if len(A) <= 1:
        return A
    for i in range(0, len(A)):
        mindex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[mindex]:
                mindex = j
                
        tmp = A[i]
        A[i] = A[mindex]
        A[mindex] = tmp
    return A

def ssortg(A: list):
    if len(A) <= 1:
        return A
    for i in range(0, len(A)):
        mindex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[mindex]:
                mindex = j
                
        tmp = A[i]
        A[i] = A[mindex]
        A[mindex] = tmp
        update()
    return A    


# merge sort
def msort(A: list):
    length = len(A)
    half_length = length//2
    if length <= 1:
        return A
    else:
        left = A[:half_length]
        right = A[half_length:]

        left = msort(left)
        right = msort(right)
    return merge(left, right)


def merge(A: list, B: list):
    C = []

    while len(A) > 0 and len(B) > 0:
        if A[0] > B[0]:
            C.append(B[0])
            del B[0]
        else:
            C.append(A[0])
            del A[0]
    for elem in A:
        C.append(elem)
    for elem in B:
        C.append(elem)
    
    return C

##

def msortg(A: list):
    length = len(A)
    half_length = length//2
    if length <= 1:
        return A
    else:
        left = A[:half_length]
        right = A[half_length:]

        left = msortg(left)
        right = msortg(right)
    return mergeg(left, right)


def mergeg(A: list, B: list):
    C = []

    while len(A) > 0 and len(B) > 0:
        if A[0] > B[0]:
            C.append(B[0])
            del B[0]
        else:
            C.append(A[0])
            del A[0]
    for elem in A:
        C.append(elem)
    for elem in B:
        C.append(elem)
    
    return C

# bogosort
def bsort(A: list):
    if len(A) <= 1:
        return A
    while True:
        is_sorted = True
        for ind in range(1, len(A)):
            if A[ind] < A[ind - 1]:
                is_sorted = False
        if is_sorted == False:
            random.shuffle(A)
        else:
            return A

def bsortg(A: list):
    if len(A) <= 1:
        return A
    while True:
        is_sorted = True
        for ind in range(1, len(A)):
            if A[ind] < A[ind - 1]:
                is_sorted = False
        if is_sorted == False:
            update()
            random.shuffle(A)
        else:
            update()
            return A

# haha jag gjorde det ändå vad busigt!!!!
def miraclesort(A: list): 
    while True:
        if A == sorted(A):
            return A
        else:
            return miraclesort(A)


# tests

def testisort():
    A = randomlist()
    assert(sorted(A) == isort(A))

def testmsort():
    A = randomlist()
    assert(sorted(A) == msort(A))

def testssort():
    A = randomlist()
    assert(sorted(A) == ssort(A))

def testbsort():
    A = randomlist()
    assert(sorted(A) == bsort(A))







# main

testisort()
# initialize the list
the_list = []
if input_list_mode:
    the_list = list(input().split())
    for ind in range (len(the_list)):
        the_list[ind] = int(the_list[ind])

else:
    for _ in range(random_list_length - 1):
        the_list.append(random.randint(-100, 100))
#    the_list.append(the_list[random.randint(0, len(the_list) - 1)]) # forcing a duplicate
        
fake_list = the_list.copy()
visual_list = fake_list.copy()


print(isort(fake_list))
fake_list = the_list.copy() 
print(ssort(fake_list))
fake_list = the_list.copy()
print(msort(fake_list))
fake_list = the_list.copy()

# print(bsort(fake_list))
# takes forever, obviously

# initialize the graphics



def moveto(square, turtle=turtle):
    turtle.up()
    turtle.goto(-300 + 0.5 * SQUARE_SIZE + square*SQUARE_SIZE, 50 - 0.4 * SQUARE_SIZE )

turtle.speed(10)

# make a graphical array
turtle.up()
turtle.goto(-300, 50)
turtle.down()
for _ in range(len(the_list)):
    # draw square
    for _ in range(4):
        turtle.fd(SQUARE_SIZE)
        turtle.right(90)
    # then move fd
    turtle.fd(SQUARE_SIZE)

# draw the text
text = []


for ind in range(len(the_list)):
    text.append (turtle.Turtle())

for ind in range(len(text)):
    text[ind].color("black")
    text[ind].hideturtle()
    moveto(ind, text[ind])
    text[ind].write(visual_list[ind])

def update():
    for ind in range(len(the_list)):
        if the_list[ind] != visual_list[ind]:
            time.sleep(SLEEP_DELAY * 2/3)
            text[ind].clear()
            text[ind].color("#ff8888")
            visual_list[ind] = the_list[ind]
            text[ind].write(visual_list[ind])
            time.sleep(SLEEP_DELAY/3)
            text[ind].clear()
            text[ind].color("black")
            text[ind].write(visual_list[ind])

ssortg(the_list)


# turtle.hideturtle()
