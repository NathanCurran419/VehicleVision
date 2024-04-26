#this section is used to address the program not finding other modules
#depending on if they are run directly or from init.py
#Authors: Nathan Curran, Michael Spears, Sarai Brown
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
from car_data import login

if __name__ == '__main__':
    login.create_login_page()
        
    

