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

#function that links the 'Cut' button to the cut functionality 
def cut():
	content_text.event_generate("<<Cut>>")

#function that links the 'Cut' button to the cut functionality
def copy():
	content_text.event_generate("<<Copy>>")

#function that links the 'Cut' button to the cut functionality
def paste():
	content_text.event_generate("<<Paste>>")

def undo():
	content_text.event_generate("<<Undo>>")

def redo():
	content_text.event_generate("<<Redo>>")



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
file_menu.add_command(label="New", accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0)
file_menu.add_command(label="Open", accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0)
file_menu.add_separator()#add a separator
file_menu.add_command(label="Save as...", accelerator='Shift+Ctrl+S')
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
edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F')
edit_menu.add_separator()#add a separator
edit_menu.add_command(label='Select All', underline=7, accelerator='Ctrl+A')
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
content_text.bind('Control-y', redo)
content_text.bind('Control-Y', redo)
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
#display the scroll bar
scroll_bar.pack(side='right', fill='y')

#displaying the menu
root.config(menu=menu_bar)

#execute the mainloop() function
root.mainloop()