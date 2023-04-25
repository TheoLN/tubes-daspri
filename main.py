##libraries

##libraries
import Utilities as u
import csvparser as c
import os
import argparse

#COMMANDS
import F01_F04 as f
import F13_14 as f


##argparse
parser = argparse.ArgumentParser(description='Menjalankan program membangun candi')
parser.add_argument('folder',type=str,nargs="?",help='folder yang ingin diload')
args = parser.parse_args()

#algoritma
print ("loading . . .",end="")


if __name__ == '__main__' :
    if args.folder is None   :
    ##jika tidak diberi argumen
        print("Tidak ada nama folder yang diberikan!")
        print("Cara penggunaan : python main.py <nama_folder>")
        exit()
    else :
        loaded_folder = f.load(args.folder)   ##loaded folder akan menyimpan path file

# I N I T I A L    S T A T E 
dataUser = [[None for i in range (3)] for i in range (u.NMAX)]
dataUser[0] = u.MARK
loggedIn = [None, None]
#dataCandi = ....

dataUser = u.attach(dataUser, c.my_csvread("user.csv") )

while True:
    command = input(">>> ")

    #F01 - Login
    if command == "logIn":
        loggedIn = f.logIn(dataUser, loggedIn)
    
    #F02 - LogOut

    elif command == "logOut":
        loggedIn = f.logout(loggedIn)

    #F03 - summonJIn
    
    elif command == "summonJin":
        dataUser = f.summonJin(dataUser)
    
    #F04 - hilangkanJIn

    elif command == "hilangkanJin":
        dataUser = f.hilangkanJin(dataUser)
        
        
        
        
        
        
        
        
    
    #F09
    elif command == "laporanjin":
            if role == "bandung_bondowoso":
                laporanjin()
            else:
                print("laporanjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    #F10
    elif command ==  "laporancandi":
            if role == "bandung_bondowoso":
                laporancandi()
            else:
                print("laporancandi hanya dapat diakses oleh akun Bandung Bondowoso.")
    #F11
    elif command == "hancurkancandi":
            if role == "roro_jonggrang":
                hancurkancandi()
            else:
                print("hancurkancandi hanya dapat diakses oleh akun Roro Jonggrang.")
    #F12
    elif command == "ayamberkokok":
            if role == "ayamberkokok":
                ayamberkokok()
            else:
                print("ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    













    






    
