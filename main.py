##libraries

from utilities import *
import os
import argparse
from F13_14 import *

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
        loaded_folder = load(args.folder)   ##loaded folder akan menyimpan path file






    
