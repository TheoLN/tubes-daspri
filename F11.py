from csvparser import *
from Utilities import *


def HancurkanCandi (data_candi) :
    
    id = int(input("Masukkan ID candi : "))
    count = 0
    for i in range (1,101):
        if data_candi[i][0]!=None and int(data_candi[i][0]) == id :
            jawab = str(input("Apakah anda yakin ingin menghancurkan candi ID: "))
            count = 1
            if jawab == 'Y' or jawab == 'y' :
                data_candi[i] = None
                break
    if count == 0 :
        print("Tidak ada candi dengan  ID tersebut.")
        return
    valid=True
    i=2
    print(data_candi)
    while valid==True:
        if data_candi[i]!=None and data_candi[i-1]==None:
            data_candi[i],data_candi[i-1]=data_candi[i-1],data_candi[i]
            print(data_candi[i-1])
            data_candi[i-1][0]=str(int(data_candi[i-1][0])-1)
            print(data_candi[i-1])
            valid=False
        i+=1
        if i==101:
            break
#HancurkanCandi()
#print(data_candi)