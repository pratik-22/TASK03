import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            result_label.config(text="Password length should be a positive integer.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        generated_password.set(password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid length (a positive integer).")

def reset_fields():
    entry_name.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    generated_password.set("")

root = tk.Tk()
root.title("Password Generator")

label_name = tk.Label(root, text="Enter name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_length = tk.Label(root, text="Enter password length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="Generated Password:")
result_label.pack()

generated_password = tk.StringVar()
generated_password.set("")
password_display = tk.Label(root, textvariable=generated_password, relief=tk.SOLID, borderwidth=1)
password_display.pack()

accept_button = tk.Button(root, text="Accept", command=lambda: print(f"Name: {entry_name.get()}, Password: {generated_password.get()}"))
accept_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack()

root.mainloop()
