import os
from tkinter import *
import subprocess
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import pickle


def add_app():
    app_name = app_name_entry.get()
    app_path = app_path_entry.get()
    apps.append((app_name, app_path))
    app_list.insert(END, app_name)
    app_name_entry.delete(0, END)
    app_path_entry.delete(0, END)

def run_apps():
    selected_apps = app_list.curselection()
    for index in selected_apps:
        subprocess.Popen([apps[index][1]])

def save_apps():
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])

    if file_path:
        with open(file_path, "wb") as f:pickle.dump(apps, f)

def load_apps():
    file_path = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pkl")])
    if file_path:
        with open(file_path, "rb") as f:
            global apps
            apps = pickle.load(f)
            app_list.delete(0, tk.END)
            for app in apps:
                app_list.insert(tk.END, app[0])

def run_scripts():
    selected_scripts = script_list.curselection()
    for index in selected_scripts:
        with open(scripts[index][1], "rb") as f:
            apps = pickle.load(f)
            for app in apps:
                subprocess.Popen([app[1]])

def add_script():
    script_name = script_name_entry.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])

    if file_path:
        with open(file_path, "wb") as f:
            pickle.dump(apps, f)
        scripts.append((script_name, file_path))
        script_list.insert(tk.END, script_name)
        script_name_entry.delete(0, tk.END)

apps = []
scripts = []

root = Tk()
root.title("Apps Scenarios")

apps_frame = Frame(root)
apps_frame.pack(side=LEFT, padx=10, pady=10)

app_name_label = Label(apps_frame, text="App Name:")
app_name_label.grid(row=0, column=0)
app_name_entry = Entry(apps_frame)
app_name_entry.grid(row=0, column=1)
app_path_label = Label(apps_frame, text="App Path:")
app_path_label.grid(row=1, column=0)
app_path_entry = Entry(apps_frame)
app_path_entry.grid(row=1, column=1)

app_list = Listbox(apps_frame)
app_list.grid(row=2, column=0, columnspan=2, sticky="nsew")

add_app_button = Button(apps_frame, text="Add App", command=add_app)
add_app_button.grid(row=3, column=0, pady=5)

run_apps_button = Button(apps_frame, text="Run Apps", command=run_apps)
run_apps_button.grid(row=3, column=1, pady=5)

save_apps_button = Button(apps_frame, text="Save Apps", command=save_apps)
save_apps_button.grid(row=4, column=0, pady=5)

load_apps_button = Button(apps_frame, text="Load Apps", command=load_apps)
load_apps_button.grid(row=4, column=1, pady=5)

scripts_frame = Frame(root)
scripts_frame.pack(side=RIGHT, padx=10, pady=10)

script_name_label = Label(scripts_frame, text="Script Name:")
script_name_label.grid(row=0, column=0)
script_name_entry = Entry(scripts_frame)
script_name_entry.grid(row=0, column=1)

script_list = Listbox(scripts_frame)
script_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

add_script_button = Button(scripts_frame, text="Add Script", command=add_script)
add_script_button.grid(row=2, column=0, pady=5)

run_scripts_button = Button(scripts_frame, text="Run Scripts", command=run_scripts)
run_scripts_button.grid(row=2, column=1, pady=5)

root.mainloop()
