import shutil
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk

main_window = tk.Tk(className="")
main_window.title('Open Source File Replacer')
main_window.resizable(False, False)
width = 700
height = 250
main_window.geometry(F'{width}x{height}')

# Common configuration
# Photoimage object for both source and destination
photoimage = tk.PhotoImage(file=r"data\icons\Folder-document-open-icon.png").subsample(5, 5)
lock_image = tk.PhotoImage(file=r"data\icons\lock.png").subsample(25, 25)
unlock_image = tk.PhotoImage(file=r"data\icons\unlock.png").subsample(10, 10)
top_button_row = 2
bottom_button_row = 4
text_row = 3
source_selected = tk.BooleanVar(main_window, value=False)
destination_selected = tk.BooleanVar(main_window, value=False)
SupportFileTypes = (
    ('All files', '*.*'),
    # ('text files', '*.txt')
)


def open_source_file():
    file_folder_option_selected = file_folder_variable.get()
    if file_folder_option_selected == file_folder_options[1]:  # file
        source_path_selected = fd.askopenfile(filetypes=SupportFileTypes)
        if source_text.get(index1=0.0) != "\n":
            source_text.delete(index1=0.0, index2=float(len(source_path_selected.name)))
        source_text.insert(0.0, source_path_selected.name)
    elif file_folder_option_selected == file_folder_options[2]:  # folder
        source_path_selected = fd.askdirectory()
        if source_text.get(index1=0.0) != "\n":
            source_text.delete(index1=0.0, index2=float(len(source_path_selected)))
        source_text.insert(0.0, source_path_selected)
    source_selected.set(value=True)
    if source_selected.get() and destination_selected.get():
        replace_button.config(state='enabled')


def open_destination_file():
    file_folder_option_selected = file_folder_variable.get()
    replace_option_selected = replace_variable.get()
    if file_folder_option_selected == file_folder_options[1] and replace_option_selected == replace_config_options[1]:
        # Simple copy/replace file in destination
        dst_path_selected = fd.askdirectory()
        if destination_text.get(index1=0.0) != "\n":
            destination_text.delete(index1=0.0, index2=float(len(dst_path_selected)))
        destination_text.insert(0.0, dst_path_selected)
        destination_selected.set(value=True)
    elif file_folder_option_selected == file_folder_options[1] and replace_option_selected != replace_config_options[1]:
        # Replace specific file
        dst_path_selected = fd.askopenfile(filetypes=SupportFileTypes)
        if destination_text.get(index1=0.0) != "\n":
            destination_text.delete(index1=0.0, index2=float(len(dst_path_selected.name)))
        destination_text.insert(0.0, dst_path_selected.name)
        destination_selected.set(value=True)
    elif file_folder_option_selected == file_folder_options[2]:  # folder
        dst_path_selected = fd.askdirectory()
        if destination_text.get(index1=0.0) != "\n":
            destination_text.delete(index1=0.0, index2=float(len(dst_path_selected)))
        destination_text.insert(0.0, dst_path_selected)
        destination_selected.set(value=True)
    if source_selected.get() and destination_selected.get():
        replace_button.config(state='enabled')


def simple_replace(source, destination):
    try:
        shutil.copy(src=source, dst=destination)
        messagebox.showinfo(title="Successful Replacement",
                            message=f"Successfully replaced the {destination} with {source}")
    except Exception as e:
        print(e)


def check_same_src_dst(source, destination):
    if source == destination:
        messagebox.showinfo(title="No replace required", message="Source and destination files are same")
        return True
    return False


def replace_function():
    """ Executes the replacement based on the configuration selected"""
    source_path = source_text.get('1.0', 'end-1c')
    destination_path = destination_text.get('1.0', 'end-1c')
    config_selected = replace_variable.get()
    file_folder_config_selected = file_folder_variable.get()
    if file_folder_config_selected == file_folder_options[1]:  # 'File'
        if config_selected == replace_config_options[1]:  # 'Simple Copy/Replace in destination location'
            """ File copy and simple replace scenario"""
            source = source_path
            source_file_name = str(source_path).split('/')[-1]
            destination = "/".join([destination_path, source_file_name])
            if check_same_src_dst(source=source, destination=destination):
                pass
            else:
                import os
                if os.path.isfile(destination):
                    simple_replace(source=source, destination=destination)
                else:
                    try:
                        shutil.copy(src=source, dst=destination)
                        messagebox.showinfo(title="Successful Copy",
                                            message=f"Successfully copied the {source} to {destination}")
                    except Exception as e:
                        print(e)
        elif config_selected == replace_config_options[2]:  # 'Regular Replace'
            """ Simple replace scenario with file present"""
            source = source_path
            destination = destination_path
            if check_same_src_dst(source=source, destination=destination):
                pass
            else:
                simple_replace(source=source, destination=destination)
        elif config_selected == replace_config_options[3]:  # 'Git Replace'
            """ Git replace scenario with file present"""
            source = source_path
            destination = destination_path
            if check_same_src_dst(source=source, destination=destination):
                pass
            else:
                pass
                # ToDo
    elif file_folder_config_selected == file_folder_options[2]:  # 'Folder'
        if config_selected == replace_config_options[1]:  # 'Simple Copy/Replace in destination location'
            """ Folder copy and simple replace scenario"""
            source = source_path
            destination = destination_path
            print(f"source:{source}\ndestination:{destination}")
            if check_same_src_dst(source=source, destination=destination):
                pass
            else:
                import os
                for dir, _, file in os.walk(source):
                    pass  # ToDo
                exit(-200)
        elif config_selected == replace_config_options[2]:  # 'Regular Replace'
            pass  # ToDo
        pass


def lock_unlock_configuration():
    if file_folder_config_lock_unlock_status.get() == 'unlocked':
        file_folder_config_option_menu.config(state='disabled')
        replace_config_option_menu.config(state='disabled')
        config_selected = replace_variable.get()
        file_folder_config_selected = file_folder_variable.get()
        if file_folder_config_selected == file_folder_options[1] and config_selected == replace_config_options[1]:  #
            # file and Regular replace
            source_button['text'] = f"Source {file_folder_config_selected}"
            destination_button['text'] = f"Destination folder"
        else:
            source_button['text'] = f"Source {file_folder_config_selected}"
            destination_button['text'] = f"Destination {file_folder_config_selected}"
        source_button.config(state='enabled')
        destination_button.config(state='enabled')
        file_folder_config_lock_unlock_status.set('locked')  # Required for the next iteration
        print("Locked the configuration")

    elif file_folder_config_lock_unlock_status.get() == 'locked':
        file_folder_config_option_menu.config(state='enabled')
        replace_config_option_menu.config(state='enabled')
        source_button.config(state='disabled')
        destination_button.config(state='disabled')
        replace_button.config(state='disabled')
        file_folder_config_lock_unlock_status.set('unlocked')  # Required for the next iteration
        print("Unlocked the configuration")


total_columns = 5
total_rows = 5
tk.Grid.rowconfigure(main_window, index=0, weight=1)
tk.Grid.rowconfigure(main_window, index=1, weight=1)
tk.Grid.rowconfigure(main_window, index=2, weight=1)
tk.Grid.columnconfigure(main_window, index=0, weight=1, uniform=True)
tk.Grid.columnconfigure(main_window, index=1, weight=1)
tk.Grid.columnconfigure(main_window, index=2, weight=1)

# Drop down configurations
""" File Folder configurations drop down """
file_folder_variable = tk.StringVar(main_window)
file_folder_label = ttk.Label(main_window, text="File or Folder option: ",
                              font=("Times New Roman", 10)).grid(row=0, column=0)
file_folder_options = ('', 'file', 'folder')
file_folder_variable.set(file_folder_options[1])
file_folder_config_option_menu = ttk.OptionMenu(main_window, file_folder_variable, *file_folder_options)
file_folder_config_option_menu.grid(row=1, column=0, sticky='nsew')
file_folder_config_option_menu.config(state="enabled")

file_folder_config_lock_unlock_status = tk.StringVar(main_window)
file_folder_config_lock_unlock_status.set("unlocked")

""" Replacement configuration Drop Down """
replace_variable = tk.StringVar(main_window)
replace_config_label = ttk.Label(main_window, text="Select the configuration: ",
                                 font=("Times New Roman", 10)).grid(row=0, column=1)
replace_config_options = ('', 'Simple Copy/Replace', 'Regular Replace', 'Git Replace')
replace_variable.set(replace_config_options[1])
replace_config_option_menu = ttk.OptionMenu(main_window, replace_variable, *replace_config_options)
replace_config_option_menu.grid(row=1, column=1, sticky='nsew')
replace_config_option_menu.config(state='enabled')

# Configuring the text boxes
source_text = tk.Text(main_window, height=1, width=30, padx=1, pady=1)
source_text.grid(column=0, row=text_row)

destination_text = tk.Text(main_window, height=1, width=30, padx=1, pady=1)
destination_text.grid(column=2, row=text_row)

""" Configuring Buttons """
# Lock/Unlock configuration
lock_unlock_config_button = ttk.Button(main_window, text=f'Lock/Unlock\nfile or folder config',
                                       command=lock_unlock_configuration)
lock_unlock_config_button.grid(column=2, row=0, sticky='w', ipadx=5, ipady=2, padx=10, pady=10)

# # Source Button
source_button = ttk.Button(main_window, text=f'Source {file_folder_variable.get()}', command=open_source_file,
                           image=photoimage, compound='left')
source_button.grid(column=0, row=top_button_row, sticky='e', ipadx=2, ipady=2, padx=0, pady=0)
source_button.config(state='disabled')

# Destination Button
destination_button = ttk.Button(main_window, text=f'Destination {file_folder_variable.get()}',
                                command=open_destination_file,
                                image=photoimage, compound='right')
destination_button.grid(column=2, row=top_button_row, sticky='w', ipadx=5, ipady=2, padx=10, pady=10)
destination_button.config(state='disabled')

# Replace Button
replace_button = ttk.Button(main_window, text='Replace', command=replace_function)
replace_button.grid(column=2, row=bottom_button_row, ipadx=5, ipady=5, padx=10, pady=10, sticky='s')
replace_button.config(state='disabled')

main_window.mainloop()
