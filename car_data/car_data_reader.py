# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:55:20 2024

@author: mspea
"""

import csv
import tkinter as tk
from tkinter import ttk


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
    selected_car = str([row for row in data
                        if row['Model'] == model and row['Make'] == make and row['Prod. year'] == year])
    car = tk.Label(root, text=selected_car)
    car.pack()
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

# make selection box
make_label = tk.Label(root, text="Select Make:")
make_label.pack()

make_select = ttk.Combobox(root, values=unique_makes)
make_select.bind('<<ComboboxSelected>>', on_make_select)
make_select.pack()

# model selection box

model_label = tk.Label(root, text="Select Model:")
model_label.pack()

model_select = ttk.Combobox(root)
model_select.bind('<<ComboboxSelected>>', on_model_select)
model_select.pack()

# year selection box

year_label = tk.Label(root, text="Select Year:")
year_label.pack()

year_select = ttk.Combobox(root)
year_select.bind('<<ComboboxSelected>>', on_year_select)
year_select.pack()

# start user interface
root.mainloop()
