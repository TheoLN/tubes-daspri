import Utilities as u

def my_csvread(file):
    rawD = [None for i in range (u.NMAX)]
    rawD[0] = u.MARK
    
    for line in open (file):
        rawD = u.attach(rawD, u.my_strip(line, "\n"))
    Data = [[] for j in range ((u.my_length(rawD))-1)]

    for i in range (1, u.my_length(rawD)):
        Dstr = ""
        for j in rawD[i]:
            if j != ";":
                Dstr += j
            else:
                Data[i-1] = u.attach(Data[i-1],Dstr)
            Dstr = ""
        Data[i-1] = u.attach(Data[i-1],Dstr)

    return Data
# return dalam bentuk nested list 