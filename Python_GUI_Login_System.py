import tkinter as tk
from tkinter import messagebox, END
import os.path

class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("Login System")


        self.label_username = tk.Label(master, text="Username : ")
        self.label_password = tk.Label(master, text="Password :")
        self.entry_username = tk.Entry(master,background="white",foreground="black")
        self.entry_password = tk.Entry(master, background="white",show="*",foreground="black")

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()

        self.entry_password.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(master, text="Sign Up", command=self.register)
        self.register_button.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as f:
                users = f.readlines()
                for user in users:
                    user = user.strip().split(',')
                    if username == user[0] and password == user[1]:
                        messagebox.showinfo("Login successful", "signed in as " f"{username}",icon="info")
                        self.entry_username.delete(0,END)
                        self.entry_password.delete(0,END)
                        return
                messagebox.showerror("Incorrect Login", "Username or password is incorrect.",icon="error")
                self.entry_username.delete(0, END)
                self.entry_password.delete(0, END)
        else:
            messagebox.showerror("Error", "User not found.",icon="warning")
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)

    def register(self):
        top = tk.Toplevel(self.master)
        top.title("Sign Up")

        label_username = tk.Label(top, text="Username : ")
        label_password = tk.Label(top, text="Password : ")

        entry_username = tk.Entry(top,background="white",foreground="black")
        entry_password = tk.Entry(top, show="*",background="white",foreground="black")

        label_username.pack()
        entry_username.pack()
        label_password.pack()
        entry_password.pack()

        def save_user():
            username = entry_username.get()
            password = entry_password.get()
            with open('users.txt', 'a') as f:
                f.write(f"{username},{password}\n")
            messagebox.showinfo("Successful", "Registration created successfully.",icon="info")
            top.destroy()

        register_button = tk.Button(top, text="Sign up", command=save_user)
        register_button.pack()


root = tk.Tk()
app = LoginScreen(root)
root.mainloop()
