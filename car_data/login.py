import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import csv
from tkinter import messagebox as msgbox
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
try:
    from car_data import VehicleVisionMainApp as main_app
except:
    import VehicleVisionMainApp as main_app




def create_login_page():
    def check_login():
        
        email = email_entry_variable.get()
        user_file = r'car_data\user_info.csv' 
        with open(user_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            for row in data:
                if email == row[5]:
                    msgbox.showinfo(title = "Thanks", message ="Login Successful")
                    root.destroy()
                    main_app.open_main_menu()
                    return

                
            


    #creating new window
    root = tk.Tk()
    root.title("Login")
    root.geometry("500x675")
    root.columnconfigure(0,weight = 1)
    root.columnconfigure(1,weight = 1)
    root.columnconfigure(2,weight = 1)
    root.columnconfigure(3,weight = 2)
    root.configure(bg='white')
    welcome_label = tk.Label(root, text="Welcome!", font=("Helvetica", 24),bg='white')
    welcome_label.grid(row = 0, column = 1, padx=(0,0), pady=(0,0))

    email_label = tk.Label(root, text="Email",border = 5,font =("Helvetica", 14),bg='white')
    email_label.grid(row = 1, column = 0, padx=(0,0),sticky='ew')
    email_entry_variable = tk.StringVar()
    email_entry = tk.Entry(root, border = 5,bg='white', textvariable=email_entry_variable)
    email_entry.grid(row=1,column = 1, padx=(0,0), pady=(15,15),sticky='ew')

    login_button = tk.Button(root, text="Login", border = 3,bg='green', command = check_login)
    login_button.grid(row=1, column = 2, padx=(10,10), pady=(0,5),sticky='ew')


    #Load logo
    logo_image = PhotoImage(file="car_data/Logo.png")
    #Creating frame for logo
    logo_frame = tk.Frame(root, name='logo_frame', border=0, borderwidth=0)
    logo_frame.configure(bg='white')
    background_image_label = tk.Label(logo_frame, image=logo_image, bg='white')
    logo_label = tk.Label(logo_frame,bg='white', image=logo_image)
    logo_label.grid(row=0, column = 0, columnspan = 3, padx=(50,0),sticky='ew')
    logo_frame.grid(row=2, column = 0, columnspan = 3,sticky='ew')


    root.mainloop()


if __name__=='__main__':
    create_login_page()
