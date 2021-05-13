import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog as fd

main_window = tk.Tk(className="")
main_window.title('Open Source File Replacer')
main_window.resizable(True, True)
main_window.geometry('700x250')

# Common configuration
# Photoimage object for both source and destination
photoimage = tk.PhotoImage(file=r"data\icons\Folder-document-open-icon.png").subsample(5, 5)
top_button_row = 2
bottom_button_row = 4
text_row = 3

SupportFileTypes = (
        ('All files', '*.*'),
        # ('text files', '*.txt')
    )

"""
# Text editor
text = tk.Text(main_window, height=12)
text.grid(column=0, row=0, sticky='nsew')

def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())
    
"""


def open_source_file():
    file_selected = fd.askopenfile(filetypes=SupportFileTypes)
    source_text.insert(1.0,file_selected.name)

def open_destination_file():
    file_selected = fd.askopenfile(filetypes=SupportFileTypes)
    destination_text.insert(1.0, file_selected.name)

def replace_function():
    print("Clicked on replace function")
    pass

tk.Grid.rowconfigure(main_window, index=0, weight=1)
tk.Grid.rowconfigure(main_window, index=1, weight=1)
tk.Grid.rowconfigure(main_window, index=2, weight=1)
tk.Grid.columnconfigure(main_window, index=0, weight=1)
tk.Grid.columnconfigure(main_window, index=1, weight=1)
tk.Grid.columnconfigure(main_window, index=2, weight=1)

# Configuration Drop Down
file_folder_option = tk.StringVar(main_window)
file_folder_label = ttk.Label(main_window, text = "File or Folder option: ",
                                font=("Times New Roman", 10)).grid(row=0, column=1)
config_options = ('','file', 'All files in the folder')
file_folder_option.set(config_options[1])
config_chosen = ttk.OptionMenu(main_window, file_folder_option, *config_options)
config_chosen.grid(row=1,column=1, sticky='nsew')


# Configuring the text boxes
source_text = tk.Text(main_window, height=1, width=30, padx=1, pady=1)
source_text.grid(column=0, row=text_row)

destination_text = tk.Text(main_window, height=1, width=30, padx=1, pady=1)
destination_text.grid(column=2, row=text_row)

""" Configuring Buttons """
# # Source Button
source_button = ttk.Button(main_window, text=f'Source ', command=open_source_file,
                           image=photoimage, compound='left')
source_button.grid(column=0, row=top_button_row, sticky='e', ipadx=2, ipady=2, padx=0, pady=0)

# config_button = ttk.Button(main_window, text='Set Configuration', command=open_source_file)
# config_button.grid(column=1, row=0, ipadx=5, ipady=2, padx=10, pady=10)

# Configuration Drop Down
config_variable = tk.StringVar(main_window)
configuration_label = ttk.Label(main_window, text = "Select the configuration: ",
                                font=("Times New Roman", 10)).grid(row=top_button_row, column=1)
config_options = ('','Simple Replace', 'Git Replace')
config_variable.set(config_options[1])
config_chosen = ttk.OptionMenu(main_window, config_variable, *config_options)
config_chosen.grid(row=text_row,column=1, sticky='nsew')

# Destination Button
destination_button = ttk.Button(main_window, text=f'Destination ',
                                command=open_destination_file,
                                image=photoimage, compound='right')
destination_button.grid(column=2, row=top_button_row, sticky='w', ipadx=5, ipady=2, padx=10, pady=10)



# Replace Button
replace_button = ttk.Button(main_window, text='Replace', command=replace_function)
replace_button.grid(column=1, row=bottom_button_row, ipadx=5, ipady=5, padx=10, pady=10, sticky='s' )


def change_dropdown(*args):
    print( config_variable.get() )

# link function to change dropdown
config_variable.trace('w', change_dropdown)
main_window.mainloop()
