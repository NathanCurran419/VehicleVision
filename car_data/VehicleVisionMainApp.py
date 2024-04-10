#Vehicle Vision Main Program
#Authors: Nathan Curran, Michael Spears, Sarai Brown

import csv
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk



#==================
# Global Variables
#=================

#personal info
name_entry = None
avg_miles_var = None
local_cost_entry = None
state_var = None
email_entry = None

#car selection related
make_select = None
model_select = None
year_select = None



#========================================
# FUNCTIONS/CODE FOR CAR SELECTION PAGE
# Author: Michael Spears
#========================================

#Michaels Code for Car Selection
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


#Code to execute when button pressed from home page (mainly UI related)
def open_car_selection():
    global make_select, year_select, model_select

    #Clear Window 
    for widget in root.winfo_children():
        widget.destroy()

    make_label = tk.Label(root, text="Select Make:")
    make_label.pack()

    make_select = ttk.Combobox(root, values=unique_makes)
    make_select.bind('<<ComboboxSelected>>', on_make_select)
    make_select.pack()

    #model selection box

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



#=============================================
# FUNCTIONS/CODE FOR PERSONAL INFORMATION PAGE
# Author: Nathan Curran
#=============================================

#Loading State Insurance Data
state_data = {}
with open('car_data\Car Insurance.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        state_data[row['Abbreviation']] = float(row['Average'])

#Submit Personal Information
def submit_form():
    name = name_entry.get()
    avg_miles_driven = float(avg_miles_var.get())
    local_cost_per_gallon = float(local_cost_entry.get())
    state_abbreviation = state_var.get()
    avg_insurance = state_data[state_abbreviation] if state_abbreviation in state_data else 0.0
    email = email_entry.get()

    # Report stored data for development purposes
    print("Name:", name)
    print("Avg Miles Driven Per Week:", avg_miles_driven)
    print("Local Cost Per Gallon:", local_cost_per_gallon)
    print("State Abbreviation:", state_abbreviation)
    print("Average Insurance:", avg_insurance)
    print("Email:", email)

#Open personal information window
def open_personal_info():
    global name_entry, avg_miles_var, local_cost_entry, state_var, email_entry

    #Clear window
    for widget in root.winfo_children():
        widget.destroy()

    #Create lables and entries
    personal_info_label = tk.Label(root, text="Personal Information", font=("Arial", 16))
    personal_info_label.pack()

    name_label = tk.Label(root, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    avg_miles_label = tk.Label(root, text="Avg Miles Driven Per Week:")
    avg_miles_label.pack()
    avg_miles_var = tk.StringVar(root)
    avg_miles_entry = tk.Entry(root, textvariable=avg_miles_var)
    avg_miles_entry.pack()

    local_cost_label = tk.Label(root, text="Local Cost Per Gallon:")
    local_cost_label.pack()
    local_cost_entry = tk.Entry(root)
    local_cost_entry.pack()

    state_label = tk.Label(root, text="State:")
    state_label.pack()
    state_var = tk.StringVar(root)
    state_options = ["MI", "RI", "LA", "KY", "FL", "NV", "CO", "NJ", "DC", "NY", "AZ", "OK", "CT", "GA", "TX", "MO", "UT", "MT", "DE", "MD", "SD", "IL", "MN", "AR", "MS", "OR", "NM", "KS", "WV", "WY", "AL", "NE", "PA", "SC", "NH", "ND", "MA", "TN", "CA", "ID", "VT", "WA", "OH", "WI", "AK", "VA", "IN", "IA", "NC", "HI", "ME"]
    state_dropdown = tk.OptionMenu(root, state_var, *state_options)
    state_dropdown.pack()

    email_label = tk.Label(root, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.pack()

#=============================================
# Main Program
# Author: Nathan Curran
#=============================================

#Creating main window
root = tk.Tk()
root.title("Vehicle Vision")
root.geometry("500x500")

#Load logo
logo_image = PhotoImage(file="car_data\Logo.png")
#Resize the logo by half
logo_image = logo_image.subsample(2, 2)
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()

# Display the welcome message
welcome_label = tk.Label(root, text="Welcome!", font=("Helvetica", 24))
welcome_label.pack()

#Navigational Buttons
vehicle_selection_button = tk.Button(root, text="Vehicle Selection", command=open_car_selection)
vehicle_selection_button.pack()

add_vehicle_button = tk.Button(root, text="Add new Vehicle", command=lambda: print("Navigate to Add new Vehicle"))
add_vehicle_button.pack()

cost_report_button = tk.Button(root, text="Cost report", command=lambda: print("Navigate to Cost Report"))
cost_report_button.pack()

personal_info_button = tk.Button(root, text="Personal Information", command=open_personal_info)
personal_info_button.pack()

# Start the main loop
root.mainloop()