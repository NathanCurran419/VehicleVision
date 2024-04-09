


import tkinter as tk
import csv


def pi_window():

    # Loading state data
    state_data = {}
    with open('car_data\Car Insurance.csv','r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            state_data[row['Abbreviation']] = float(row['Average'])

    # Submission function
    def submit_form():
        name = name_entry.get()
        avg_miles_driven = float(avg_miles_var.get())
        local_cost_per_gallon = float(local_cost_entry.get())
        state_abbreviation = state_var.get()
        avg_insurance = state_data[state_abbreviation] if state_abbreviation in state_data else 0.0
        email = email_entry.get()
        
        data = [name,avg_miles_driven,local_cost_per_gallon,state_abbreviation,avg_insurance,email]
        rows = []
        user_file = r'car_data\user_info.csv'
        with open(user_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
                
        row_index = len(rows)+1

        # Update the specific row with new data
        if row_index < len(rows):
            rows[row_index] = data
        else:
            # If row_index is out of bounds, append the data as a new row
            rows.append(data)

        # Write the updated data back to the CSV file
        with open(user_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)


        # Report stored data for development purposes
        print("Name:", name)
        print("Avg Miles Driven Per Week:", avg_miles_driven)
        print("Local Cost Per Gallon:", local_cost_per_gallon)
        print("State Abbreviation:", state_abbreviation)
        print("Average Insurance:", avg_insurance)
        print("Email:", email)
        
        window.destroy()

    window = tk.Tk()
    window.title("Personal Information")

    info_label = tk.Label(window, text="Personal Information", font=("Arial", 16))
    info_label.pack()

    desc_label = tk.Label(window, text="To help formulate individual cost reports.", font=("Arial", 10))
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

    submit_button = tk.Button(window, text="Submit", command=submit_form)
    submit_button.pack()

    return window.mainloop()

pi_window()