import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
from PIL import ImageTk, Image
import os, shutil



main_app = tk.Tk()
main_app.geometry('1200x800')
main_app.title('Sasta Editor')
main_app.wm_iconbitmap(bitmap = 'icon.ico')
#--------------------------------MAIN MENU-----------------------------

mainmenu = tk.Menu(main_app)

# File 
new_icon = tk.PhotoImage(file = 'icons/new.png')
open_icon = tk.PhotoImage(file = 'icons/open.png')
save_icon = tk.PhotoImage(file = 'icons/save.png')
save_as_icon = tk.PhotoImage(file = 'icons/save_as.png')
exit_icon = tk.PhotoImage(file = 'icons/exit.png')


file = tk.Menu(mainmenu, tearoff = 0)





# Edit 

copy_icon = tk.PhotoImage(file = 'icons/copy.png')
paste_icon = tk.PhotoImage(file = 'icons/paste.png')
cut_icon = tk.PhotoImage(file = 'icons/cut.png')
clear_icon = tk.PhotoImage(file = 'icons/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons/find.png')

edit = tk.Menu(mainmenu, tearoff = 0)



# View 

tool_bar_icon = tk.PhotoImage(file = 'icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'icons/status_bar.png')

view = tk.Menu(mainmenu, tearoff = 0)




# Color theme

light_default_icon = tk.PhotoImage(file = 'icons/light_default.png')
light_plus_icon = tk.PhotoImage(file = 'icons/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons/dark.png')
monokai_icon = tk.PhotoImage(file = 'icons/monokai.png')
night_blue_icon = tk.PhotoImage(file = 'icons/night_blue.png')
pink_icon = tk.PhotoImage(file = 'icons/red.png')
 

color_theme = tk.Menu(mainmenu, tearoff = 0)

theme_choice = tk.StringVar()

color_icons = (light_default_icon, light_plus_icon, dark_icon, monokai_icon, night_blue_icon, pink_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2'),
    'Pink' : ('#2d2d2d', '#ffe8e8')
}

# Help

about_icon = tk.PhotoImage(file = 'icons/icon3.png')
the_creator_icon = tk.PhotoImage(file = 'icons/the_creator.png')

help = tk.Menu(mainmenu, tearoff = 0)

# cascade

mainmenu.add_cascade(label = 'File',menu = file)
mainmenu.add_cascade(label = 'Edit',menu = edit)
mainmenu.add_cascade(label = 'View',menu = view)
mainmenu.add_cascade(label = 'Color Theme',menu = color_theme)
mainmenu.add_cascade(label = 'Help',menu = help)

# -----------------------------END MAIN MENU----------------------------



#--------------------------------TOOLBAR----------------------------

tool_bar = ttk.Label(main_app)
tool_bar.pack(side = tk.TOP, fill = tk.X)

# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0,column = 0, padx = 5)

# size box
size_var = tk.IntVar()
size_box = ttk.Combobox(tool_bar, width = 15, textvariable = size_var, state = 'readonly')
size_box['values'] = tuple(range(8,80,2))
size_box.current(5)
size_box.grid(row = 0,column = 1, padx = 5)

# bold button()
bold_icon = tk.PhotoImage(file = 'icons/bold.png')
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0,column = 2, padx =5)

# italic button()
italic_icon = tk.PhotoImage(file = 'icons/italic.png')
italic_btn = ttk.Button(tool_bar, image = italic_icon)
italic_btn.grid(row = 0,column = 3, padx =5)

# underline button()
underline_icon = tk.PhotoImage(file = 'icons/underline.png')
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0,column = 4, padx =5)

# font_color button()
font_color_icon = tk.PhotoImage(file = 'icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image = font_color_icon)
font_color_btn.grid(row = 0,column = 5, padx =5)

# align_left button()
align_left_icon = tk.PhotoImage(file = 'icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image = align_left_icon)
align_left_btn.grid(row = 0,column = 6, padx =5)

# align_center button()
align_center_icon = tk.PhotoImage(file = 'icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image = align_center_icon)
align_center_btn.grid(row = 0,column = 7, padx =5)

# underline button()
align_right_icon = tk.PhotoImage(file = 'icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image = align_right_icon)
align_right_btn.grid(row = 0,column = 8, padx =5)


creation = ttk.Label(tool_bar, text = 'Created by Sachin' ,foreground = '#9E9696')
creation.grid(row = 0, column = 20,padx = 300,sticky = tk.E)



# -----------------------------END TOOLBAR----------------------------


#--------------------------------TEXT EDITOR-----------------------------

text_editor = tk.Text(main_app)
text_editor.config(wrap = 'word', relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font funcionality

current_font_family = 'Arial'
current_font_size = 14

def change_font(event = None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family,current_font_size))

def change_size(event = None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
size_box.bind("<<ComboboxSelected>>", change_size)

text_editor.configure(font=('Arial',14))


# buttons fuctionality

# bold button

def change_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] =='normal':
        text_editor.configure(font = (current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] =='bold':
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

# underline button

def underline_font():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] ==0:
        text_editor.configure(font = (current_font_family,current_font_size, 'underline'))
    if text_property.actual()['underline'] ==1:
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

underline_btn.configure(command = underline_font)


# underline button

def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] =='roman':
        text_editor.configure(font = (current_font_family,current_font_size, 'italic'))
    if text_property.actual()['slant'] =='italic':
        text_editor.configure(font = (current_font_family,current_font_size,'roman'))

italic_btn.configure(command = change_italic)

# font color functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

font_color_btn.configure(command = change_font_color)

# align functionality

# left align

def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left', justify =tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT , text_content, 'left')

align_left_btn.configure(command = align_left)

# center button

def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center', justify =tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT , text_content, 'center')

align_center_btn.configure(command = align_center)

# left align

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right', justify =tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT , text_content, 'right')

align_right_btn.configure(command = align_right)


# -----------------------------END TEXT EDITOR----------------------------


#--------------------------------STATUS BAR-----------------------------

status_bar = ttk.Label(main_app, text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM, fill = tk.X)

creation2 = ttk.Label(status_bar, text = '--Created by Sachin' )
creation2.pack(side = tk.RIGHT)

text_changed = False
def changed(event = None):
    global text_changed
    if text_editor.edit_modified():
        text_changed= True
        words = len(text_editor.get(1.0 , 'end-1c').split())
        characters = len(text_editor.get(1.0 , 'end -1c').replace(' ' , ''))
        status_bar.config(text = f'Characters = {characters}  Words = {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)

# -----------------------------END STATUS BAR----------------------------


#--------------------------------MAIN MENU FUNCTIONALITY-----------------------------
url = ''

def new_file(event = None):
    global url
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url, 'w', encoding = 'utf-8') as fw:
                        fw.write(content)
                    url = ''
                    text_editor.delete(1.0, tk.END)
                else:
                    try:
                        url = filedialog.asksaveasfile(mode = 'w' , defaultextension = '.txt', filetypes = (('Type File', '*.txt'), ('All files', '*.*')))
                        content2 = str(text_editor.get(1.0,tk.END))
                        url.write(content2)
                        url.close()
                        url = ''
                        text_editor.delete(1.0, tk.END)
                    except:
                        return
            elif mbox is False:
                url = ''
                text_editor.delete(1.0, tk.END)
        else:
            url = ''
            text_editor.delete(1.0, tk.END)
    except:
        return

def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Type File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

def save_file(event = None):
    global url
    try:
        if url:
            content =str(text_editor.get(1.0,tk.END))
            with open(url, 'w', encoding = 'utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w' , defaultextension = '.txt', filetypes = (('Type File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
            return

def save_as_file(event = None):
    try:
        url = filedialog.asksaveasfile(mode = 'w' , defaultextension = '.txt', filetypes = (('Type File', '*.txt'), ('All files', '*.*')))
        content = text_editor.get(1.0,tk.END)
        url.write(content)
        url.close()
    except:
        return

def exit_fun(event = None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url, 'w', encoding = 'utf-8') as fw:
                        fw.write(content)
                    main_app.destroy()
                else:
                    try:
                        url = filedialog.asksaveasfile(mode = 'w' , defaultextension = '.txt', filetypes = (('Type File', '*.txt'), ('All files', '*.*')))
                        content2 = str(text_editor.get(1.0,tk.END))
                        url.write(content2)
                        url.close()
                        main_app.destroy()
                    except:
                        return
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return


    


# file commands
file.add_command(label = 'New', image = new_icon, compound = tk.LEFT,accelerator = 'Ctrl+N', command = new_file)
file.add_command(label = 'Open', image = open_icon, compound = tk.LEFT,accelerator = 'Ctrl+O', command = open_file)
file.add_command(label = 'Save', image = save_icon, compound = tk.LEFT,accelerator = 'Ctrl+S', command = save_file)
file.add_command(label = 'Save As', image = save_as_icon, compound = tk.LEFT,accelerator = 'Ctrl+Shift+S', command = save_as_file)
file.add_command(label = 'Exit', image = exit_icon, compound = tk.LEFT,accelerator = 'Ctrl+Q', command = exit_fun)

# edit commands

def find_fun(event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove(word, '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add(word, start_pos , end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(word, foreground = 'red' , background = 'yellow')
    def replace():
        word = find_input.get()
        replaced = replace_input.get()
        content = text_editor.get(1.0 , tk.END)
        new_content = content.replace(word, replaced)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    # frame
    find_frame = ttk.LabelFrame(find_dialogue, text = 'Find/Replace')
    find_frame.pack(pady = 20)

    # labels
    text_find_label = ttk.Label(find_frame, text = 'Find: ')
    text_replace_label = ttk.Label(find_frame, text = 'Replace: ')
 
    #entry
    find_input = ttk.Entry(find_frame, width = 30)
    replace_input = ttk.Entry(find_frame, width = 30)

    # button
    find_button = ttk.Button(find_frame, text = 'Find', command = find)
    replace_button = ttk.Button(find_frame, text = 'Replace', command = replace)

    # grid
    text_find_label.grid(row= 0, column = 0, padx = 4, pady = 4)
    text_replace_label.grid(row= 1, column = 0, padx = 4, pady = 4)
    find_input.grid(row= 0, column = 1, padx = 4, pady = 4)    
    replace_input.grid(row= 1, column = 1, padx = 4, pady = 4)    
    find_button.grid(row = 2, column = 0 , padx =8, pady = 4)
    replace_button.grid(row = 2, column = 1 , padx =8, pady = 4)

    find_dialogue.mainloop()


edit.add_command(label = 'Copy', image = copy_icon, compound = tk.LEFT,accelerator = 'Ctrl+C', command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = 'Paste', image = paste_icon, compound = tk.LEFT,accelerator = 'Ctrl+V', command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label = 'Cut', image = cut_icon, compound = tk.LEFT,accelerator = 'Ctrl+X', command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = 'Clear All', image = clear_icon, compound = tk.LEFT,accelerator = 'Ctrl+Shift+X', command = lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label = 'Find/Replace', image = find_icon, compound = tk.LEFT,accelerator = 'Ctrl+F', command = find_fun)

# view check buttons

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def toolbar_fun():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM, fill = tk.X)
        show_toolbar = True

def statusbar_fun():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM, fill = tk.X)
        show_statusbar = True




view.add_checkbutton(label = 'Tool Bar',onvalue = 1, offvalue = 0,variable = show_toolbar, image = tool_bar_icon, compound = tk.LEFT, command = toolbar_fun)
view.add_checkbutton(label = 'Status Bar',onvalue = 1, offvalue = 0,variable = show_statusbar, image = status_bar_icon, compound = tk.LEFT, command = statusbar_fun)

# color theme commands

# color theme

def change_theme():
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color , bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background = bg_color, fg = fg_color)



count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image = color_icons[count], variable = theme_choice,  compound = tk.LEFT, command = change_theme)
    count += 1

# help commands

def sasta_editor():

    sasta_message = tk.Toplevel()
    sasta_message.title('About Sasta Editor')
    sasta_message.geometry('485x410')

    label_frame = ttk.LabelFrame(sasta_message, text = 'About Sasta Editor ')
    label_frame.grid(row = 0, column = 0, padx = 25, pady = 20)

    canvas = tk.Canvas(label_frame,width = 130, height = 300)
    canvas.grid(rowspan = 15,column = 0, padx = 10, pady = 20)
    photo = tk.PhotoImage(file = 'icons\icon3.png')
    canvas.create_image(0,0, image = photo, anchor ='nw')

    label1 = ttk.Label(label_frame, text= 'Sasta Editor ',font = 'Times 20')
    label1.grid(row= 1, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label2 = ttk.Label(label_frame, text= 'Unregistered')
    label2.grid(row= 2, column= 1, sticky = tk.N, padx = 40, pady = 0) 


    label4 = ttk.Label(label_frame, text= 'Copyright @ Birth of Universe - 2019')
    label4.grid(row= 4, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label5 = ttk.Label(label_frame, text= 'Version 1.0.0, Built 007')
    label5.grid(row= 5, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label6 = ttk.Label(label_frame, text= 'Sasta editor is a free and open source documents reader, witer and editor ')
    label6.grid(row= 7, rowspan= 4 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label7 = ttk.Label(label_frame, text= 'made by very talented programmer Mr. Sachin of IITD Community. ')
    label7.grid(row= 8, rowspan= 4 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label8 = ttk.Label(label_frame, text= 'This Editor as the name suggests is now a beginner level editor, that is ')
    label8.grid(row= 9, rowspan= 4 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 

    label9 = ttk.Label(label_frame, text= 'is capable of some basic editings of text. Stay updated with our resources ')
    label9.grid(row= 10, rowspan= 4 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 

    label10 = ttk.Label(label_frame, text= 'you will soon get one of the best softwares in the whole world.')
    label10.grid(row= 11, rowspan= 4 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 



    sasta_message.mainloop()

def creator():
    global the_creator_icon
    creator = tk.Toplevel()
    creator.title('About The Creator')
    creator.geometry('565x535')

    label_frame = ttk.LabelFrame(creator, text = 'About Sasta Editor ')
    label_frame.grid(row = 0, column = 0, padx = 25, pady = 20)

    canvas = tk.Canvas(label_frame,width = 130, height = 430)
    canvas.grid(rowspan = 20,columnspan = 1, padx = 10, pady = 20)
    # photo = tk.PhotoImage(file = 'icons\the_creator.png')
    canvas.create_image(0,0, image = the_creator_icon, anchor ='nw')


    label1 = ttk.Label(label_frame, text= 'SACHIN ',font = 'Times 25 bold')
    label1.grid(row= 3, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label2 = ttk.Label(label_frame, text= '                   - the creator')
    label2.grid(row= 4, column= 1, sticky = tk.N, padx = 40, pady = 0)
   
 
    label6 = ttk.Label(label_frame, text= 'Mr. Sachin is a top class devoloper currently studying in one of the most prestigious ')
    label6.grid(row= 10 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label7 = ttk.Label(label_frame, text= 'institutes of India, going to complete his degree in 2023.')
    label7.grid(row= 11, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label8 = ttk.Label(label_frame, text= 'This software is his one of the earliest work.Stay updated with his work you are definately ')
    label8.grid(row= 13 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label9 = ttk.Label(label_frame, text= 'going to get astonished with his evry creation. ')
    label9.grid(row= 14 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label11 = ttk.Label(label_frame, text= 'You can follow his works from these direct links: ')
    label11.grid(row= 15, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label10 = ttk.Label(label_frame, text= 'Facebook:  ')
    label10.grid(row= 16 , column = 0 ,sticky = tk.NW, padx = 20, pady = 0)

    data = tk.StringVar()
    data.set('https://www.facebook.com/profile.php?id=100010131825138')
    w = tk.Entry(label_frame, textvariable = data, state = 'readonly', width = 55)
    w.grid(row = 16,column = 0,columnspan = 2,sticky = tk.NW, padx = 80)

    label12 = ttk.Label(label_frame, text= 'Instagram:')
    label12.grid(row= 17, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0)

    data2 = tk.StringVar()
    data2.set('https://www.instagram.com/_.mr._sachin._/')
    w2 = tk.Entry(label_frame, textvariable = data2, state = 'readonly', width = 55)
    w2.grid(row = 17,column = 0,columnspan = 2,sticky = tk.NW, padx = 80)

    label13 = ttk.Label(label_frame, text= 'Youtube: Under Construction........')
    label13.grid(row= 18, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0)

    label14 = ttk.Label(label_frame, text= 'WebPage: Under Construction........')
    label14.grid(row= 19, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0)
    





help.add_command(label = 'About Sasta Editor', compound = tk.LEFT, command = sasta_editor)
help.add_separator()
help.add_command(label = 'About The Creator', compound = tk.LEFT, command = creator)


# -----------------------------END MAIN MENU FUNCTIONALITY----------------------------


main_app.config(menu=mainmenu)

#  bind shortcut keys

main_app.bind('<Control-n>', new_file)
main_app.bind('<Control-o>', open_file)
main_app.bind('<Control-s>', save_file)
main_app.bind('<Control-Shift-s>', save_as_file)
main_app.bind('<Control-q>', new_file)
main_app.bind('<Control-n>', exit_fun)
main_app.bind('<Control-f>', find_fun)



main_app.mainloop()