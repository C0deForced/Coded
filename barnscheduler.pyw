from tkinter import *
from tkinter import ttk

#declairing the tkinter object
main_window = Tk()

#delairing the dictionary that will store all tabs
tabs = {}
#Main Window setup class: Initializing main window size, window title, base frame for time shedule
class window_setup:
    def __init__(self, main, geo, name):

        #setting up the size of the program window
        self.main = main.geometry(geo)
        
        #setting the name of the window
        self.name = main.title(name)


        #setting up frame for main Tab frame
        self.schedule_frame = Frame(main)
        self.schedule_frame.grid(row=0, pady=10, padx=10, sticky=W)
        
        self.note = ttk.Notebook(self.schedule_frame)
        self.note.grid(row=0, column=1)

        self.tabframe = Frame(self.note, width=50, height=50)
        self.tabframe.grid(row=0)





        #setting up the button and entry frame
        self.button_frame = Frame(main)
        self.button_frame.grid(row=1, padx=10, pady=10, sticky=W)

class main_treeview:
    def __init__(self, main, time, name, location):
        self.data_table = ttk.Treeview(main)
        self.revealplus = 0
        self.data_table['columns'] = ('time', 'name', 'location')
        self.data_table.column('#0', width=str(self.revealplus), anchor=W)
        self.data_table.column('time', anchor=W, width=100, minwidth=75)
        self.data_table.column('name', anchor=CENTER, width=100, minwidth=75)
        self.data_table.column('location', anchor=W, width=100, minwidth=75)
        self.data_table.heading('#0', text='', anchor=W)
        self.data_table.heading('time', text='time', anchor=W)
        self.data_table.heading('name', text='name', anchor=CENTER)
        self.data_table.heading('location', text='location', anchor=W)
        self.data_table.grid(row=0)

class data_input_setup:
    def __init__(self, main):

        self.name_label = Label(main, text="time:")
        self.name_label.grid(row=0, column=0)
        self.time_label = Label(main,text="name:")
        self.time_label.grid(row=0, column=2)
        self.location_lable = Label(main,text="location:")
        self.location_lable.grid(row=0, column=4)
        #Name data entry
        self.name = Entry(main, width=25)
        self.name.grid(row=0, column=1, padx=10)
        #Time for event
        self.time = Entry(main, width=25)
        self.time.grid(row=0, column=3, padx=10)
        #where is the person going to be during the time block 
        self.location = Entry(main, width=25)
        self.location.grid(row=0, column=5, padx=10)
        
        #button to update the current record selected
        self.update_b = Button(main, text='Update', command=lambda: do_value_update())
        self.update_b.grid(row=1, column=0, padx=10, pady=10)

        self.remove_b = Button(main, text='remove', command=lambda: do_remove_value())
        self.remove_b.grid(row=1, column=1, padx=10, pady=10)

class new_treeview:
    def __init__(self, main, time, name, location):
        self.data_table = ttk.Treeview(main)
        self.data_table['columns'] = ('time', 'name', 'location')
        self.data_table.column('#0', minwidth=25, width=50)
        self.data_table.column('time', minwidth=50, anchor=W)
        self.data_table.column('name', minwidth=50, anchor=CENTER)
        self.data_table.column('location', minwidth=50, anchor=W)
        self.data_table.heading('#0', text='',anchor=W)
        self.data_table.heading('time', text=time,anchor=W)
        self.data_table.heading('name', text=name,anchor=CENTER)
        self.data_table.heading('location', text=location,anchor=W)
        self.data_table.grid(row=0)



#run the actual class to make the window do the thing
page = window_setup(main_window, "800x700", "Barn chart")


page.note.add(page.tabframe, text="Base Schedule") 
main_tree= main_treeview(page.tabframe, "time", "name", "location" )


#setup the data input
data = data_input_setup(page.button_frame)



data_values = [
    ["8:00am","",""],
    ["9:00am","",""],
    ["10:00am","",""],
    ["11:00am","",""],
    ["12:00noon","",""],
    ["1:00pm","",""],
    ["2:00pm","",""],
    ["3:00pm","",""],
    ["4:00pm","",""],
    ["5:00pm","",""],
    ["6:00pm","",""],
    ["7:00pm","",""],
    ["8:00pm","",""],
    ]

count = 0
for x in data_values:
    main_tree.data_table.insert(parent='', index='end', iid=count, text='', values=(x[0], x[1], x[2]))
    count += 1

pop_menu = Menu(main_window, tearoff=0)

pop_menu.add_command(label='add time', command=lambda: insert_pop())
pop_menu.add_command(label='remove time')
pop_menu.add_command(label='FUCK!')

def menu_pop(event):
    try:
        pop_menu.tk_popup(event.x_root, event.y_root, 0)
    finally:
        pop_menu.grab_release()

main_window.bind("<Button-3>", menu_pop)





#print(main_tree.data_table.get_children())
def do_value_update():
    main_tree.data_table.insert(parent='0', index='end', iid=16, text='', values=("8:10am", 'DJ', 'Ring'))
    main_tree.data_table.move('16', '0', '0')



def insert_pop():
    global insert
    global data_time_in
    global data_name_in
    global data_location_in
    insert = Toplevel(main_window)
    insert.title('Enter Time')
    insert.geometry('250x150')
    
    data_time_in = Entry(insert)
    data_name_in = Entry(insert)
    data_location_in = Entry(insert)
    time_label = Label(insert, text='Time: ')
    name_label = Label(insert, text='Name: ')
    location_label = Label(insert, text='Location:')

    time_label.grid(row=0, column=0, sticky=W)
    name_label.grid(row=1, column=0, sticky=W)
    location_label.grid(row=2, column=0, sticky=W)

    data_time_in.grid(row=0, column=1, sticky=W)
    data_name_in.grid(row=1, column=1, sticky=W)
    data_location_in.grid(row=2, column=1, sticky=W)
    
    close = Button(insert, text='ok', command=lambda:[block_val(), close_time_entry()])
    close.grid(row=3, sticky=W)

def close_time_entry():
    insert.destroy()
 
def block_val():
    time_in = data_time_in.get()
    name_in = data_name_in.get()
    location_in = data_location_in.get()
    print(time_in, name_in, location_in)

def do_remove_value():
    pass

def create_tab():
    name = data.name.get()
    tab_ID = 'tab_' + str(name)
    tabs[tab_ID] = Frame(page.tabframe, bg='#F2B33D', width=50, height=50)
    tabs[tab_ID].grid(row=1, ipady=30, ipadx=30)
    page.note.add(tabs[tab_ID], text=name)
    new_treeview(tabs[tab_ID])




main_window.mainloop()