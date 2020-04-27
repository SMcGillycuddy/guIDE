'''
guIDE is a lightweight text editor / IDE.

Functionality: 
File -> New, Open, Save, Save As..., Exit
Edit -> Cut, Copy, Paste, Undo, Redo
View -> Show Line Numbers, Show Cursor Location, Highlight Current Line, Themes
About -> About, Help
Shortcut Icons, Scroll Bar, Line Numbers

@Seadna McGillycuddy
'''

#importing tkinter
from tkinter import *
#import the filedialog module
import tkinter.filedialog
#import the OS module
import os

#creating a global variable to store the name of the currently opened file
file_name = None

#giving the window a title
PROGRAM_NAME = "guIDE"
#creating a root window
root = Tk()
#giving the window a size
root.geometry('350x350')
#adding the title to the window
root.title(PROGRAM_NAME)
#adding an icon to the window
root.iconphoto(False, PhotoImage(file='icons/guIDE_logo_30.png'))

#defining the open file function
def open_file(event=None):
	#ask the user which file to open
	input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if input_file_name:
		global file_name
		file_name = input_file_name
		#adding the filename to the root window
		root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
		#delete the contents of the text widget
		content_text.delet(1.0, END)
		#open the file in read mode and insert its content into the text widget
		with open(file_name) as _file:
			content_text.insert(1.0, _file.read())

#defining the save function
def save(event=None):
	global file_name
	#checking to see if there is a file open
	if not file_name:
		#if no file is open, call the save_as function
		save_as()
	else:
		#or else call the write_to_file function
		write_to_file(file_name)
	return "break"

#defining the save_as function
def save_as(event=None):
	#open the dialog so the user can input a filename
	input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if input_file_name:
		global file_name
		file_name = input_file_name
		#call the write_to_file function
		write_to_file(file_name)
		#adding the filename to the root window
		root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
	return "break"

#defining the write_to_file function
def write_to_file(file_name):
	try:
		content = content_text.get(1.0, 'end')
		with open(file_name, 'w') as the_file:
			the_file.write(content)
	except IOError:
		pass

#defining the new_file function
def new_file(event=None):
	#change the root window's title to 'Untitled'
	root.title("Untitled")
	global file_name
	file_name = None
	#delete the content of the text widget
	content_text.delete(1.0, END)


#defining the Cut, Copy, Paste, Undo, Redo functions
def cut():
	content_text.event_generate("<<Cut>>")

def copy():
	content_text.event_generate("<<Copy>>")

def paste():
	content_text.event_generate("<<Paste>>")

def undo():
	content_text.event_generate("<<Undo>>")

def redo(event=None):
	content_text.event_generate("<<Redo>>")
	return 'break'

#defining the select all function
def select_all(event=None):
	content_text.tag_add('sel', '1.0', 'end')
	return "break"

#defining the find text function
def find_text(event=None):
	#creating a new top level window  specifying its geometry
	search_toplevel = Toplevel(root)
	#giving it a title
	search_toplevel.title("Find Text")
	#making it a transient window
	search_toplevel.transient(root)
	#making it non-resizable
	search_toplevel.resizable(False, False)
	Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
	search_entry_widget = Entry(search_toplevel, width=25)
	search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
	search_entry_widget.focus_set()
	#creating a variable to store the state of the Ignore Case option 
	ignore_case_value = IntVar()
	Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)
	Button(search_toplevel, text="Find All", underline=0, command=lambda: search_output(search_entry_widget.get(), ignore_case_value.get(), content_text, search_toplevel, search_entry_widget)).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

#defining the close search window function
def close_search_window():
	content_text.tag_remove('match', '1,0', END)
	search_toplevel.destroy()
	search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
	return 'break'

#defining the search output function
def search_output(needle, if_ignore_case, content_text,
                  search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


#specifing the icons for the menu
new_file_icon = PhotoImage(file='icons/new_file.png')
open_file_icon = PhotoImage(file='icons/open_file.png')
save_file_icon = PhotoImage(file='icons/save.png')
cut_icon = PhotoImage(file='icons/cut.png')
copy_icon = PhotoImage(file='icons/copy.png')
paste_icon = PhotoImage(file='icons/paste.png')
undo_icon = PhotoImage(file='icons/undo.png')
redo_icon = PhotoImage(file='icons/redo.png')

#adding a menu bar
menu_bar = Menu(root)

#adding and populating a file menu in the menu bar
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0, command=new_file)
file_menu.add_command(label="Open", accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0, command=open_file)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0, command=save)
file_menu.add_separator()#add a separator
file_menu.add_command(label="Save as...", accelerator='Shift+Ctrl+S', command=save_as)
file_menu.add_command(label="Exit", accelerator='Alt+F4')
menu_bar.add_cascade(label='File', menu=file_menu)

#adding and populating an edit menu in the menu bar
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', image=undo_icon, command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon, command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon, command=paste)
edit_menu.add_separator()#add a separator
edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F', command=find_text)
edit_menu.add_separator()#add a separator
edit_menu.add_command(label='Select All', underline=7, accelerator='Ctrl+A', command=select_all)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

#adding a view menu in the menu bar
view_menu = Menu(menu_bar, tearoff=0)
#create a Integer variable to store the state of show line number
show_line_no = IntVar()
#setting the show_line_no variable to '1'
show_line_no.set(1)
#adding a checkbutton that allows the user to toggle the show line number function 
view_menu.add_checkbutton(label="Show Line Numbers", variable=show_line_no)
#acreating a variable that stores the state of show_cursor_info
show_cursor_info = IntVar()
#set the value of the show_cursor_info to '1'
show_cursor_info.set(1)
#adding a checkbutton to toggle showing the cursor location on/off
view_menu.add_checkbutton(label='Show Cursor Location at Bottom', variable=show_cursor_info)
#creating a variable to store the state of the highlight current line option
highlight_line = IntVar()
#adding a checkbutton to toggle highlighting the current line on/off
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1, offvalue=0, variable=highlight_line)

#creating a themes cascade menu inside the view menu
themes_menu = Menu(menu_bar, tearoff=0)
#adding a themes menu inside the view menu
view_menu.add_cascade(label="Themes", menu=themes_menu)

#setting the available colour schemes
color_schemes = {
	'Default': '#000000.#FFFFFF',
	'Grey': '#83406A.#D1D4D1',
	'Aqua': '#5B8340.#D1E7E0',
	'Beige': '#4B4620.#FFF0E1',
	'Cobalt': '#ffffBB.#3333aa',
	'Olive': '#D1E7E0.#5B8340',
	'Night Mode': '#FFFFFF.#000000',
}

#creating a variable that stores the selected theme
theme_choice = StringVar()
#setting the theme to default
theme_choice.set('Default')
#for loop that populates the themes menu with the various colour schemes
for k in sorted(color_schemes):
	#adding a radio button that allows user to select the colour scheme
	themes_menu.add_radiobutton(label=k, variable=theme_choice)
#adding the above widgets to the view menu
menu_bar.add_cascade(label='View', menu=view_menu)

#adding and populating an about menu in the menu bar
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About')
about_menu.add_command(label='Help')
menu_bar.add_cascade(label='About',  menu=about_menu)

#displaying the menu
root.config(menu=menu_bar)


#adding a frame for the horizontal shortcut icon bar with styling
shortcut_bar = Frame(root, height=25, background='#f0f0f0')
#display the shortcut icon bar
shortcut_bar.pack(expand='no', fill='x')

#adding a frame for the vertical line number bar with styling
line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0, background='#bfbfbf', state='disabled', wrap='none')
#display the line number bar
line_number_bar.pack(side='left', fill='y')

#adding the main content Text widget and Scrollbar widget
content_text = Text(root, wrap='word', undo=1)
#display the main content Text widget
content_text.pack(expand='yes', fill='both')
#adding a scroll bar widget to the main text content widget
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
#display the scroll bar
scroll_bar.pack(side='right', fill='y')

#adding key bindings for the operations
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)


#execute the mainloop() function
root.mainloop()