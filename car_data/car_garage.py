import csv
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk

#this section is used to address the program not finding other modules
#depending on if they are run directly or from init.py
##=======================================================
import sys
import os
from tkinter import messagebox
import csv
sys.path.append(os.path.split(sys.argv[0])[0])
try:
    from car_data import VehicleVisionMainApp as main_app
except:
    import VehicleVisionMainApp as main_app
##======================================================



def open_garage(email = "None"):
        garage_page = tk.Tk()
        garage_page.geometry("500x500")
        previous_cars = []

        def load_car_comp(page):
            page.destroy()
            garage_page = tk.Tk()
            
                
            def go_home():
                garage_page.destroy()
                main_app.open_main_menu()
        
            window_container = tk.Frame(garage_page,border=0)
            window_container.columnconfigure(1, weight = 1)
            window_container.columnconfigure(2, weight = 1)
            window_container.columnconfigure(3, weight = 1)
            title_label = tk.Label(window_container, text = 'Car Comparison Results', background='white')
            title_label.grid(row=1,column = 1, columnspan=3)
            window_container.configure(bg='white')
    
            car1 = list(previous_cars[1:7])
            car2 = list(previous_cars[7:15])

            mpg_comp_word = '' # using to dynamically change words for less than or greater than etc
            cost_comp_word = ''
    
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
        
                car1_price_label = tk.Label(window_container,textvariable = car1_price_var, font = '14', bg='white', justify = 'left')
                car1_price_label.grid(row = 4, column = 1, padx= 10, pady = 10,)
    
                car1_make_label = tk.Label(window_container,textvariable = car1_make_var, font = '14', bg='white', justify = 'left')
                car1_make_label.grid(row = 5, column = 1, padx= 10, pady = 10)
    
                car1_model_label = tk.Label(window_container, textvariable = car1_model_var, font = '14', bg='white', justify = 'left')
                car1_model_label.grid(row = 6, column = 1, padx= 10, pady = 10)
    
                car1_year_label = tk.Label(window_container, textvariable = car1_year_var, font = '14', bg='white', justify = 'left')
                car1_year_label.grid(row =7 , column = 1, padx= 10, pady = 10)
            
                car1_category_label = tk.Label(window_container, textvariable = car1_cat_var, font = '14', bg='white', justify = 'left')
                car1_category_label.grid(row = 8, column = 1, padx= 10, pady = 10)
    
                car1_gear_label = tk.Label(window_container, textvariable = car1_gear_var, font = '14', bg='white', justify = 'left')
                car1_gear_label.grid(row = 9, column = 1, padx= 10, pady = 10)
    
                car1_drive_label = tk.Label(window_container, textvariable = car1_drive_var, font = '14', bg='white', justify = 'left')
                car1_drive_label.grid(row = 10, column = 1, padx= 10, pady = 10)
    
                car1_mpg_label = tk.Label(window_container, textvariable = car1_mpg_var, font = '14', bg='white', justify = 'left')
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

        
                car2_price_label = tk.Label(window_container,textvariable = car2_price_var, font = '14', bg='white', justify = 'left')
                car2_price_label.grid(row = 4, column = 3, padx= 10, pady = 10)
    
                car2_make_label = tk.Label(window_container,textvariable = car2_make_var, font = '14', bg='white', justify = 'left')
                car2_make_label.grid(row = 5, column = 3, padx= 10, pady = 10)
    
                car2_model_label = tk.Label(window_container, textvariable = car2_model_var, font = '14', bg='white', justify = 'left')
                car2_model_label.grid(row = 6, column = 3, padx= 10, pady = 10)
    
                car2_year_label = tk.Label(window_container, textvariable = car2_year_var, font = '14', bg='white', justify = 'left')
                car2_year_label.grid(row = 7, column = 3, padx= 10, pady = 10)
            
                car2_category_label = tk.Label(window_container, textvariable=car2_cat_var, font = '14', bg='white', justify = 'left')
                car2_category_label.grid(row = 8, column = 3, padx= 10, pady = 10)
    
                car2_gear_label = tk.Label(window_container, textvariable =car2_gear_var, font = '14', bg='white', justify = 'left')
                car2_gear_label.grid(row = 9, column = 3, padx= 10, pady = 10)
    
                car2_drive_label = tk.Label(window_container, textvariable =car2_drive_var, font = '14', bg='white', justify = 'left')
                car2_drive_label.grid(row = 10, column = 3, padx= 10, pady = 10)
    
                car2_mpg_label = tk.Label(window_container, textvariable=car2_mpg_var, font = '14', bg='white', justify = 'left')
                car2_mpg_label.grid(row = 11, column = 3, padx= 10, pady = 10)

            car_details_comparison_label = tk.Label(window_container, text = car_details_comparison, font='Calibri 14 bold', bg='white')
            car_details_comparison_label.grid(row = 3, column = 1, columnspan = 3)

            done_button = tk.Button(window_container, text = 'Done', bg = 'green', command = go_home,width=10,height=3)
            done_button.grid(row=12,column = 2)
            
            garage_page.mainloop()

        # Display the welcome message
        if email == "None":
            welcome_label = tk.Label(garage_page, text="Welcome!", font=("Helvetica", 24), bg='white')
            welcome_label.grid(row = 1, column = 1)
        elif email != 'None':
            user_name = email[:email.index("@")]
            welcome_message = (f'Welcome back {user_name}!')
            welcome_label = tk.Label(garage_page, text=welcome_message, font=("Helvetica", 24), bg='white')
            welcome_label.grid(row=1,column= 1)
            garage_page.title((f'{user_name} Garage'))

        #loading user info to find email
        user_file = r'car_data/user_logs.csv' 
        with open(user_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            #when email is found load into list of previous selections
            for row in data:
                if email == row['Email']:
                    found_cars = []
                    for  k in row:
                       if k != 'Email':
                        found_cars.append(row[k]) 
                    previous_cars.append(found_cars)
                    print(found_cars)
                    
        car_selection = ttk.Combobox(garage_page, values = previous_cars)
        car_selection.bind('<<ComboboxSelected>>', lambda event: load_car_comp(garage_page))
        car_selection.grid(row=2, column=1,padx=(10), ipadx = (150))

        garage_page.mainloop()

open_garage()

