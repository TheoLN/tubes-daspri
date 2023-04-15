### COMMON CASE FUNCTIONS
MARK = "\mark"
NMAX = 111

def Marked(string : str) :
    return str(string) == str(MARK)

def my_length(array : list,i =0 ):
    
    if Marked(array[i]) :
        return i
    else:
        return my_length(array,i+1)

def attach(array : list ,x,i=0):
    if array[i] == MARK:
        array[i], array[i + 1] = x, MARK
        return array
    else:
        return attach(array,x,i+1)

def head(arr : list) :
    return arr[0]

def tail(arr : list):
    temp = [0 for i in range (my_length(arr)+1)]
    temp[my_length(arr)-1] = MARK
    for i in range (1,my_length(arr)):
        attach(temp,arr[i])
    return temp
    
def my_delArray (array : list, x):
    if array == []:
        return []
    elif array [0] == x:
        return array[1:]
    else:
        return [array[0]] + my_delArray(array[1:],x)


def my_strip(string : str, str):
    i = 0
    array = list(string)
    while i < my_length(array):
        if array[i] == str:
            my_delArray(array, array[i])
            
        i += 1
    newstring =""
    for i in range (0, my_length(array)):
        newstring += array[i]
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
        return 0 + my_count(x, array[1:])
    else:
        return 1 + my_count(x, array[1:])





### SPECIAL CASE FUNCTIONS

def isAvailable(x, array): #check username availibility in matrix
    for i in range (0,my_length(array)):
        if isElmt(x,array):
            return False
        else:
            continue
    return True

    


# ***TESTING***

print(attach([1,2,3,4,5,MARK,0,0],6))


