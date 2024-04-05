#-*-coding:utf-8-*-
"""
CreatedonMonApr122:08:542024

@author:mspea
"""

import car_data.car_data_reader as cdr
import car_data.personal_information as pi

print("Select first car.")
cdr.ui()
car1 = cdr.ui.car
print("Selected a second car.")
cdr.ui()
car2 = cdr.ui.car
print(f'Your first selected car: {car1}')
print(f'Your second selected car: {car2}')


done = ""
while done != "Y":
    done = input("Quit? Y or N\n").upper()
    if done == "Y":
        print("Thanks for stopping by!")
    elif done != "Y" and done != "N":
        print(f'Your first selected car: {car1}')
        print(f'Your second selected car: {car2}')
        done = input("Please enter Y or N \n").upper()
    elif done == "N":
        print(f'Your first selected car: {car1}')
        print(f'Your second selected car: {car2}')
        done = input("Please enter Y once done reviewing data\n").upper()
        
    