# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:55:20 2024

@author: mspea
"""


import csv
import tkinter as tk
from tkinter import Canvas, Frame, Image, Toplevel, ttk

class ui():
    
    
    def create_frame(container):
        
        main_window_frame = ttk.Frame(container)
        
        #grid_laout for frame
        main_window_frame.columnconfigure(0,weight=1)
        main_window_frame.columnconfigure(0,weight = 3)
        
        
        def update_models():
            # updating model selection based on make
            selected_make = make_select.get()
            unique_models = filter_models_by_make(car_data, selected_make)
            model_select['values'] = unique_models
            
        def on_make_select(event):
            # updating model selection
            update_models()
            print("Models updated")


        def on_model_select(event):
            # updating years
            update_years()
            print("Years updated")

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
                container.destroy()
                
            # closes exit prompt and sends user back to main window(main_window_frame)
            def go_back():
                container.deiconify()
                exit_prompt.destroy()
                
            # Creating second window for prompt
            global exit_prompt
            exit_prompt = Toplevel()
            exit_prompt.title("Are you sure?")
            exit_prompt.geometry("250x150")
            container.withdraw() #hides main window instead of destroy
            yes_button = tk.Button(exit_prompt,text="Yes Exit", command = close_windows, font=40,justify='center')
            no_button = tk.Button(exit_prompt, text ="No go back...", command=go_back,font=40, justify='center')
            yes_button.grid(row=1,column = 1,padx=10,pady=30)
            no_button.grid(row=2,column=1,padx=60,pady=0)
        
        def on_reset_click():
            pass
            
          
            
            
        
        def on_year_select(event):
            # calling set car to pull selected car info
            okay_button = tk.Button(main_window_frame,text="Select",bg='green',height = 3, width=10,font=14, command= set_car, state='active')
            okay_button.grid(row=7, column = 1, padx=10,pady=10)
            

                            
        def set_car():
            data = car_data
            make = make_select.get()
            model = model_select.get()
            year = year_select.get()
            selected_car = []
            
            #Finding row for matching car details
            for row in data:
                if row['Model'] == model and row['Make'] == make and row['Prod. year'] == year:
                    for val in row:
                        selected_car.append((row[val]))
                            
            #Creating Car Labels
            price_label = tk.Label(main_window_frame,text = (f'Price: ${selected_car[0]}'), font = 14, bg='white')
            price_label.grid(row = 3, column = 1, padx= 10, pady = 10)
    
            car_make_label = tk.Label(main_window_frame,text = (f'Make: {selected_car[1]}'), font = 14, bg='white')
            car_make_label.grid(row = 3, column = 2, padx= 10, pady = 10)
    
            car_model_label = tk.Label(main_window_frame, text = (f'Model: {selected_car[2]}'), font = 14, bg='white')
            car_model_label.grid(row = 4, column = 1, padx= 10, pady = 10)
    
            car_year_label = tk.Label(main_window_frame, text = (f'Year: {selected_car[3]}'), font = 14, bg='white')
            car_year_label.grid(row = 4, column = 2, padx= 10, pady = 10)
    
            #Price,Make,Model,Prod. year,Category,Gear box type,Drive wheels,UHighway
            car_category_label = tk.Label(main_window_frame, text=(f'Category: {selected_car[4]}'), font = 14, bg='white')
            car_category_label.grid(row = 5, column = 1, padx= 10, pady = 10)
    
            car_gear_label = tk.Label(main_window_frame, text = (f'Gear Type: {selected_car[5]}'), font = 14, bg='white')
            car_gear_label.grid(row = 5, column = 2, padx= 10, pady = 10)
    
            car_drive_label = tk.Label(main_window_frame, text = (f'Drive: {selected_car[6]}'), font = 14, bg='white')
            car_drive_label.grid(row = 6, column = 1, padx= 10, pady = 10)
    
            car_mpg_label = tk.Label(main_window_frame, text= (f'AVG MPG: {selected_car[7]}'), font = 14, bg='white')
            car_mpg_label.grid(row = 6, column = 2, padx= 10, pady = 10)
    
            print(selected_car)
        
        for widget in main_window_frame.winfo_children():
            widget.grid(padx=5,pady=5)

        def create_button(container):
            # create okay button
            select_button = tk.Button(main_window_frame,text="Select",bg='grey',height = 3, width=10,font=14, command= set_car, state='disabled')
            select_button.grid(row=7, column = 1, padx=10,pady=10)

            # create reset button
            reset_button = tk.Button(main_window_frame,text="Reset", bg = 'yellow', height = 3, width = 10, font = 14, command=on_reset_click)
            reset_button.grid(row=7,column=2,padx=10,pady=10)

            #create close button
            close_button = tk.Button(main_window_frame,text = "Exit", bg="red", height = 3,width = 10, font = 14, command= on_close_click)
            close_button.grid(row=7,column = 3,padx=10,pady=10)
        
        
        create_button(container)          



    
        # make selection box
        make_label = tk.Label(main_window_frame, text="Select Make:", bg='white')
        make_label.grid(row = 1, column = 1, padx= 10, pady = 10)
        
        make_select = ttk.Combobox(main_window_frame, values=unique_makes)
        make_select.bind('<<ComboboxSelected>>', on_make_select)
        make_select.grid(row = 2, column = 1, padx= 10, pady = 10)

        # model selection box

        model_label = tk.Label(main_window_frame, text="Select Model:", bg='white')
        model_label.grid(row = 1, column = 2, padx= 10, pady = 10)

        model_select = ttk.Combobox(main_window_frame)
        model_select.bind('<<ComboboxSelected>>', on_model_select)
        model_select.grid(row = 2, column = 2, padx= 10, pady = 10)

        # year selection box

        year_label = tk.Label(main_window_frame, text="Select Year:", bg='white')
        year_label.grid(row = 1, column = 3, padx= 10, pady = 10)

        year_select = ttk.Combobox(main_window_frame)
        year_select.bind('<<ComboboxSelected>>', on_year_select)
        year_select.grid(row = 2, column = 3, padx= 10, pady = 10)

         

    
        return main_window_frame
    
    
    def create_root_window(self):
        root = tk.Tk()
        root.title("Car Comparison Tool")
        root.geometry("1400x1400")
    
        root.columnconfigure(0,weight=4)
        root.columnconfigure(1,weight=1)
    
        main_window_frame = ui.create_frame(root)
        main_window_frame.grid(column=1,row=0)
        
    
        root.mainloop()


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

form1 = ui()



# start user interface
if __name__ == "__main__":
    form1.create_root_window()
