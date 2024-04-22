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
    from car_data import personal_information as pi
except:
    import VehicleVisionMainApp as main_app
    import personal_information as pi




def create_login_page():
    
    # used to take to user info page if no account exist
    def open_create_account():
        root.destroy()
        pi.pi_window()
    
    def check_login():
        email_found = False
        email = email_entry_variable.get()
        
        # Checking if @ is in email address to confirm valid
        if '@' not in email:
            msgbox.showerror(title = "Invalid email", message = "Please enter valid email address.")
            return


        #loading user info to check if email exist
        user_file = r'car_data\user_info.csv' 
        with open(user_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            #if email is found currently will take to main menu
            for row in data:
                if email == row['email']:
                    msgbox.showinfo(title = "Thanks", message ="Login Successful")
                    email_found = True
                    root.destroy()
                    main_app.open_main_menu()
                    return
            #if email is not found will prompt to take to personal info page to create account
            if  email_found == False:
                create_account = False
                create_account = msgbox.askyesno(title = "Email not found", message = "Email not found. Create account?") # returns True of yes is clicked
                if create_account == True:
                   open_create_account()
                return
            

    #creating new window
    root = tk.Tk()
    root.title("Login")
    root.geometry("500x700")
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
    email_entry = tk.Entry(root, border = 5,bg='white', textvariable=email_entry_variable,font = '14')
    email_entry.grid(row=1,column = 1, padx=(0,0), pady=(15,15),sticky='ew')

    login_button = tk.Button(root, text="Login", border = 3,bg='green', command = check_login, font = '14')
    login_button.grid(row=1, column = 2, padx=(10,10), pady=(0,5),sticky='ew')
    create_account_button = tk.Button(root, text = "Create Account", border = 3,bg = 'blue', font='14', command = open_create_account)
    create_account_button.grid(row=2,column = 1, padx=(10,10), pady=(5,5),sticky = 'ew')

    #Load logo
    logo_image = PhotoImage(file="car_data/Logo.png")
    #Creating frame for logo
    logo_frame = tk.Frame(root, name='logo_frame', border=0, borderwidth=0)
    logo_frame.configure(bg='white')
    background_image_label = tk.Label(logo_frame, image=logo_image, bg='white')
    logo_label = tk.Label(logo_frame,bg='white', image=logo_image)
    logo_label.grid(row=0, column = 0, columnspan = 3, padx=(50,0),sticky='ew')
    logo_frame.grid(row=3, column = 0, columnspan = 3,sticky='ew')


    root.mainloop()


if __name__=='__main__':
    create_login_page()
