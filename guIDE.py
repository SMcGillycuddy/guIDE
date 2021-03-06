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

#import the OS module
import os
#importing tkinter
from tkinter import *
#import the filedialog module
import tkinter.filedialog
#importing the messagebox module
import tkinter.messagebox

#giving the window a title
PROGRAM_NAME = "guIDE"
#creating a global variable to store the name of the currently opened file
file_name = None

#creating a root window
root = Tk()
#giving the window a size
root.geometry('700x700')
#adding the title to the window
root.title(PROGRAM_NAME)
#adding an icon to the window
root.iconphoto(False, PhotoImage(file='icons/guIDE_logo_30.png'))

#defining the function that updates the line number
def update_line_numbers(event=None):
	line_numbers = get_line_numbers()
	line_number_bar.config(state='normal')
	line_number_bar.delete('1.0','end')
	line_number_bar.insert('1.0', line_numbers)
	line_number_bar.config(state='disabled')

#defining the function that highlights lines
def highlight_line(interval=100):
	content_text.tag_remove("active_line", 1.0, "end")
	content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
	content_text.after(interval, toggle_highlight)

#defining the function that undos the higlight line
def undo_highlight():
	content_text.tag_remove("active_line", 1.0, "end")

#defining the function that toggles wether line highlighting is on or off
def toggle_highlight(event=None):
	if to_highlight_line.get():
		highlight_line()
	else:
		undo_highlight()

#defining the function that shows the position of the cursor
def show_cursor_info_bar():
	show_cursor_info_checked = show_cursor_info.get()
	if show_cursor_info_checked:
		cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
	else:
		cursor_info_bar.pack_forget()

#defining the function that updates the cursor bar
def update_cursor_info_bar(Event=None):
	row, col = content_text.index(INSERT).split('.')
	line_num, col_num = str(int(row)), str(int(col)+1)
	infotext = "Line: {0} | Column {1}".format(line_num, col_num)
	cursor_info_bar.config(text=infotext)

#defining the function that executes when the content has been changed 
def on_content_changed(event=None):
	update_line_numbers()
	update_cursor_info_bar()

#defining the function that gets the line number
def get_line_numbers():
	output = ''
	if show_line_number.get():
		row, col = content_text.index("end").split('.')
		for i in range(1, int(row)):
			output += str(i) + '\n'
	return output

#defining the function that displays an about message
def display_about_messagebox(event=None):
	tkinter.messagebox.showinfo("About", "{}-{}".format(PROGRAM_NAME, "\nguIDE\n Copyright S. McGillycuddy 2020"))

#defining the function that displays a help message
def display_help_messagebox(event=None):
	tkinter.messagebox.showinfo("Help", "--TO DO---\n Help text goes here", icon='question')

#defining the function that terminates the program
def exit_editor(event=None):
	if tkinter.messagebox.askokcancel("Quit?", "Really Quit?"):
		root.destroy()

#defining the new_file function
def new_file(event=None):
	#change the root window's title to 'Untitled'
	root.title("Untitled")
	global file_name
	file_name = None
	#delete the content of the text widget
	content_text.delete(1.0, END)
	#call the on_content_changed function
	on_content_changed()

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
	#call the on_content_changed function
	on_content_changed()

#defining the write_to_file function
def write_to_file(file_name):
	try:
		content = content_text.get(1.0, 'end')
		with open(file_name, 'w') as the_file:
			the_file.write(content)
	except IOError:
		tkinter.messagebox.showwarning("Save", "Could not save this file.")

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

#defining a function that allows the user to change the colour scheme / theme
def change_theme(event=None):
	selected_theme = theme_choice.get()
	fg_bg_colors = color_schemes.get(selected_theme)
	foreground_color, background_color = fg_bg_colors.split('.')
	content_text.config(background=background_color, fg=foreground_color)

#defining the function that shows a context menu
def show_popup_menu(event):
	popup_menu.tk_popup(event.x_root, event.y_root)


#defining the Cut, Copy, Paste, Undo, Redo functions
def cut():
	content_text.event_generate("<<Cut>>")
	#call the on_content_changed function
	on_content_changed()
	return "break"

def copy():
	content_text.event_generate("<<Copy>>")
	return "break"

def paste():
	content_text.event_generate("<<Paste>>")
	#call the on_content_changed function
	on_content_changed()
	return "break"

def undo():
	content_text.event_generate("<<Undo>>")
	#call the on_content_changed function
	on_content_changed()
	return "break"

def redo(event=None):
	content_text.event_generate("<<Redo>>")
	#call the on_content_changed function
	on_content_changed()
	return "break"

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
file_menu.add_command(label="Exit", accelerator='Alt+F4', command=exit_editor)
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
show_line_number = IntVar()
#setting the show_line_no variable to '1'
show_line_number.set(1)
#creating a boolean variable for the highlight line option
to_highlight_line = BooleanVar()
#adding a checkbutton that allows the user to toggle the show line number function 
view_menu.add_checkbutton(label="Show Line Numbers", variable=show_line_number)
#acreating a variable that stores the state of show_cursor_info
show_cursor_info = IntVar()
#set the value of the show_cursor_info to '1'
show_cursor_info.set(1)
#adding a checkbutton to toggle showing the cursor location on/off
view_menu.add_checkbutton(label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor_info_bar)
			#creating a variable to store the state of the highlight current line option
			#highlight_line = IntVar()
#creating a boolean variable for the highlight line option
to_highlight_line = BooleanVar()
#adding a checkbutton to toggle highlighting the current line on/off
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1, offvalue=0, variable=to_highlight_line, command=toggle_highlight)

#creating a themes cascade menu inside the view menu
themes_menu = Menu(menu_bar, tearoff=0)
#adding a themes menu inside the view menu
view_menu.add_cascade(label='Themes', menu=themes_menu)

#setting the available colour schemes
color_schemes = {
	'Light Mode': '#000000.#FFFFFF',
	'Dark Mode': '#FFFFFF.#525252',
}

#creating a variable that stores the selected theme
theme_choice = StringVar()
#setting the theme to default
theme_choice.set('Default')
#for loop that populates the themes menu with the various colour schemes
for k in sorted(color_schemes):
	#adding a radio button that allows user to select the colour scheme
	themes_menu.add_radiobutton(label=k, variable=theme_choice, command=change_theme)
#adding the above widgets to the view menu
menu_bar.add_cascade(label='View', menu=view_menu)

#adding and populating an about menu in the menu bar
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', command=display_about_messagebox)
about_menu.add_command(label='Help', command=display_help_messagebox)
menu_bar.add_cascade(label='About',  menu=about_menu)

#displaying the menu
root.config(menu=menu_bar)

#adding a frame for the horizontal shortcut icon bar with styling
shortcut_bar = Frame(root, height=30, background='#f7f7f7')
#display the shortcut icon bar
shortcut_bar.pack(expand='no', fill='x')

#adding the icons to the shortcut bar
icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo', 'find_text')
for i, icon in enumerate(icons):
	tool_bar_icon = PhotoImage(file='icons/{}.png'.format(icon))
	cmd = eval(icon)
	tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
	tool_bar.image = tool_bar_icon
	tool_bar.pack(side='left')

#adding a frame for the vertical line number bar with styling
line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0, background='#8a8a8a', state='disabled', wrap='none')
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

#adding a context menu
popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
	cmd = eval(i)
	popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=select_all)

#adding cursor information label
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')

#adding key bindings for the operations
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-S>', save)
content_text.bind('<KeyPress-F1>', display_help_messagebox)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='ivory2')
content_text.bind('<Button-3>', show_popup_menu)

root.protocol('WM_DELETE_WINDOW', exit_editor)

#execute the mainloop() function
root.mainloop()