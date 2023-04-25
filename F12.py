
from Utilities import *
from csvparser import *

def count_string(s):
    """
    Counts the length of a string without using the len() function.
    
    Parameters:
    s (str): The string to count the length of.
    
    Returns:
    int: The length of the string.
    """
    count = 0
    for char in s:
        count += 1
    return count

def AyamBerkokok(data_candi) :
    print("Kukuruyuk.. Kukuruyuk..")
    count = 0
    for i in range (100) :
        if data_candi[i]!= None :
            count += 1 
    
    if count >= 100 :
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    elif count >= 0 and count < 100 :
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
#AyamBerkokok()