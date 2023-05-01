import time

### COMMON CASE FUNCTIONS
MARK = "\\mark"
NMAX = 111

'''def Marked(arr) :
    return arr == MARK'''

def my_length(array : list ,i = 0):
    if array[i] == MARK:
        return i
    else:
        return my_length(array,i+1)

def attach(array  ,x,i = 0):
    if array[i] == MARK:
        array[i], array[i + 1] = x, MARK
        return array
    else:
       return attach(array,x,i+1)
    
def sort_id(dataCandi):
    
    for i in range(my_length(dataCandi)):
        index_min = i
        
        for j in range(i + 1, my_length(dataCandi)):
            
            
            if int(dataCandi[j][0]) < int(dataCandi[index_min][0]):
                index_min = j
         
        (dataCandi[i], dataCandi[index_min]) = (dataCandi[index_min], dataCandi[i])
    
    return dataCandi



def konsdot(x, array : list):
    for i in range (my_length(array),-1,-1):
        array[i+1]=array[i]
    array[0] = x
    return array
        


'''def head(arr : list) :
    return arr[0]'''

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






### SPECIAL CASE FUNCTIONS


seed: int
seed = int(time.time())

def lcg(seed):
    a = 110351432445
    c = 12345
    m = 2**31

    seed = (a* seed + c) % m
    return seed

def rng():
    global seed
    seed = lcg(seed)
    if  (seed % 100) < 6:
        return (seed % 100)
    else:
        return rng()

    


# ***TESTING***
#print(tail([1,2,3,4,5,MARK]))
#print(my_delArray(tail([1,2,3,4,5,MARK]),4))
#print(my_count(5,[1,2,3,4,5,5,6,7,MARK,None,None]))
