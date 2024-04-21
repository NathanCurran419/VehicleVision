#Vehicle Vision Main Program
#Authors: Nathan Curran, Michael Spears, Sarai Brown


import csv
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk

#this section is used to address the program not finding other modules
#depending on if they are run directly or from init.py
##=======================================================
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
try:
    from car_data import  CARS
    from car_data import  personal_information as pi
except:
    import CARS
    import personal_information as pi
##======================================================   

    
#==================
# Global Variables
#=================
#UI related
logo_image = None

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

def open_car_main(open_window):
    #the current open window must be destroyed
    #before opening a new window or it won't load
    open_window.destroy()
    CARS.run_main()

#=============================================
# FUNCTIONS/CODE FOR PERSONAL INFORMATION PAGE
# Author: Nathan Curran
#=============================================

def open_pi_window(open_window):
    open_window.destroy()
    pi.pi_window()

#=============================================
# Main Program
# Author: Nathan Curran
#=============================================

def open_main_menu():
    
    global logo_image
    
    main_root = tk.Tk("Main App","Main App","Main App")
    main_root.title("Vehicle Vision")
    main_root.geometry("500x500")
    
    #Clear Screen
    for widget in main_root.winfo_children():
         widget.destroy()
    
    #Load logo
    logo_image = PhotoImage(file="car_data\Logo.png")
    #Resize the logo by half
    logo_image = logo_image.subsample(2, 2)
    logo_label = tk.Label(main_root, image=logo_image)
    logo_label.pack()

    # Display the welcome message
    welcome_label = tk.Label(main_root, text="Welcome!", font=("Helvetica", 24))
    welcome_label.pack()

    #Navigational Buttons
    vehicle_selection_button = tk.Button(main_root, text="Vehicle Selection", command =lambda: open_car_main(main_root))
    vehicle_selection_button.pack()

    add_vehicle_button = tk.Button(main_root, text="Add new Vehicle", command=lambda: print("Navigate to Add new Vehicle"))
    add_vehicle_button.pack()

    cost_report_button = tk.Button(main_root, text="Cost report", command=lambda: print("Navigate to Cost Report"))
    cost_report_button.pack()

    personal_info_button = tk.Button(main_root, text="Personal Information", command=lambda: open_pi_window(main_root))
    personal_info_button.pack()
    
    return main_root.mainloop()

#Creating main window


def start_application():
    open_main_menu()

# Start the main loop
if __name__ == '__main__':
   start_application()

   