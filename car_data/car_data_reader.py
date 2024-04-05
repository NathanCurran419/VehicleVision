# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:55:20 2024

@author: mspea
"""


import csv
from http.client import NOT_FOUND
import tkinter as tk
from tkinter import Frame, Image, Label, Toplevel, ttk

class ui():
    
    
    car = []
    car2 = []

  
    
        
    def __init__ (self):
        root = tk.Tk()
        root.title("Car Comparison Tool")
        root.geometry("1400x600")

        root.columnconfigure(1,weight=1)
        #root.columnconfigure(2,weight=1)
    
        main_window_frame = ui.create_frame(root, name = 'car_1')
        main_window_frame.grid(column=1,row=0, padx = 0, pady = 0)
        main_window_frame2 = ui.create_frame(root, name = 'car_2')
        main_window_frame2.grid(column=1,row=2, padx = 0, pady = 0)

        root.mainloop()
        
    def on_reset_click(frame,name):
        parent_window = frame.winfo_toplevel()
        grid_info = frame.grid_info()
        frame.destroy()
        new_frame = ui.create_frame(parent_window,name)
        new_frame.grid(column = grid_info['column'], row=grid_info['row'], padx=grid_info['padx'], pady = grid_info['pady'])
        
        

        
        
    
    def create_frame(container, name):
        
        container = ttk.Frame(container, name = name)
        
        
        
        def update_models():
            # updating model selection based on make
            selected_make = make_select.get()
            unique_models = filter_models_by_make(car_data, selected_make)
            model_select['values'] = unique_models
            
        def on_make_select(event):
            # updating model selection
            update_models()


        def on_model_select(event):
            # updating years
            update_years()

        def update_years():
        # updating year selected based on model
            selected_model = model_select.get()
            unique_year = filter_cars_by_year(car_data, selected_model)
            year_select['values'] = unique_year

        def filter_cars_by_year(data, model):
            # filtering cars by year from selected model
            make = make_select.get()
            model = model_select.get()
            return sorted(set([row['Prod. year'] for row in data if row['Model'] == model and row['Make'] == make]))
        
        
        def on_okay_click():
            make = make_select.get()
            model = model_select.get()
            year = year_select.get()
            print(make)
            print(model)
            print(year)
        def on_close_click():
            
            #closes all windows if user selects yes to exit
            def close_windows():
                container.winfo_toplevel().destroy()
                
            # closes exit prompt and sends user back to main window(container)
            def go_back():
                container.winfo_toplevel().deiconify()
                exit_prompt.destroy()
                
            # Creating second window for prompt
            global exit_prompt
            exit_prompt = Toplevel()
            exit_prompt.title("Are you sure?")
            exit_prompt.geometry("250x150")
            container.winfo_toplevel().withdraw() #hides main window instead of destroy
            yes_button = tk.Button(exit_prompt,text="Yes Exit", command = close_windows, font=40,justify='center')
            no_button = tk.Button(exit_prompt, text ="No go back...", command=go_back,font=40, justify='center')
            yes_button.grid(row=1,column = 1,padx=10,pady=30)
            no_button.grid(row=2,column=1,padx=60,pady=0)
        def display_car_comparison():
            container.winfo_toplevel().destroy()
            
            

        def on_year_select(event):
            # calling set car to pull selected car info
            if container.winfo_name() == 'car_2':
                okay_button = tk.Button(container.winfo_toplevel(),text="Select",bg='green',height = 3, width=10,font=14, command= display_car_comparison, state='active')
                okay_button.grid(row=7, column = 1, padx=10,pady=10)
                set_car()
            if container.winfo_name() == 'car_1':
                set_car()
            

                            
        def set_car():
            data = car_data
            make = make_select.get()
            model = model_select.get()
            year = year_select.get()
            selected_car = []
            
            #Creating detail Car Labels
            price_var = tk.StringVar()
            car_make_var = tk.StringVar()
            car_model_var = tk.StringVar()
            car_year_var = tk.StringVar()
            car_cat_var = tk.StringVar()
            car_gear_var = tk.StringVar()
            car_drive_var = tk.StringVar()
            car_mpg_var = tk.StringVar()

            price_label = tk.Label(container,textvariable = price_var, font = 14, bg='white')
            price_label.grid(row = 3, column = 1, padx= 10, pady = 10)
    
            car_make_label = tk.Label(container,textvariable = car_make_var, font = 14, bg='white')
            car_make_label.grid(row = 3, column = 2, padx= 10, pady = 10)
    
            car_model_label = tk.Label(container, textvariable = car_model_var, font = 14, bg='white')
            car_model_label.grid(row = 4, column = 1, padx= 10, pady = 10)
    
            car_year_label = tk.Label(container, textvariable = car_year_var, font = 14, bg='white')
            car_year_label.grid(row = 4, column = 2, padx= 10, pady = 10)
            
            car_category_label = tk.Label(container, textvariable=car_cat_var, font = 14, bg='white')
            car_category_label.grid(row = 3, column = 3, padx= 10, pady = 10)
    
            car_gear_label = tk.Label(container, textvariable =car_gear_var, font = 14, bg='white')
            car_gear_label.grid(row = 3, column = 4, padx= 10, pady = 10)
    
            car_drive_label = tk.Label(container, textvariable =car_drive_var, font = 14, bg='white')
            car_drive_label.grid(row = 4, column = 3, padx= 10, pady = 10)
    
            car_mpg_label = tk.Label(container, textvariable=car_mpg_var, font = 14, bg='white')
            car_mpg_label.grid(row = 4, column = 4, padx= 10, pady = 10)
            

            
            
            #Finding row for matching car details
            for row in data:
                if row['Model'] == model and row['Make'] == make and row['Prod. year'] == year:
                    for val in row:
                        selected_car.append((row[val]))
            if selected_car == [] :
                
                price_var.set("Price: NA")
                car_make_var.set(f'Make: {make}')
                car_model_var.set(f'Model: {model}')
                car_year_var.set(f'Year: {year}')
                car_cat_var.set(f'Category: NA')
                car_gear_var.set(f'Gear: NA')
                car_drive_var.set(f'Drive: NA')
                car_mpg_var.set(f'MPG: NA')

                
            if selected_car != []:               
                price_var.set(f'Price: ${selected_car[0]}')
                car_make_var.set(f'Make: {selected_car[1]}')
                car_model_var.set(f'Model: {selected_car[2]}')
                car_year_var.set(f'Year: {selected_car[3]}')
                car_cat_var.set(f'Category: {selected_car[4]}')
                car_gear_var.set(f'Gear Type: {selected_car[5]}')
                car_drive_var.set(f'Drive: {selected_car[6]}')
                car_mpg_var.set(f'AVG MPG: {selected_car[7]}')

            if container.winfo_name() == 'car_1':
                ui.car = selected_car
            elif container.winfo_name() == 'car_2':
                ui.car2 = selected_car


                
            
            
                

        def create_button(container):
            # create okay button
            select_button = tk.Button(container.winfo_toplevel(),text="Select",bg='grey',height = 3, width=10,font=14, command= set_car, state='disabled')
            select_button.grid(row=7, column = 1, padx=10,pady=10)

            # create reset button
            reset_button = tk.Button(container,text="Reset", bg = 'yellow', height = 1, width = 5, font = 14, command=lambda: ui.on_reset_click(container, container.winfo_name()))
            reset_button.grid(row=2,column=4,padx=10,pady=10)

            #create close button
            close_button = tk.Button(container.winfo_toplevel(),text = "Exit", bg="red", height = 3,width = 10, font = 14, command= on_close_click)
            close_button.grid(row=8,column = 1,padx=10,pady=10)
        
        
        create_button(container)          



    
        # make selection box
        make_label = tk.Label(container, text="Select Make:", bg='white')
        make_label.grid(row = 1, column = 1, padx= 10, pady = 10)
        
        make_select = ttk.Combobox(container, values=unique_makes)
        make_select.bind('<<ComboboxSelected>>', on_make_select)
        make_select.grid(row = 2, column = 1, padx= 10, pady = 10)

        # model selection box

        model_label = tk.Label(container, text="Select Model:", bg='white')
        model_label.grid(row = 1, column = 2, padx= 10, pady = 10)

        model_select = ttk.Combobox(container)
        model_select.bind('<<ComboboxSelected>>', on_model_select)
        model_select.grid(row = 2, column = 2, padx= 10, pady = 10)

        # year selection box

        year_label = tk.Label(container, text="Select Year:", bg='white')
        year_label.grid(row = 1, column = 3, padx= 10, pady = 10)

        year_select = ttk.Combobox(container)
        year_select.bind('<<ComboboxSelected>>', on_year_select)
        year_select.grid(row = 2, column = 3, padx= 10, pady = 10)

         

    
        return container
    



def load_car_data(filename):
    # read car data from file
    # try:
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
    # except UnicodeDecodeError:
    #     print(f"Found error {current_row}")


def get_unique_makes(data):
    # Getting unique car makes from data

    return sorted(set(row['Make'] for row in data))


def filter_models_by_make(data, make):
    # filtering data by make

    return sorted(set([row['Model'] for row in data if row['Make'] == make]))

# loading car data

car_data = load_car_data('car_data\CAR DATA COMBINED.csv')

# getting unqiue car makes

unique_makes = get_unique_makes(car_data)






# start user interface
if __name__ == "__main__":
    form1 = ui()
    form1
    
