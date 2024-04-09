#-*-coding:utf-8-*-
"""
CreatedonMonApr122:08:542024

@author:mspea
"""

import car_data.car_data_reader as cdr
import car_data.personal_information as pi
import tkinter as tk
from tkinter import ttk

cdr.ui()
car1 = list(cdr.ui.car)
car2 = list(cdr.ui.car2)


car_details_comparison = '' 
if car1 != [] and car2 != []:
    if round(float(car1[7]),2)  <= round(float(car2[7]),2):
        mpg_comp_word = " MPG less than "
    elif round(float(car1[7]),2)  >= round(float(car2[7]),2):
        mpg_comp_word = ' MPG more than '
    if round(float(car1[0]),2) <= round(float(car2[0]),2):
        cost_comp_word = ' less than '
    elif round(float(car1[0]),2) >= round(float(car2[0]),2):
        cost_comp_word = ' more than '
    car_details_comparison = (f'{car1[1]} gets {round(float(car1[7]),2) - round(float(car2[7]),2)} {mpg_comp_word} {car2[1]} and {car1[1]} cost ${round(float(car1[0]),2) - round(float(car2[0]),2)} {cost_comp_word} {car2[1]}\n')
else:
    car_details_comparison = 'No car selected'






def create_main_window_frame(window, window_name):
    def go_home():
        window.destroy()
        pi.pi_window()
        
    window_container = ttk.Frame(window,name = window_name)
    window_container.columnconfigure(1, weight = 1)
    window_container.columnconfigure(2, weight = 1)
    window_container.columnconfigure(3, weight = 1)

    title_label = tk.Label(window_container, text = 'Car Comparison Results')
    title_label.grid(row=1,column = 1, columnspan=3)
    

    if car1 != [] and car2 != []:

        car1_price_var = tk.StringVar()
        car1_make_var = tk.StringVar()
        car1_model_var = tk.StringVar()
        car1_year_var = tk.StringVar()
        car1_cat_var = tk.StringVar()
        car1_gear_var = tk.StringVar()
        car1_drive_var = tk.StringVar()
        car1_mpg_var = tk.StringVar()

        car2_price_var = tk.StringVar()
        car2_make_var = tk.StringVar()
        car2_model_var = tk.StringVar()
        car2_year_var = tk.StringVar()
        car2_cat_var = tk.StringVar()
        car2_gear_var = tk.StringVar()
        car2_drive_var = tk.StringVar()
        car2_mpg_var = tk.StringVar()

        # Car 1 label details
        car1_price_var.set(f'Price: ${car1[0]}')
        car1_make_var.set(f'Make: {car1[1]}')
        car1_model_var.set(f'Model: {car1[2]}')
        car1_year_var.set(f'Year: {car1[3]}')
        car1_cat_var.set(f'Category: {car1[4]}')
        car1_gear_var.set(f'Gear Type: {car1[5]}')
        car1_drive_var.set(f'Drive: {car1[6]}')
        car1_mpg_var.set(f'AVG MPG: {car1[7]}')
        
        car1_price_label = tk.Label(window_container,textvariable = car1_price_var, font = 14, bg='white', justify = 'left')
        car1_price_label.grid(row = 4, column = 1, padx= 10, pady = 10,)
    
        car1_make_label = tk.Label(window_container,textvariable = car1_make_var, font = 14, bg='white', justify = 'left')
        car1_make_label.grid(row = 5, column = 1, padx= 10, pady = 10)
    
        car1_model_label = tk.Label(window_container, textvariable = car1_model_var, font = 14, bg='white', justify = 'left')
        car1_model_label.grid(row = 6, column = 1, padx= 10, pady = 10)
    
        car1_year_label = tk.Label(window_container, textvariable = car1_year_var, font = 14, bg='white', justify = 'left')
        car1_year_label.grid(row =7 , column = 1, padx= 10, pady = 10)
            
        car1_category_label = tk.Label(window_container, textvariable = car1_cat_var, font = 14, bg='white', justify = 'left')
        car1_category_label.grid(row = 8, column = 1, padx= 10, pady = 10)
    
        car1_gear_label = tk.Label(window_container, textvariable = car1_gear_var, font = 14, bg='white', justify = 'left')
        car1_gear_label.grid(row = 9, column = 1, padx= 10, pady = 10)
    
        car1_drive_label = tk.Label(window_container, textvariable = car1_drive_var, font = 14, bg='white', justify = 'left')
        car1_drive_label.grid(row = 10, column = 1, padx= 10, pady = 10)
    
        car1_mpg_label = tk.Label(window_container, textvariable = car1_mpg_var, font = 14, bg='white', justify = 'left')
        car1_mpg_label.grid(row = 11, column = 1, padx= 10, pady = 10)

        # Car 2 label details
        car2_price_var.set(f'Price: ${car2[0]}')
        car2_make_var.set(f'Make: {car2[1]}')
        car2_model_var.set(f'Model: {car2[2]}')
        car2_year_var.set(f'Year: {car2[3]}')
        car2_cat_var.set(f'Category: {car2[4]}')
        car2_gear_var.set(f'Gear Type: {car2[5]}')
        car2_drive_var.set(f'Drive: {car2[6]}')
        car2_mpg_var.set(f'AVG MPG: {car2[7]}')
        
        car2_price_label = tk.Label(window_container,textvariable = car2_price_var, font = 14, bg='white', justify = 'left')
        car2_price_label.grid(row = 4, column = 3, padx= 10, pady = 10)
    
        car2_make_label = tk.Label(window_container,textvariable = car2_make_var, font = 14, bg='white', justify = 'left')
        car2_make_label.grid(row = 5, column = 3, padx= 10, pady = 10)
    
        car2_model_label = tk.Label(window_container, textvariable = car2_model_var, font = 14, bg='white', justify = 'left')
        car2_model_label.grid(row = 6, column = 3, padx= 10, pady = 10)
    
        car2_year_label = tk.Label(window_container, textvariable = car2_year_var, font = 14, bg='white', justify = 'left')
        car2_year_label.grid(row = 7, column = 3, padx= 10, pady = 10)
            
        car2_category_label = tk.Label(window_container, textvariable=car2_cat_var, font = 14, bg='white', justify = 'left')
        car2_category_label.grid(row = 8, column = 3, padx= 10, pady = 10)
    
        car2_gear_label = tk.Label(window_container, textvariable =car2_gear_var, font = 14, bg='white', justify = 'left')
        car2_gear_label.grid(row = 9, column = 3, padx= 10, pady = 10)
    
        car2_drive_label = tk.Label(window_container, textvariable =car2_drive_var, font = 14, bg='white', justify = 'left')
        car2_drive_label.grid(row = 10, column = 3, padx= 10, pady = 10)
    
        car2_mpg_label = tk.Label(window_container, textvariable=car2_mpg_var, font = 14, bg='white', justify = 'left')
        car2_mpg_label.grid(row = 11, column = 3, padx= 10, pady = 10)

    car_details_comparison_label = ttk.Label(window_container, text = car_details_comparison, font='Calibri 14 bold')
    car_details_comparison_label.grid(row = 3, column = 1, columnspan = 3)

    done_button = tk.Button(window_container, text = 'Done', bg = 'green', command = go_home)
    done_button.grid(row=12,column = 2)

    
    return window_container


class comparison_window():
    com_window = tk.Tk()
    com_window.title('Car comparison')
    com_window.geometry('900x600')
    com_window.columnconfigure(1,weight = 1)
    
    main_window = create_main_window_frame(com_window,window_name = 'main comparison window')
    main_window.grid(row = 1, column =1)



    com_window.mainloop()
    





if __name__ == '__main__':
    comparison_window()
