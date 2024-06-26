import tkinter as tk
from tkinter import messagebox
import csv
#this section is used to address the program not finding other modules
#depending on if they are run directly or from init.py
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
try:
    from car_data import VehicleVisionMainApp as main_app
    from car_data import login as login_window
except:
    import VehicleVisionMainApp as main_app
    import login as login_window
    


def pi_window():

    # Loading state data
    state_data = {}
    with open('car_data/Car Insurance.csv','r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            state_data[row['Abbreviation']] = float(row['Average'])
     
    rows = []
    
    # Submission function
    def submit_form():
        
        name = name_entry.get()
        avg_miles_driven = float(avg_miles_var.get())
        local_cost_per_gallon = float(local_cost_entry.get())
        state_abbreviation = state_var.get()
        avg_insurance = state_data[state_abbreviation] if state_abbreviation in state_data else 0.0
        email = email_entry.get()
        
        data = [name,avg_miles_driven,local_cost_per_gallon,state_abbreviation,avg_insurance,email]
        
        user_file = r'car_data\user_info.csv'
                
        # Check if email already exists in the CSV file
        with open(user_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if email == row['email']:
                    messagebox.showinfo("Error", "Email already exists. Please login instead.")
                    return

        # Append the data as a new row
        with open(user_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, avg_miles_driven, local_cost_per_gallon,state_abbreviation,avg_insurance, email])
        window.destroy()
        main_app.open_main_menu(email)

        
    def login():
        window.destroy()
        login_window.create_login_page()
    
    def main_menu():
        window.destroy()
        main_app.open_main_menu()

    window = tk.Tk()
    window.title("Personal Information")
    window.geometry('700x400')

    info_label = tk.Label(window, text="Personal Information", font=("Arial", 16))
    info_label.pack()

    desc_label = tk.Label(window, text="To help formulate individual cost reports.", font=("Arial", 14))
    desc_label.pack()

    name_label = tk.Label(window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    avg_miles_label = tk.Label(window, text="Avg Miles Driven Per Week:")
    avg_miles_label.pack()
    avg_miles_var = tk.StringVar(window)
    avg_miles_entry = tk.Entry(window, textvariable=avg_miles_var)
    avg_miles_entry.pack()

    local_cost_label = tk.Label(window, text="Local Cost Per Gallon:")
    local_cost_label.pack()
    local_cost_entry = tk.Entry(window)
    local_cost_entry.pack()

    state_label = tk.Label(window, text="State:")
    state_label.pack()
    state_var = tk.StringVar(window)
    state_options = sorted(["MI", "RI", "LA", "KY", "FL", "NV", "CO", "NJ", "DC", "NY", "AZ", "OK", "CT", "GA", "TX", "MO", "UT", "MT", "DE", "MD", "SD", "IL", "MN", "AR", "MS", "OR", "NM", "KS", "WV", "WY", "AL", "NE", "PA", "SC", "NH", "ND", "MA", "TN", "CA", "ID", "VT", "WA", "OH", "WI", "AK", "VA", "IN", "IA", "NC", "HI", "ME"])
    state_dropdown = tk.OptionMenu(window, state_var, *state_options)
    state_dropdown.pack()

    email_label = tk.Label(window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(window)
    email_entry.pack()
    
    login_button = tk.Button(window, text="Login Instead", command= login)
    login_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit_form)
    submit_button.pack()
    
    #BACK BUTTON
    back_button = tk.Button(window, text="Back to Main Menu", command= main_menu)
    back_button.pack()

    return window.mainloop()

if __name__=="__main__":
    pi_window()