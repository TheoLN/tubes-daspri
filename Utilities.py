### COMMON CASE FUNCTIONS
MARK = "\\mark"
NMAX = 111

def Marked(arr) :
    return arr == MARK

def my_length(array : list ,i = 0):
    if Marked(array[i]):
        return i
    else:
        return my_length(array,i+1)

def attach(array  ,x,i = 0):
    if Marked(array[i]):
        array[i], array[i + 1] = x, MARK
        return array
    else:
       return attach(array,x,i+1)
    




def konsdot(x, array : list):
    for i in range (my_length(array),-1,-1):
        array[i+1]=array[i]
    array[0] = x
    return array
        


def head(arr : list) :
    return arr[0]

def tail(arr : list):
    temp = [None for i in range (NMAX)]
    temp[0] = MARK
    if my_length(arr) > 1:
        for i in range (1,my_length(arr)):
            temp = attach(temp,arr[i])
    return temp
    
def my_delArray (array : list, x):
    if array == []:
        return []
    elif array [0] == x:
        return tail(array)
    else:
        return konsdot(array[0],my_delArray(tail(array),x))


def my_strip(string : str, str):

    array = list(string)

    i = 0
    j = array[i]
    newstring = ""
    while j != str:
        newstring += j
        i += 1
        j = array[i]
    
    return newstring


def isElmt(x,array: list):
    for i in range(my_length(array)):
        if x == array[i]:
            return True
    else:
        return False
    
def my_count(x, array:list):
    if array == []:
        return 0
    elif array[0] != x :
        if my_length(array) > 1:
            return 0 + my_count(x, tail(array))
        else: 
            return 0
    else:
        if my_length(array) > 1:
            return 1 + my_count(x, tail(array))
        else:
            return 1





### SPECIAL CASE FUNCTIONS

def isAvailable(x, array): #check username availibility in matrix
    for i in range (0,my_length(array)):
        if isElmt(x,array):
            return False
        else:
            continue
    return True

def lcg(seed):
    a = 1103515245
    c = 12345
    m = 2**31
    x = seed
    while True:
        x = (a * x + c) % m
        yield x

def rng():
    gen = lcg(seed=42)
    return 1 + next(gen) % 5

    


# ***TESTING***
#print(tail([1,2,3,4,5,MARK]))
#print(my_delArray(tail([1,2,3,4,5,MARK]),4))
#print(my_count(5,[1,2,3,4,5,5,6,7,MARK,None,None]))