import tkinter as tk
from tkinter import ttk
import os
import csv

class window():
    car = []
    car2 = []    

    def load_car_data(filename):
        # Load car data from a CSV file.
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    
    def get_unique_makes(data):
        # Get unique car makes from the data.
        return sorted(set(row['Make'] for row in data))

    # Get the current directory due to issues loading from different folder
    current_dir = os.path.dirname(__file__)
    # Path to the CSV file
    car_data_path = os.path.join(current_dir, "CAR DATA COMBINED.csv")
    # Load car data from the CSV file
    car_data = load_car_data(car_data_path)
    # Get unique car makes from the car data
    unique_makes = get_unique_makes(car_data)
    
    @staticmethod
    def ui():
        root = tk.Tk()
        root.title("Car Comparison Tool")
        root.geometry("650x500")
        root.resizable(0,0) # Prevents resizing to help with background image layout
        
        # Function to create the UI for the car comparison tool.
        # Load the background image
        bg_image_path = os.path.join(os.path.dirname(__file__), "VehicleVisionTempImage.png")
        background_image = tk.PhotoImage(file=bg_image_path)
        background_image_label = tk.Label(root, image=background_image)
        background_image_label.place(x=0, y=0)
        background_image_label.image_ref = background_image

        # Create window frames
        main_window_frame = window.create_frame(root, name='car_1', bg= background_image)
        main_window_frame.grid(column=1, row=1, padx=10, pady=10)
        main_window_frame2 = window.create_frame(root, name='car_2', bg= background_image)
        main_window_frame2.grid(column=1, row=2, padx=10, pady=10)
        
        return root.mainloop()
               

    @staticmethod
    def on_reset_click(frame, name, bg):
        # Reset button click handler.
        parent_window = frame.winfo_toplevel()
        grid_info = frame.grid_info()
        frame.destroy()

        new_frame = window.create_frame(parent_window, name, bg)
        new_frame.grid(column=grid_info['column'], row=grid_info['row'], padx=grid_info['padx'], pady=grid_info['pady'])

    @staticmethod
    def create_frame(container, name, bg):
        # Function to create a new frame.
        container = ttk.Frame(container, name=name, border=0, borderwidth=0, padding=10)
        background_image_label = ttk.Label(container, image=bg)

        if name == 'car_1':
            background_image_label.place(x=-20, y=-20)
        else:
            background_image_label.place(x=-20, y=-160)

        def update_models():
            # Update the models.
            okay_button = tk.Button(container.winfo_toplevel(), text="Select", bg='grey', height=3, width=10,
                                    font=14, state='disable')
            okay_button.grid(row=7, column=1, padx=10, pady=10)
            selected_make = make_select.get()
            unique_models = filter_models_by_make(selected_make)
            model_select['values'] = unique_models

        def on_make_select(event):
            # for make selection.
            update_models()

        def filter_models_by_make(make):
            # Filter models by make.
            return sorted(set([row['Model'] for row in window.car_data if row['Make'] == make]))

        make_label = tk.Label(container, text="Select Make:", bg='skyblue')
        make_label.grid(row=1, column=1, padx=10, pady=10)

        make_select = ttk.Combobox(container, values=window.unique_makes)
        make_select.bind('<<ComboboxSelected>>', on_make_select)
        make_select.grid(row=2, column=1, padx=10, pady=10)
        model_label = tk.Label(container, text="Select Model:", bg='skyblue')
        model_label.grid(row=1, column=2, padx=10, pady=10)

        model_select = ttk.Combobox(container)
        model_select.bind('<<ComboboxSelected>>', lambda event: update_years())
        model_select.grid(row=2, column=2, padx=10, pady=10)

        year_label = tk.Label(container, text="Select Year:", bg='skyblue')
        year_label.grid(row=1, column=3, padx=10, pady=10)

        year_select = ttk.Combobox(container)
        year_select.bind('<<ComboboxSelected>>', lambda event: on_year_select())
        year_select.grid(row=2, column=3, padx=10, pady=10)

        def update_years():
            # Update the years.
            selected_model = model_select.get()
            unique_year = filter_cars_by_year(selected_model)
            year_select['values'] = unique_year

        def filter_cars_by_year(model):
            # Filter cars by year.
            make = make_select.get()
            return sorted(set([row['Prod. year'] for row in window.car_data if row['Model'] == model and row['Make'] == make]))

        def on_close_click():
            # for close button.
            def close_windows():
                container.winfo_toplevel().destroy()

            def go_back():
                container.winfo_toplevel().deiconify()
                exit_prompt.destroy()

            exit_prompt = tk.Toplevel()
            exit_prompt.title("Are you sure?")
            exit_prompt.geometry("250x150")
            container.winfo_toplevel().withdraw()
            yes_button = tk.Button(exit_prompt, text="Yes Exit", command=close_windows, font=40, justify='center')
            no_button = tk.Button(exit_prompt, text="No go back...", command=go_back, font=40, justify='center')
            yes_button.grid(row=1, column=1, padx=10, pady=30)
            no_button.grid(row=2, column=1, padx=60, pady=0)

        def display_car_comparison():
            container.winfo_toplevel().destroy()
            # Display the car comparison.
        
        def on_year_select():
            # Enables Select Button
            if container.winfo_name() == 'car_2':
                okay_button = tk.Button(container.winfo_toplevel(), text="Select", bg='green', height=3, width=10,
                                        font=14, command=display_car_comparison, state='active')
                okay_button.grid(row=7, column=1, padx=10, pady=10)
                set_car()
            if container.winfo_name() == 'car_1':
                set_car()

        def set_car():
            # Set the selected car.
            make = make_select.get()
            model = model_select.get()
            year = year_select.get()
            selected_car = []

            for row in window.car_data:
                if row['Model'] == model and row['Make'] == make and row['Prod. year'] == year:
                    for val in row:
                        selected_car.append((row[val]))

            if container.winfo_name() == 'car_1':
                window.car = selected_car
            elif container.winfo_name() == 'car_2':
                window.car2 = selected_car

        def create_button(container):
            # Create buttons.
            select_button = tk.Button(container.winfo_toplevel(), text="Select", bg='grey', height=3, width=10,
                                      font=14, command=display_car_comparison, state='disabled')
            select_button.grid(row=7, column=1, padx=10, pady=10)

            reset_button = tk.Button(container, text="Reset", bg='yellow', height=1, width=5, font=14,
                                     command=lambda: window.on_reset_click(container, container.winfo_name(), bg))
            reset_button.grid(row=2, column=4, padx=10, pady=10)

            close_button = tk.Button(container.winfo_toplevel(), text="Exit", bg="red", height=3, width=10, font=14,
                                     command=on_close_click)
            close_button.grid(row=8, column=1, padx=10, pady=10)

        create_button(container)

        return container

def open_car_data():
    return window.ui()


if __name__ == '__main__':
    open_car_data()
