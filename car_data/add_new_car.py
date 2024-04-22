#this section is used to address the program not finding other modules
#depending on if they are run directly or from init.py
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
try:
    from car_data import VehicleVisionMainApp as main_app
except:
    import VehicleVisionMainApp as main_app
    
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import csv

def create_add_new_car_window():
    
    
    #saves car if not already in system
    def submit_car(price: float, make: str,model: str,year: str,cat: str,gear: str,drive: str,mpg:float):
                
        
        data = [price, make,model,year,cat,gear,drive,mpg]
        
        # Get the current directory due to issues loading from different folder
        current_dir = os.path.dirname(__file__)
        # Path to the CSV file
        car_data_path = os.path.join(current_dir, "CAR DATA COMBINED.csv")
        # Append the data as a new row
        with open(car_data_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        msgbox.showinfo(title= "Thank you", message="Thank you for your submission")


    #checks to see if car is already logged
    def check_car():
        price = price_entry.get()
        make = make_entry.get().upper()
        model= model_entry.get().upper()
        year = year_entry.get().upper()
        cat = cat_variable.get().upper()
        mpg = mpg_entry.get()
        gear = gear_variable.get().upper()
        drive = drive_variable.get().upper()
        
        try:
            price = float(price)
        except:
            msgbox.showinfo(title ="Error", message="Please enter price in form 1.00 or 1")
            return
        
        try:
            mpg = float(mpg)
        except:
            msgbox.showinfo("Error", "Please enter Average mpg in form 1.00 or 1")
            return
            
        
        if price == 0.0 or make =="" or model == "" or year == "" or cat =="" or mpg ==0.0 or gear =="" or drive == "":
            msgbox.showinfo("Error", "Please enter all fields")
            return

            
        for row in car_data:
            if row['Model'].upper() == model and row['Make'].upper() == make and row['Prod. year'] == year:
                msgbox.showinfo(title="Error", message=f'Car {year} {make} {model} already exist')
                return
        submit_car(price, make,model,year,cat,gear,drive,mpg)



    def open_main_menu():
        root.destroy()
        main_app.open_main_menu()
        
    #page settings
    root = tk.Tk()
    root.title("Enter New Car Details")
    root.geometry("350x300")
    root.resizable(width=False,height=False)
    root.configure(bg='white')
    
    
    instruct_label = tk.Label(root, text="Enter new car details",bg='white')
    instruct_label.grid(row=0, column=1, padx=(0, 0))
    
    #Price Settings
    price_label = tk.Label(root, text="Enter Price",bg='white')
    price_label.grid(row=1, column=0, padx=(10, 5))
    price_variable = tk.StringVar
    price_entry = tk.Entry(root,border=5)
    price_entry.grid(row=1, column=1, padx=(0, 10))
    # Make settings
    make_label = tk.Label(text = "Enter Make",bg='white')
    make_label.grid(row=2, column=0, padx=(10, 5))
    make_variable = tk.StringVar()
    make_entry = tk.Entry(root,border=5)
    make_entry.grid(row=2, column=1, padx=(0, 10))
    
    #Model settings
    model_label = tk.Label(root,text="Enter Model",bg='white')
    model_label.grid(row=3, column=0, padx=(10, 5))
    model_variable = tk.StringVar()
    model_entry = tk.Entry  (root,border=5)
    model_entry.grid(row=3, column=1, padx=(0, 10))

    #Year setting
    year_label = tk.Label(root, text="Enter Year",bg='white')
    year_label.grid(row=4, column=0, padx=(10, 5))
    year_variable = tk.StringVar()
    year_entry = tk.Entry(root, border =5)
    year_entry.grid(row=4, column=1, padx=(0, 10))
    
    #MPG settings
    mpg_label = tk.Label(root, text="Enter Average MPG",bg='white')
    mpg_label.grid(row=5, column=0, padx=(10, 5))
    mpg_variable = tk.StringVar()
    mpg_variable.set("0.0")
    mpg_entry = tk.Entry(root,border =5)
    mpg_entry.grid(row=5, column=1, padx=(0, 10))
    
    #Category Settings
    def get_unique_cats(data):

        # Get unique car makes from the data.
        unique_cats = sorted(set(row['Category'] for row in data))
        return unique_cats
    
    unique_cats = [any]
    unique_cats = get_unique_cats(car_data)
    cat_label = tk.Label(root, text="Select Car Category",bg='white')
    cat_label.grid(row=6, column=0, padx=(10, 5))
    cat_variable = tk.StringVar()
    cat_variable.set("Other")
    cat_selector = tk.OptionMenu(root,cat_variable, *unique_cats)
    cat_selector.grid(row=6, column=1, padx=(0, 10)) 
    
    #Gear Box settings
    gear_label = tk.Label(root, text="Select Gear Box Type",bg='white')
    gear_label.grid(row=7, column=0, padx=(10, 5))
    gear_variable = tk.StringVar()
    gear_variable.set("Other")
    unique_gears = sorted(["Manual","Automatic","Other"])
    gear_selector = tk.OptionMenu(root,gear_variable,*unique_gears)
    gear_selector.grid(row=7, column=1, padx=(0, 10))
    
    #Drive settings
    drive_label = tk.Label(root, text="Select Drive Box Type",bg='white')
    drive_label.grid(row=8, column=0, padx=(10, 5))
    drive_variable = tk.StringVar()
    drive_variable.set("Other")
    drive_gears = sorted(["4x4","Front","Rear","AWD","Other"])
    drive_selector = tk.OptionMenu(root,drive_variable,*drive_gears)
    drive_selector.grid(row=8, column=1, padx=(0, 10))
    

    # Button Settings
    add_button = tk.Button(root, text= "Add", command = check_car)
    add_button.grid(row=9, column=1, padx=(0, 10))
    main_menu_button = tk.Button(root, text = "Main Menu", command = open_main_menu)
    main_menu_button.grid(row=0, column=2, padx=(0, 0))
    
    #Display Page
    root.mainloop()

    

# Get the current directory due to issues loading from different folder
current_dir = os.path.dirname(__file__)
# Path to the CSV file
car_data_path = os.path.join(current_dir, "CAR DATA COMBINED.csv")
# Load car data from a CSV file.
with open(car_data_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    car_data = [row for row in reader]


def main():
    return create_add_new_car_window()
    
if __name__ == '__main__':
       main()

