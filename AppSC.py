import os
import subprocess
import tkinter as tk

apps = []

def add_app():
    app_name = app_name_entry.get()
    app_path = app_path_entry.get()
    apps.append((app_name, app_path))
    app_list.insert(tk.END, app_name)
    app_name_entry.delete(0, tk.END)
    app_path_entry.delete(0, tk.END)

def run_apps():
    selected_apps = app_list.curselection()
    for index in selected_apps:
        subprocess.Popen([apps[index][1]])

root = tk.Tk()
root.title("Open Apps")

frame = tk.Frame(root)
frame.pack()

app_name_label = tk.Label(frame, text="App Name:")
app_name_label.grid(row=0, column=0)
app_name_entry = tk.Entry(frame)
app_name_entry.grid(row=0, column=1)

app_path_label = tk.Label(frame, text="App Path:")
app_path_label.grid(row=1, column=0)
app_path_entry = tk.Entry(frame)
app_path_entry.grid(row=1, column=1)

add_app_button = tk.Button(frame, text="Add App", command=add_app)
add_app_button.grid(row=2, column=0, columnspan=2)

app_list = tk.Listbox(frame, selectmode=tk.MULTIPLE)
app_list.grid(row=3, column=0, columnspan=2)

run_apps_button = tk.Button(frame, text="Run Apps", command=run_apps)
run_apps_button.grid(row=4, column=0, columnspan=2)

root.mainloop()