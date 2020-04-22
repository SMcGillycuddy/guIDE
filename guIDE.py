'''
guIDE is a lightweight text editor / IDE.

Functionality: 
File -> New, Open, Save, Save As..., Exit
Edit -> Cut, Copy, Paste, Undo, Redo
View -> ----TODO-----
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

#-----TO DO-----#
#adding and populating a view menu in the menu bar
view_menu = Menu(menu_bar, tearoff=0)
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
content_text = Text(root, wrap='word')
#display the main content Text widget
content_text.pack(expand='yes', fill='both')
#adding a scroll bar widget to the main text content widget
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
#display the scroll bar
scroll_bar.pack(side='right', fill='y')

#displaying the menu
root.config(menu=menu_bar)

#execute the mainloop() function
root.mainloop()