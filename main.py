import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

main_window = tk.Tk(className="")
main_window.title('Open Source File Replacer')
main_window.resizable(True, True)
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
    file_selected = fd.askopenfile(filetypes=SupportFileTypes)
    source_text.insert(1.0, file_selected.name)
    source_selected.set(value=True)
    if source_selected.get() and destination_selected.get():
        replace_button.config(state='enabled')
    else:
        pass


def open_destination_file():
    file_selected = fd.askopenfile(filetypes=SupportFileTypes)
    destination_text.insert(1.0, file_selected.name)
    destination_selected.set(value=True)
    if source_selected.get() and destination_selected.get():
        replace_button.config(state='enabled')
    else:
        pass


def replace_function():
    if config_variable.get() == 'Simple Replace':
        print(f"Source = {source_text.get('1.0', 'end-1c')}, Destination = {destination_text.get('1.0', 'end-1c')}")
        # shutil.copy(src=source_text.get("1.0","end-1c"),dst=destination_text.get("1.0","end-1c"))
    elif config_variable.get() == 'Git Replace':
        print(f"**Config chosen = {config_variable.get()}")
    else:
        pass
    pass


def lock_unlock_configuration():
    if file_folder_config_lock_unlock_status.get() == 'unlocked':
        file_folder_config_chosen.config(state='disabled')
        source_button['text'] = f"Source {file_folder_option.get()}"
        source_button.config(state='enabled')
        destination_button['text'] = f"Destination {file_folder_option.get()}"
        destination_button.config(state='enabled')
        config_chosen.config(state='enabled')
        file_folder_config_lock_unlock_status.set('locked')
        print("Locked the configuration")
    elif file_folder_config_lock_unlock_status.get() == 'locked':
        file_folder_config_chosen.config(state='enabled')
        config_chosen.config(state='disabled')
        file_folder_config_lock_unlock_status.set('unlocked')
        source_button.config(state='disabled')
        destination_button.config(state='disabled')
        replace_button.config(state='disabled')
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
file_folder_option = tk.StringVar(main_window)
file_folder_label = ttk.Label(main_window, text="File or Folder option: ",
                              font=("Times New Roman", 10)).grid(row=0, column=1)
file_folder_options = ('', 'file', 'folder')
file_folder_option.set(file_folder_options[1])
file_folder_config_chosen = ttk.OptionMenu(main_window, file_folder_option, *file_folder_options)
file_folder_config_chosen.grid(row=1, column=1, sticky='nsew')
file_folder_config_lock_unlock_status = tk.StringVar(main_window)
file_folder_config_lock_unlock_status.set("unlocked")

""" Replacement configuration Drop Down """
config_variable = tk.StringVar(main_window)
configuration_label = ttk.Label(main_window, text="Select the configuration: ",
                                font=("Times New Roman", 10)).grid(row=top_button_row, column=1)
config_options = ('', 'Simple Replace', 'Git Replace')
config_variable.set(config_options[1])
config_chosen = ttk.OptionMenu(main_window, config_variable, *config_options)
config_chosen.grid(row=text_row, column=1, sticky='nsew')
config_chosen.config(state='disabled')

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
source_button = ttk.Button(main_window, text=f'Source {file_folder_option.get()}', command=open_source_file,
                           image=photoimage, compound='left')
source_button.grid(column=0, row=top_button_row, sticky='e', ipadx=2, ipady=2, padx=0, pady=0)
source_button.config(state='disabled')

# Destination Button
destination_button = ttk.Button(main_window, text=f'Destination {file_folder_option.get()}',
                                command=open_destination_file,
                                image=photoimage, compound='right')
destination_button.grid(column=2, row=top_button_row, sticky='w', ipadx=5, ipady=2, padx=10, pady=10)
destination_button.config(state='disabled')

# Replace Button
replace_button = ttk.Button(main_window, text='Replace', command=replace_function)
replace_button.grid(column=1, row=bottom_button_row, ipadx=5, ipady=5, padx=10, pady=10, sticky='s')
replace_button.config(state='disabled')

main_window.mainloop()
