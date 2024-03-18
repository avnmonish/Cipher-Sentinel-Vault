

# Importing necessary modules :
import tkinter as tk
from tkinter import messagebox
import os

# Cipher modules :
import adfgvx
import polybius
import fsqr
import bifid

# Random Password Generator module :
import random_pass

# File structure handling :
if not os.path.isdir('Keys') :
    os.mkdir('Keys')

if not os.path.isdir('Data') :
    os.mkdir('Data')

# Function to handle LOGIN button click :
def login() :
   
    # Username of the user.
    username = entry_username.get()
   
    # Keys of the user.
    K1 = entry_key1.get()
    K2 = entry_key2.get()
    K3 = entry_key3.get()
    
    # If usernmame, K1, K2, K3 are entered :
    if username and K1 and K2 and K3 :

        try:
           
            # Opening the key file to read the keys.
            with open(f"Keys/{username}_key.txt", 'r') as file1 :
                data = file1.readlines()
    
            # Decrypting the keys read from the file.
    
            # fileK1 = polybius.decrypt(data[0].strip())
            # fileK2 = polybius.decrypt(data[1].strip())
            # fileK3 = polybius.decrypt(data[2].strip())
           
            fileK1 = data[0].strip()
            fileK1 = polybius.decrypt(fileK1)
           
            fileK2 = data[1].strip()
            fileK2 = polybius.decrypt(fileK2)
           
            fileK3 = data[2].strip()
            fileK3 = polybius.decrypt(fileK3)
    
            # Checking whether the user entered valid keys.
            if fileK1 == K1 and fileK2 == K2 and fileK3 == K3 :
               
                # Show success message box after successfull login.
                messagebox.showinfo(title = "Login Success", message = "Login Successful!")
    
                # Show password manager window.
                password_manager_window(username, K1, K2, K3)
                #login_window.destroy()
    
               
                # Minimizing the login window after login.
                root.state(newstate = 'iconic')
    
            # If any of the key(s) is/are invalid shows an ERROR message.
            else :
               
                messagebox.showerror(title = "Invalid Keys", message = "Please try again.")
    
    
        # If the username is invalid display an ERROR message.
        except IOError :
            messagebox.showerror(title = "Invalid Username", message = "Please try again.")
       
       
        # Deleting the input details from the input boxes.
        entry_username.delete(0, tk.END)
        entry_key1.delete(0, tk.END)
        entry_key2.delete(0, tk.END)
        entry_key3.delete(0, tk.END)
   

# Function to handle SIGNUP button click :
def signup() :

    # Details that user entered.
    username = entry_username.get()
    K1 = entry_key1.get()
    K2 = entry_key2.get()
    K3 = entry_key3.get()

    # If usernmame, K1, K2, K3 are entered :
    if username and K1 and K2 and K3 :

        # Checking for username conflicts.
        if not os.path.isfile(f"Keys/{username}_key.txt") :
           
            # Opening the key file to store the keys.
            with open(f"Keys/{username}_key.txt", 'w') as file :
    
                # Encrypting the keys.
                k1 = polybius.encrypt(K1)
                k2 = polybius.encrypt(K2)
                k3 = polybius.encrypt(K3)
               
                # Writing the keys to the file.
                file.write(f"{k1}\n")
                file.write(f"{k2}\n")
                file.write(f"{k3}\n")
           
            # Deleting the input details from the input boxes.
            entry_username.delete(0, tk.END)
            entry_key1.delete(0, tk.END)
            entry_key2.delete(0, tk.END)
            entry_key3.delete(0, tk.END)
           
            # Signup Success.
            messagebox.showinfo(title = "Signup Successful", message = "Signup Successful!")
       
        # If the entered username already exixts.
        else :
            messagebox.showerror(title = "Username Exists", message = "Username already exists. Please choose another.")


# Function to make password visible :
def toggle_password_visibility():

    # If button clicked, then show password :
    if show_password_var.get() :
        
        entry_key1.config(show = "")
        entry_key2.config(show = "")
        entry_key3.config(show = "")

    # If buttin not clicked then hide the password.
    else :
        entry_key1.config(show = "*")
        entry_key2.config(show = "*")
        entry_key3.config(show = "*")


# Function to exit the application :
def done() :
    root.destroy()

# Function to handle main window where the user perfomrs desired operations.
def password_manager_window(username, K1, K2, K3) :

    # Configuring the window.
    password_manager_window = tk.Toplevel(root)
    password_manager_window.title(f"Password Manager - {username}")
    password_manager_window.geometry('500x300+480+250')

    # Add your visual styles and colors here.
    password_manager_window.configure(bg = 'gray20')

    # Function to handle ADD button click :
    def add() :

        # Configuring add data window :
        add_window = tk.Toplevel(password_manager_window)
        add_window.title("Add data")
        add_window.geometry('500x300+480+250')
        add_window.configure(bg = 'gray20')

        # Function to toggle password :
        def toggle_password_visibility_add() :

            # Toggles on the password :
            if show_password_var_add.get() :
                entry_password_add.config(show = "")

            # Toggles of the password :
            else :
                entry_password_add.config(show = "*")

        # Function to save data to file :
        def save_password() :

            # Username and password.
            user = entry_username_add.get()
            pwd = entry_password_add.get()

            if user and pwd :

                # Opening the data file to write to the file.
                with open(f"Data/{username}.txt", 'a') as file3 :
                   
                    # Encrypting the password before writing to file :
                    pwd = polybius.encrypt(pwd)
                    pwd = bifid.encrypt(pwd)
                    pwd = adfgvx.encrypt(pwd, K1)
                    pwd = fsqr.encrypt(pwd, K2, K3)

                    # Writing to file.
                    file3.write(f"{user} {pwd}\n")

                # Deleting the input data from inputbox.
                entry_username_add.delete(0, tk.END)
                entry_password_add.delete(0, tk.END)

                # Destroying the add data window.
                add_window.destroy()

        # Configuring labels for add window :
        label_username_add = tk.Label(add_window, text = "Username ", bg = 'gray20', fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
        label_password_add = tk.Label(add_window, text = "Password ", bg = 'gray20', fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
    
        # Configuring entrybox for add window :
        entry_username_add = tk.Entry(add_window, justify = 'center', bg = 'gray34', fg = 'aqua', font = ('consolas', 12, 'bold'))
        entry_password_add = tk.Entry(add_window, show = "*", justify = 'center', bg = 'gray34', fg = 'aqua', font = ('consolas', 12, 'bold'))

        show_password_var_add = tk.BooleanVar()
        show_password_checkbox_add = tk.Checkbutton(add_window, text="Show Password", variable=show_password_var_add, command=toggle_password_visibility_add, bg='gray20', fg='white', font=('Comic Sans MS', 10, 'bold'))

        # Configuring button for add window :
        button_save = tk.Button(add_window, text = "Save", command = save_password, bg = "gray34", fg = "lime", font = ('Comic Sans MS', 10, 'bold'))

        # Positioning the components of the add window :
        label_username_add.place(x = 80, y = 100)
        entry_username_add.place(x = 150, y = 100)
        label_password_add.place(x = 80, y = 150)
        entry_password_add.place(x = 150, y = 150)
        show_password_checkbox_add.place(x=250, y=200)
        button_save.place(x = 150, y = 200)

    # Function to handle DELETE button click :
    def delete() :
       
        # Configuring Delete Data Window :
        delete_window = tk.Toplevel(password_manager_window)
        delete_window.title(f"Delete Password - {username}")
        delete_window.geometry('500x300+480+250')
        delete_window.configure(bg = 'gray20')

        def delete_user() :
           
            # Username to be deleted.
            delU = entry_username2.get()
           
            # If file exists :
            if os.path.isfile(f"Data/{username}.txt") :

                # Open files to extract all data :
                with open(f"Data/{username}.txt", 'r') as D:
                    details = D.readlines()

                # If file is not empty :
                if len(details) != 0 :

                    # Traversing the data to delete the given username :
                    for line in details :
                        if line.split()[0] == delU :
                           
                            os.remove(f"Data/{username}.txt")
                           
                            with open(f"Data/{username}.txt", 'w') as update:
                                for detail in details:
                                    userName, passwd = map(str, detail.split())
               
                                    if userName != delU:
                                        update.write(f"{userName} {passwd}\n")
               
                            messagebox.showinfo("Delete Success", "Successfully deleted.")
   
                            break

                    # File doesn't contain given username :
                    else :
                        messagebox.showerror("No Match", "No such data exists")

                # File is empty :
                else :
                    messagebox.showinfo("Empty File", "File is already empty.")

            # FIle doesn't exist :
            else :
                messagebox.showwarning("NO DATA!!!", "No data added yet")

            # Destroying the delete window.
            delete_window.destroy()


        # Configuring the components of delete window :
        label_username2 = tk.Label(delete_window, text = "Username ", bg = 'gray20', fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
        entry_username2 = tk.Entry(delete_window, justify = 'center', bg = 'gray34', fg = 'aqua', font = ('consolas', 12, 'bold'))
        button_delete_user = tk.Button(delete_window, text = "Delete", command = delete_user, bg = "gray34", fg = "orangered2", font = ('Comic Sans MS', 10, 'bold'))

        # Positioning the components of delete window :
        label_username2.place(x = 80, y = 100)
        entry_username2.place(x = 150, y = 100)
        button_delete_user.place(x = 180, y = 150)

    # Function to handle VIEW button click :
    def view() :
       
        # If already file exists then open it :
        try:
           
            # Opening file to read the contents :
            with open(f"Data/{username}.txt", 'r') as v :
                contents = v.readlines()
           
            # Configuring view Data Window :
            view_window = tk.Toplevel(password_manager_window)
            view_window.title(f"View Passwords - {username}")
            view_window.geometry('500x300+480+250')
            view_window.configure(bg = 'gray20')

            # If file not empty :
            if len(contents) != 0 :
               
                # Looping through lines to display it :
                for line in contents:
                   
                    # Extracting line as list.
                    line = line.split()
                   
                    # Decrypting the password :
                    pawd = fsqr.decrypt(line[1].strip(), K2, K3)
                    pawd = adfgvx.decrypt(pawd, K1)
                    pawd = bifid.decrypt(pawd)
                    pawd = polybius.decrypt(pawd)
                   
                    # Configuring the label of view :
                    label = tk.Label(view_window, text = f"{line[0]} : {pawd}", bg = 'gray20', fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
                    label.pack(anchor = "w")
           
            # If file is empty :
            else :
               
                # Configuring the label of view :
                label = tk.Label(view_window, text = "File is empty.", bg = 'gray20', fg = 'firebrick1', font = ('Comic Sans MS', 10, 'bold'))
                label.pack(anchor = "w")

        # If file is not there
        except IOError :

            # Displaying a warning that no file exists.
            messagebox.showwarning(title = 'No file', message = "No data added yet.")

    # Function to handle GENERATE PASSWORD button click :
    def generate_password() :

        # Configuring Generate Password Window :
        generate_password_window = tk.Toplevel(password_manager_window)
        generate_password_window.title(f"Generate Password - {username}")
        generate_password_window.geometry('500x300+480+250')
        generate_password_window.configure(bg = 'gray20')


        # Function to generate password :
        def generate() :
            
            # Inputting length of password.
            length = entry_length_gen.get()

            if length != '' :
                
                length = int(length)

                # IF length entered and >= 8 :
                if length > 7 :
                    
                    # Generating a random password of given length.
                    random_password = random_pass.password(length)
                    
                    # Displaying the password :
                    entry_generated_password.delete(0, tk.END)
                    entry_generated_password.insert(0, random_password)
    
                    # Destroying Generate password window.
                    generate_password_window.destroy()
    
                # Length is not satisfied :
                else :
                    messagebox.showwarning(title = 'Length Not Satisfied', message = "Minimum length 8")
            
            # No length given :
            else :
                messagebox.showwarning(title = 'No Length given', message = "Minimum length 8")


        label_length_gen = tk.Label(generate_password_window, text = "Password Length ", bg = 'gray20', fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
        entry_length_gen = tk.Entry(generate_password_window, justify = 'center', bg = 'gray34', fg = 'aqua', font = ('consolas', 12, 'bold'))
        button_generate = tk.Button(generate_password_window, text = "Generate Password", command = generate, bg = "gray34", fg = "lime", font = ('Comic Sans MS', 10, 'bold'))

        label_length_gen.place(x = 80, y = 100)
        entry_length_gen.place(x = 200, y = 100)
        button_generate.place(x = 180, y = 150)


    # Function to handle LOGOUT button click :
    def logout() :

        # Maximizing the root window.
        root.state(newstate = 'normal')

        # Destroying the password manager window.
        password_manager_window.destroy()


    # Configuring buttons of the user operation page :
    button_add = tk.Button(password_manager_window, text = "Add", command = add, width = 21, bg = "gray34", fg = "aqua", font = ('Comic Sans MS', 10, 'bold'))
    button_delete = tk.Button(password_manager_window, text = "Delete", command = delete, width = 21, bg = "gray34", fg = "lightcoral", font = ('Comic Sans MS', 10, 'bold'))
    button_view = tk.Button(password_manager_window, text = "View", command = view, width = 21, bg = "gray34", fg = "lightseagreen", font = ('Comic Sans MS', 10, 'bold'))
    button_generate_password = tk.Button(password_manager_window, text = "Generate Password", command = generate_password, width = 21, bg = "gray34", fg = "violet", font = ('Comic Sans MS', 10, 'bold'))
    exit_button = tk.Button(password_manager_window, text = 'Logout', command = logout, width = 21, bg = "gray34", fg = 'firebrick1', font = ('Comic Sans MS', 10, 'bold'))
   
    # Displays the generated password.
    entry_generated_password = tk.Entry(password_manager_window, justify = 'center', width = 20, bg = 'gray34', fg = 'lime', font = ('consolas', 12, 'bold'))


    # Positioning components of operations :
    button_add.pack(side = 'top', padx = 15, pady = 9)
    button_delete.pack(side = 'top', padx = 15, pady = 9)
    button_view.pack(side = 'top', padx = 15, pady = 9)
    button_generate_password.pack(side = 'top', padx = 15, pady = 9)
    entry_generated_password.pack(side = 'top', padx = 15, pady = 9)
    exit_button.pack(side = 'top', padx = 15, pady = 9)


# Configuring root window :
root = tk.Tk()
root.title("Password Manager")
root.geometry('500x300+480+250')
root.configure(bg = 'gray20')

# Configuring Main window :
login_window = tk.Frame(root, bg = "gray20")
login_window.pack(pady = 50)

# Configuring labels of Main window :
label_username = tk.Label(login_window, text = "Username ", bg = "gray20", fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
label_key1 = tk.Label(login_window, text = "Key 1 ", bg = "gray20", fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
label_key2 = tk.Label(login_window, text = "Key 2 ", bg = "gray20", fg = 'white', font = ('Comic Sans MS', 10, 'bold'))
label_key3 = tk.Label(login_window, text = "Key 3 ", bg = "gray20", fg = 'white', font = ('Comic Sans MS', 10, 'bold'))

# Configuring entry boxes of Main window :
entry_username = tk.Entry(login_window, font=('consolas', 12, 'bold'), justify='center', bg='gray34', fg='aqua')
entry_key1 = tk.Entry(login_window, show="*", justify='center', font=('consolas', 12, 'bold'), bg='gray34', fg='aqua')
entry_key2 = tk.Entry(login_window, show="*", justify='center', font=('consolas', 12, 'bold'), bg='gray34', fg='aqua')
entry_key3 = tk.Entry(login_window, show="*", justify='center', font=('consolas', 12, 'bold'), bg='gray34', fg='aqua')


show_password_var = tk.BooleanVar()


# Configuring Buttons in Main window :
button_login = tk.Button(login_window, text = "Login", command = login, bg = "gray34", fg = "lime", font = ('Comic Sans MS', 12, 'bold'))
button_signup = tk.Button(login_window, text = "Signup", command = signup, bg = "gray34", fg = "aquamarine2", font = ('Comic Sans MS', 12, 'bold'))
button_exit = tk.Button(login_window, text = 'Exit', command = done, bg = 'gray34', fg = 'firebrick1', font = ('Comic Sans MS', 12, 'bold'))
show_password_checkbox = tk.Checkbutton(login_window, text = "Show Password", variable = show_password_var, command = toggle_password_visibility, bg = 'gray20', fg = 'white', font = ('Comic Sans MS', 10, 'bold'))


# Positioning components of Main window :
label_username.grid(row = 0, column = 0)
entry_username.grid(row = 0, column = 2)
label_key1.grid(row = 2, column = 0)
entry_key1.grid(row = 2, column = 2)
label_key2.grid(row = 4, column = 0)
entry_key2.grid(row = 4, column = 2)
label_key3.grid(row = 6, column = 0)
entry_key3.grid(row = 6, column = 2)
button_login.grid(row = 15, column = 0, pady = 15)
button_signup.grid(row = 15, column = 2)
button_exit.grid(row = 15, column = 4)
show_password_checkbox.grid(row = 8, column = 0, columnspan = 3)

# Storing inputs of signup/login window :
entry_length = tk.Entry(root)
entry_generated_password = tk.Entry(root)

# Running the mainloop.
root.mainloop()


