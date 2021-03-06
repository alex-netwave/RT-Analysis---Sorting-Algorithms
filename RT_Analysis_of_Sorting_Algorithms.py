import math
import random
import csv
import random
import datetime
import copy


"""Insertion Sort Function Below"""
def INSERTION_SORT(A):
    for j in range(2, len(A)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key: 
            A[i+1] = A[i]
            i = i - 1
        A[i + 1] = key

def ALG1(A, i):
    INSERTION_SORT(A)
    return A[i]

"""Heapsort Functions Below"""
def LEFT(i):
    return 2 * i

def RIGHT(i):
    return 2 * i + 1


def MAX_HEAPIFY(A, i): 
    n = len(A) - 1 # A.heap-size 
    l = LEFT(i)
    r = RIGHT(i)
    if l <= n and A[l] > A[i]: 
        largest = l 
    else:
        largest = i 
    if r <= n and A[r] > A[largest]: 
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest)


def BUILD_MAX_HEAP(A): 
    n = len(A) - 1 #must subtract 1 here to account for additional 0 placed into array
    for i in range(math.floor(n/2), 0, -1):
        MAX_HEAPIFY(A, i)  

def HEAPSORT(A):

    n = len(A) - 1
    #heap_size = n # A.pop() in for suite/block handles the heap-size 
    BUILD_MAX_HEAP(A)    
    T = copy.deepcopy(A)

    for i in range(n, 0, -1):
        A[1], A[i] = A[i], A[1]
        T[i] = A.pop() #A.heap-size = A.heap-size - 1
        MAX_HEAPIFY(A, 1)
    A.pop()
    A.extend(T)
        

def ALG2(A, i):
    HEAPSORT(A)
    return A[i]

"""Randomized-select Function Below"""

def PARTITION(A, p, r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j] <= x:
            i=i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def RANDOMIZED_PARTITION(A, p, r):
    i=random.randint(p,r) #i=RANDOM(p, r)  #at mercy of RNG
    A[r], A[i] = A[i], A[r]
    return PARTITION(A, p, r)

def RANDOMIZED_SELECT(A, p, r, i):
    if p==r:
        return A[p]
    q=RANDOMIZED_PARTITION(A, p, r)
    k=q-p+1
    if i==k:
        return A[q]
    elif i<k:
        return RANDOMIZED_SELECT(A, p, q-1, i)
    else:
        return RANDOMIZED_SELECT(A, q+1, r, i-k)

def ALG3(A, n, i):
    #A.insert(0,0)
    return RANDOMIZED_SELECT(A, 1, n, i)

"""Calling the functions above to get RTs"""
#List of input sizes from 10,000 to 200,000, each 10,000 apart
n = [i for i in range(10000,210000,10000)] 

#Amount of values to average
m = 5
#Gets the current time - call before and after each call to ALGx
def time_us():
    x = datetime.datetime.now()
    return (x.hour * 3600 + x.minute * 60 + x.second) * 10**6 + x.microsecond

with open('project_data1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Group", "Averages(ms):", "ALG1", "ALG2", "ALG3"])
    for j in range(0, 8):
        a1 = [[],[],[]] #for 5 rt values from each run, for each algorithm
        print(f"Group[{j}]:")
        for k in range(m):
            #Create a list A of discrete values
            A = []
            for i in range(n[j]):
                x = random.randint(1,999999)
                y = A.count(x) #counting the instances generated by ranint that are already in the the list
                while(y != 0):  #ascertains the uniqueness of the new element
                    x = random.randint(1,999999)
                    y = A.count(x)
                A.append(x) 

            A.insert(0,0)
            C = copy.deepcopy(A)
            D = copy.deepcopy(A)
            print(f"Run[{k}]:")
            #ith smallest value    
            i = math.ceil(2*n[j]/3)
            
            t1 = time_us()
            ALG1(A, i)#ALG1 call here
            t2 = time_us()
            a1[0].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG2(C, i)#ALG2 call here
            t2 = time_us()
            a1[1].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG3(D, n[j], i)#ALG3 call here
            t2 = time_us()
            a1[2].append(abs(t2-t1))
            print(a1)
        z = [sum(a1[i])/5000 for i in range(3)]
        writer.writerow([j, " ", z[0], z[1], z[2]])

with open('project_data2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Group", "Averages(ms):", "ALG1", "ALG2", "ALG3"])
    for j in range(8, 15):
        a1 = [[],[],[]] #for 5 rt values from each run, for each algorithm
        print(f"Group[{j}]:")
        for k in range(m):
            #Create a list A of discrete values
            A = []
            for i in range(n[j]):
                x = random.randint(1,999999)
                y = A.count(x) #counting the instances generated by ranint that are already in the the list
                while(y != 0):  #ascertains the uniqueness of the new element
                    x = random.randint(1,999999)
                    y = A.count(x)
                A.append(x) 

            A.insert(0,0)
            C = copy.deepcopy(A)
            D = copy.deepcopy(A)
            print(f"Run[{k}]:")
            #ith smallest value  
            i = math.ceil(2*n[j]/3)
            
            t1 = time_us()
            ALG1(A, i)#ALG1 call here
            t2 = time_us()
            a1[0].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG2(C, i)#ALG2 call here
            t2 = time_us()
            a1[1].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG3(D, n[j], i)#ALG3 call here
            t2 = time_us()
            a1[2].append(abs(t2-t1))
            print(a1)
        z = [sum(a1[i])/5000 for i in range(3)]
        writer.writerow([j, " ", z[0], z[1], z[2]])

with open('project_data3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Group", "Averages(ms):", "ALG1", "ALG2", "ALG3"])
    for j in range(15, 19):
        a1 = [[],[],[]] #for 5 rt values from each run, for each algorithm
        print(f"Group[{j}]:")
        for k in range(m):
            #Create a list A of discrete values
            A = []
            for i in range(n[j]):
                x = random.randint(1,999999)
                y = A.count(x) #counting the instances generated by ranint that are already in the the list
                while(y != 0):  #ascertains the uniqueness of the new element
                    x = random.randint(1,999999)
                    y = A.count(x)
                A.append(x) 

            A.insert(0,0)
            C = copy.deepcopy(A)
            D = copy.deepcopy(A)
            print(f"Run[{k}]:")
            #ith smallest value  
            i = math.ceil(2*n[j]/3)
            
            t1 = time_us()
            ALG1(A, i)#ALG1 call here
            t2 = time_us()
            a1[0].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG2(C, i)#ALG2 call here
            t2 = time_us()
            a1[1].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG3(D, n[j], i)#ALG3 call here
            t2 = time_us()
            a1[2].append(abs(t2-t1))
            print(a1)
        z = [sum(a1[i])/5000 for i in range(3)]
        writer.writerow([j, " ", z[0], z[1], z[2]])
        
with open('project_data4.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Group", "Averages(ms):", "ALG1", "ALG2", "ALG3"])
    for j in range(19, 20):
        a1 = [[],[],[]] #for 5 rt values from each run, for each algorithm
        print(f"Group[{j}]:")
        for k in range(m):
            #Create a list A of discrete values
            A = []
            for i in range(n[j]):
                x = random.randint(1,999999)
                y = A.count(x) #counting the instances generated by ranint that are already in the the list
                while(y != 0):  #ascertains the uniqueness of the new element
                    x = random.randint(1,999999)
                    y = A.count(x)
                A.append(x) 

            A.insert(0,0)
            C = copy.deepcopy(A)
            D = copy.deepcopy(A)
            print(f"Run[{k}]:")
            #ith smallest value  
            i = math.ceil(2*n[j]/3)
            
            t1 = time_us()
            ALG1(A, i)#ALG1 call here
            t2 = time_us()
            a1[0].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG2(C, i)#ALG2 call here
            t2 = time_us()
            a1[1].append(abs(t2-t1))
            
            
            t1 = time_us()
            ALG3(D, n[j], i)#ALG3 call here
            t2 = time_us()
            a1[2].append(abs(t2-t1))
            print(a1)
        z = [sum(a1[i])/5000 for i in range(3)]
        writer.writerow([j, " ", z[0], z[1], z[2]])