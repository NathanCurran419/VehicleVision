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
from tkinter import messagebox
sys.path.append(os.path.split(sys.argv[0])[0])
try:
    from car_data import car_comp
    from car_data import personal_information as pi
    from car_data import add_new_car as add_car
except:
    import car_comp
    import personal_information as pi
    import add_new_car as add_car
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
    car_comp.run_main()
    
def open_add_vehicle(open_window):
    open_window.destroy()
    add_car.main()


def open_cost_report(open_window):
    messagebox.showinfo(title = "Cost report", message="Sorry page not yet available")
    

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
    main_root.configure(bg='white')
    #Clear Screen
    for widget in main_root.winfo_children():
         widget.destroy()
    
    #Load logo
    logo_image = PhotoImage(file="car_data/Logo.png")
    #Resize the logo by half
    logo_image = logo_image.subsample(2, 2)
    logo_label = tk.Label(main_root, image=logo_image,bg='white')
    logo_label.pack()

    # Display the welcome message
    welcome_label = tk.Label(main_root, text="Welcome!", font=("Helvetica", 24), bg='white')
    welcome_label.pack()

    #Navigational Buttons
    vehicle_selection_button = tk.Button(main_root, text="Vehicle Selection", command =lambda: open_car_main(main_root),bg='white')
    vehicle_selection_button.pack()

    add_vehicle_button = tk.Button(main_root, text="Add new Vehicle", command=lambda: open_add_vehicle(main_root),bg='white')
    add_vehicle_button.pack()

    cost_report_button = tk.Button(main_root, text="Cost report", command=lambda: open_cost_report(main_root),bg='white')
    cost_report_button.pack()

    personal_info_button = tk.Button(main_root, text="Personal Information", command=lambda: open_pi_window(main_root),bg='white')
    personal_info_button.pack()
    
    return main_root.mainloop()

#Creating main window


def start_application():
    open_main_menu()

# Start the main loop
if __name__ == '__main__':
   start_application()

   