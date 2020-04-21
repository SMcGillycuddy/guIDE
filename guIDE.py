'''
guIDE is a lightweight text editor / IDE.

Functionality: 
File -> New, Open, Save, Save As..., Exit
Edit -> Cut, Copy, Paste, Undo, Redo
View -> ----TODO-----
About -> About, Help

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

#specifing the icons for the menu
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

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
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', image=undo_icon)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon)
edit_menu.add_separator()#add a separator
edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F')
edit_menu.add_separator()#add a separator
edit_menu.add_command(label='Select All', underline=7, accelerator='Ctrl+A')
menu_bar.add_cascade(label='Edit', menu=edit_menu)


#----TO DO----
#adding and populating a file menu in the menu bar
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)


#adding and populating an about menu in the menu bar
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About')
about_menu.add_command(label='Help')
menu_bar.add_cascade(label='About',  menu=about_menu)


#displaying the menu
root.config(menu=menu_bar)

#execute the mainloop() function
root.mainloop()