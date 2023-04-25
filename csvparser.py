import Utilities as u

def my_csvread(file):
    rawD = [None for i in range (u.NMAX)]
    rawD[0] = u.MARK
    
    for line in open (file):
        rawD = u.attach(rawD,line)
    print(rawD)
    Data = [[None for i in range (5)] for i in range (u.my_length(rawD)-1)]
    for i in range (1,u.my_length(rawD)):
        Dstr = ""
        j = 0
        k = rawD[i][j]
        c = 0
        while k != "\n":
            print(k)
            if k != ";":
                Dstr += k
            else:
                Data[i-1][c] = Dstr
                c += 1
                Dstr = ""
            j += 1
            k = rawD[i][j]
        if k == "\n":
            Data[i-1][c] = Dstr
    
    return Data

# return dalam bentuk nested list 

#print(my_csvread("user.csv"))
