#this section is used to address the program not finding other modules
#depending on if they are run directly or from init.py
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
from car_data import VehicleVisionMainApp as main_app

if __name__ == '__main__':
    main_app.open_main_menu()

