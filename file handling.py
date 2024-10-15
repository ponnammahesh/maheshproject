#file handling
"""f = open('samplefile.txt','r')

f1 = open('abc','w')

for data in f:
    f1.write(data)"""
#linear search
"""pos = -1
def mahesh(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False
list = [5,8,4,6,9,2]
n = 9
if mahesh(list, n):
    print("found",pos)
else:
    print("not found")"""

#binary search (taking lower bound, upper bound and
#finding mid value/element, if mid is < search value
#move lower bound to mid and repeat the process
"""pos = -1
def search(list, n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False
list = [4,7,8,12,45,99]
n=100
if search(list, n):
    print("found",pos)
else:
    print("not found")"""

#bubble sort (comparing adjacent values/elements and
#swaping if left element is bigger than right element)
"""def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
num = [5,3,8,6,7,2]
sort(num)
print(num)"""

# 'selection sort' assuming first value is min and finding min value
# by comparing it with adjacent value for each iteration
def sort(num):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if num[j] < num[minpos]:
                minpos = j
        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp

        print(num)

num = [5,3,8,6,7,2]
sort(num)
print(num)
