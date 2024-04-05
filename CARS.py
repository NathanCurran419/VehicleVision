#-*-coding:utf-8-*-
"""
CreatedonMonApr122:08:542024

@author:mspea
"""

from tokenize import Double
import car_data.car_data_reader as cdr
import car_data.personal_information as pi

print("Select first car.")
cdr.ui()
car1 = cdr.ui.car
print("Selected a second car.")
car2 = cdr.ui.car2
print(f'Your first selected car: {car1}')
print(f'Your second selected car: {car2}')
print(f'{car1[1]} gets {float(car1[7]) - float(car2[7])} MPG than {car2[1]} and {car1[1]} cost ${float(car1[0]) - float(car2[0])} then {car2[1]}\n')


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
        
    