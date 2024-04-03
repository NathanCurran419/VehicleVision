# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:55:20 2024

@author: mspea
"""

import csv
from ctypes import alignment
import tkinter as tk
from tkinter import Image, ttk


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


def filter_cars_by_year(data, model):
    # filtering cars by year from selected model
    make = make_select.get()
    return sorted(set([row['Prod. year'] for row in data if row['Model'] == model and row['Make'] == make]))


def update_models():
    # updating model selection based on make
    selected_make = make_select.get()
    unique_models = filter_models_by_make(car_data, selected_make)
    model_select['values'] = unique_models


def update_years():
    # updating year selected based on model
    selected_model = model_select.get()
    unique_year = filter_cars_by_year(car_data, selected_model)
    year_select['values'] = unique_year


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
    price_label = tk.Label(root,text = (f'Price: ${selected_car[0]}'), font = 14, bg='white')
    price_label.grid(row = 3, column = 1, padx= 10, pady = 10)
    
    car_make_label = tk.Label(root,text = (f'Make: {selected_car[1]}'), font = 14, bg='white')
    car_make_label.grid(row = 3, column = 2, padx= 10, pady = 10)
    
    car_model_label = tk.Label(root, text = (f'Model: {selected_car[2]}'), font = 14, bg='white')
    car_model_label.grid(row = 4, column = 1, padx= 10, pady = 10)
    
    car_year_label = tk.Label(root, text = (f'Year: {selected_car[3]}'), font = 14, bg='white')
    car_year_label.grid(row = 4, column = 2, padx= 10, pady = 10)
    
    #Price,Make,Model,Prod. year,Category,Gear box type,Drive wheels,UHighway
    car_category_label = tk.Label(root, text=(f'Category: {selected_car[4]}'), font = 14, bg='white')
    car_category_label.grid(row = 5, column = 1, padx= 10, pady = 10)
    
    car_gear_label = tk.Label(root, text = (f'Gear Type: {selected_car[5]}'), font = 14, bg='white')
    car_gear_label.grid(row = 5, column = 2, padx= 10, pady = 10)
    
    car_drive_label = tk.Label(root, text = (f'Drive: {selected_car[6]}'), font = 14, bg='white')
    car_drive_label.grid(row = 6, column = 1, padx= 10, pady = 10)
    
    car_mpg_label = tk.Label(root, text= (f'AVG MPG: {selected_car[7]}'), font = 14, bg='white')
    car_mpg_label.grid(row = 6, column = 2, padx= 10, pady = 10)
    
    print(selected_car)


def on_make_select(event):
    # updating make selection
    update_models()
    print("Models updated")


def on_model_select(event):
    update_years()
    print("Years updated")


def on_year_select(event):
    print(f'{make_select.get()} {model_select.get()} {year_select.get()}')
    set_car()


# loading car data

car_data = load_car_data('car_data\CAR DATA COMBINED.csv')

# getting unqiue car makes

unique_makes = get_unique_makes(car_data)

# Creating user interface

root = tk.Tk()
root.title("Car Comparison Tool")
root.geometry("500x500")

background_image = tk.PhotoImage(file='car_data\VehicleVisionTempImage.png',height = 500,width=500)
background_label = tk.Label(root, image = background_image)
background_label.place(x=0,y=0)


# make selection box
make_label = tk.Label(root, text="Select Make:", bg='white')
make_label.grid(row = 1, column = 1, padx= 10, pady = 10)

make_select = ttk.Combobox(root, values=unique_makes)
make_select.bind('<<ComboboxSelected>>', on_make_select)
make_select.grid(row = 2, column = 1, padx= 10, pady = 10)

# model selection box

model_label = tk.Label(root, text="Select Model:", bg='white')
model_label.grid(row = 1, column = 2, padx= 10, pady = 10)

model_select = ttk.Combobox(root)
model_select.bind('<<ComboboxSelected>>', on_model_select)
model_select.grid(row = 2, column = 2, padx= 10, pady = 10)

# year selection box

year_label = tk.Label(root, text="Select Year:", bg='white')
year_label.grid(row = 1, column = 3, padx= 10, pady = 10)

year_select = ttk.Combobox(root)
year_select.bind('<<ComboboxSelected>>', on_year_select)
year_select.grid(row = 2, column = 3, padx= 10, pady = 10)

# start user interface
root.mainloop()
