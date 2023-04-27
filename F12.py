from main2 import *
from Utilities import *
from csvparser import *

def AyamBerkokok() :
    print("Kukuruyuk.. Kukuruyuk..")
    count = 0
    for i in range (100) :
        if data_candi[i][0]!= None :
            count += 1 
    
    if count >= 100 :
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    elif count >= 0 and count < 100 :
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
AyamBerkokok()
