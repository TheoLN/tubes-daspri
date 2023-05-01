import Utilities as u
import os

def my_csvread(file,loaded_folder):
    rawD = [None for i in range (u.NMAX)]
    rawD[0] = u.MARK
    
    for line in open (os.path.join(loaded_folder,str(file))):
        rawD = u.attach(rawD,line)
    
    Data = [[None for i in range (5)] for i in range (u.my_length(rawD))]
    
    for i in range (1,u.my_length(rawD)):
        Dstr = ""
        j = 0
        k = rawD[i][j]
        c = 0
        while k != "\n":
            
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
    Data[u.my_length(rawD)-1] = u.MARK
    return Data

# return dalam bentuk nested list 




def initial_data (file,loaded_folder) :  ## menyiapkan initial data untuk main
    data = [[None for i in range(5)]for i in range(u.NMAX)]
    data[0] = u.MARK
    temp_data = my_csvread(file,loaded_folder)
    for i in range (u.my_length(temp_data)) :
        data = u.attach(data, temp_data[i])
    return data



 
