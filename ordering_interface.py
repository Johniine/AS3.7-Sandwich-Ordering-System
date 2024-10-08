"""
Author: John Eric Ragos
Purpose: To create a program that allows the user to build and name their sandwich.
Date: 25/06/2024
Version 1: Created a GUI for the starting interface
Version 2: Created a GUI for the ordering interface
Version 3: Created a GUI for the help interface
Version 4: Created the GUI for the export interface
Version 5: Changed the GUI for ordering interface 
"""

# Imports
from tkinter import *
from tkinter import ttk

# Total
total_price = 0

# Colours
light_green = "#D9EAD3"
light_peach = "#FCE5CD"
light_yellow = "#FFF2CC"
light_cornflower_blue = "#C9DAF8"
light_magenta = "#EAD1DC"
light_red = "#F4CCCC"
light_green = "#D9EAD3"

# Fonts
courier = ("Courier", 17, "bold")
header_courier = ("Courier", 20, "bold")
sub_head_courier = ("Courier", 12, "bold")

# List
bread = ["Wholemeal","White","Cheesy White","Gluten Free"]
meat = ["Chicken","Beef","Salami","Vegan Slice"]
garnish1 = ["Onion","Tomato","Lettuce","Cheese"]
garnish2 = ["None","Onion","Tomato","Lettuce","Cheese"]

details = []

# Dictionary
prices = {"None":0,"Wholemeal":1.00,"White":0.80,"Cheesy White":1.20,"Gluten Free":1.40,"Chicken":2.60,
          "Beef":3.00,"Salami":4.00,"Vegan Slice":3.30,"Onion":1.69,"Tomato":1.00,"Lettuce":2.00,"Cheese":2.50}

# Hover information
info = "Hover on the\nImage to see\nThe item prices"

# Class
class Order:
    def __init__(self) -> None:
        # This is the teal green background for the starting interface
        self.background_frame3 = Frame(
            window3,width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame3.grid(padx=2,pady=5,column=0,row=0)

        self.background_frame4 = Frame(
            window3,width=180, height=443, bg=light_yellow, borderwidth=1, relief=SOLID
            )
        self.background_frame4.grid(padx=0,pady=0,column=1,row=0)

        # 1st Frame labels, images, and buttons
        # header for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame3,bg=light_yellow,text="Bring out 120% of the sandwich flavourness",
            font=sub_head_courier,width=49,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=3,columnspan=3)

        # Ordering interface images
        self.image_label_frame1 = Label(
            self.background_frame3,image=image_name1,borderwidth=1,relief=SOLID,text=""
            )
        self.image_label_frame1.grid(padx=0,pady=3,row=3,column=0)
        self.image_label_frame1.bind('<Enter>',lambda event:self.on_enter(event,image_type='bread'))
        self.image_label_frame1.bind('<Leave>',lambda event:self.on_leave(event,image_type='bread'))

        self.image_label_frame2 = Label(
            self.background_frame3,image=image_name2,borderwidth=1,relief=SOLID,text=""
            )
        self.image_label_frame2.grid(padx=0,pady=3,row=3,column=1)
        self.image_label_frame2.bind('<Enter>',lambda event:self.on_enter(event,image_type='meat'))
        self.image_label_frame2.bind('<Leave>',lambda event:self.on_leave(event,image_type='meat'))

        self.image_label_frame3 = Label(
            self.background_frame3,image=image_name3,borderwidth=1,relief=SOLID,text=""
            )
        self.image_label_frame3.grid(padx=0,pady=3,row=3, column=2)
        self.image_label_frame3.bind('<Enter>',lambda event:self.on_enter(event,image_type='garnish'))
        self.image_label_frame3.bind('<Leave>',lambda event:self.on_leave(event,image_type='garnish'))

        # Ordering Menu labels
        self.bread_label = Label(
            self.background_frame3,text="Bread",bg=light_cornflower_blue,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.bread_label.grid(padx=5,pady=5,row=2,column=0)

        self.meat_label = Label(
            self.background_frame3,text="Meat",bg=light_cornflower_blue,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.meat_label.grid(padx=5,pady=5,row=2,column=1)

        self.garnish_label = Label(
            self.background_frame3,text="Garnish",bg=light_cornflower_blue,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.garnish_label.grid(padx=5,pady=5,row=2,column=2)

        # Reset Buttons
        self.bread_button = Button(
            self.background_frame3,text="Reset Bread",bg=light_red,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID,
            command=lambda:self.reset_order("bread")
        )
        self.bread_button.grid(padx=5,pady=1,row=6,column=0)

        self.meat_button = Button(
            self.background_frame3,text="Reset Meat",bg=light_red,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID,
            command=lambda:self.reset_order("meat")
        )
        self.meat_button.grid(padx=5,pady=1,row=6,column=1)

        self.garnish_button = Button(
            self.background_frame3,text="Reset Garnish",bg=light_red,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID,
            command=lambda:self.reset_order("garnish")
        )
        self.garnish_button.grid(padx=5,pady=1,row=6,column=2)

        # Combo box
        self.chosen_bread = StringVar()
        self.chosen_bread.set("")

        self.chosen_meat1 = StringVar()
        self.chosen_meat1.set("")

        self.chosen_garnish1 = StringVar()
        self.chosen_garnish1.set("")

        self.chosen_garnish2 = StringVar()
        self.chosen_garnish2.set("")

        self.combobox_bread = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_bread,state="readonly",width=22
        )
        self.combobox_bread['values'] = bread
        self.combobox_bread.grid(padx=3,pady=2,column=0,row=4)

        self.combobox_meat1 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_meat1,state="readonly",width=22
        )
        self.combobox_meat1['values'] = meat
        self.combobox_meat1.grid(padx=3,pady=2,column=1,row=4)

        self.combobox_garnish1 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_garnish1,state="readonly",width=22
        )
        self.combobox_garnish1['values'] = garnish1
        self.combobox_garnish1.grid(padx=3,pady=2,column=2,row=4)

        self.combobox_garnish2 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_garnish2,state="readonly",width=22
        )
        self.combobox_garnish2['values'] = garnish2
        self.combobox_garnish2.grid(padx=3,pady=2,column=2,row=5)

        # 2nd frame labels, entry box and buttons
        self.error_label = Label(
            self.background_frame4,bg=light_red,text=info,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,height=5,
            justify=LEFT
            )
        self.error_label.grid(padx=3,pady=5)

        self.total_label = Label(
            self.background_frame4,bg=light_peach,text="Total: $0.00",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,height=2
            )
        self.total_label.grid(padx=3,pady=2)

        self.calculate_button = Button(
            self.background_frame4,bg=light_green,text="Calculate",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,
            command=self.calculate
        )
        self.calculate_button.grid(padx=3,pady=2)

        self.proceed_button = Button(
            self.background_frame4,bg=light_cornflower_blue,text="Proceed",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,state=DISABLED
        )
        self.proceed_button.grid(padx=3,pady=2)

        self.list_label1 = Label(
            self.background_frame4,text="",
            bg=light_peach,font=sub_head_courier,borderwidth=1,relief=SOLID,
            width=17,height=8
        )
        self.list_label1.grid(padx=3,pady=3)

        self.cancel_button = Button(
            self.background_frame4,text="Cancel Order",bg=light_red,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17
        )
        self.cancel_button.grid(padx=3,pady=5)

    # This functions will disable and enable the calculate and proceed button
    def disable_proc(self):
        '''This method disable the proceed button and enable the calculate button'''
        self.proceed_button.configure(state=DISABLED)
        self.calculate_button.configure(state=ACTIVE)
    
    def disable_calc(self):
        '''This method disable the calculate button and enable the proceed button'''
        self.proceed_button.configure(state=ACTIVE)
        self.calculate_button.configure(state=DISABLED)

    # This method get the users order and append them in a list to be user for calculation later
    def get_order(self):
        '''this method get the user's order and add them in a list'''
        self.customers_order = []
        self.customers_order.append(self.chosen_bread.get())
        self.customers_order.append(self.chosen_meat1.get())
        self.customers_order.append(self.chosen_garnish1.get())
        self.customers_order.append(self.chosen_garnish2.get())
    
    # This method will calculate the users order total and put them in the label
    def calculate(self):
        '''This method calculate the order ammount'''
        global total_price
        self.get_order()
        for i in self.customers_order:
            try: # Removes 'None' from the list
                self.customers_order.remove("None")
            except ValueError:
                try:
                    self.ingredient_list = "".join([str(f"{items}\n") for items in self.customers_order])
                    self.list_label1.configure(text=self.ingredient_list,justify=LEFT)
                    total_price += float(prices[i])
                    self.total_label.configure(text=f"Total: ${total_price:.2f}")
                    self.disable_calc()
                    self.error_label.configure(text=info)

                except KeyError: # Will verify if the combo-boxes are empty and will set the total to 0 and remove everything from the list
                    self.error_label.configure(text="Please Select\nAn Order First",justify=LEFT)
                    self.total_label.configure(text=f"Total: ${0:.2f}")
                    self.customers_order.clear()
                    self.list_label1.configure(text="")
                    self.disable_proc()
                    
    # Resets methods
    def reset_order(self,order_type):
        '''This method reset the user's orders'''
        global total_price
        try:
            if order_type == "bread": # This will reset the bread combo-box and the selected bread in the list
                self.customers_order.remove(self.chosen_bread.get())
                self.chosen_bread.set("")
            
            elif order_type == "meat": # This will reset the meat combo-box and the selected meat in the list
                self.customers_order.remove(self.chosen_meat1.get())
                self.chosen_meat1.set("")
            
            elif order_type == "garnish": # This will reset the garnish combo-box and the selected garnish in the list
                self.customers_order.remove(self.combobox_garnish1.get())
                self.customers_order.remove(self.chosen_garnish2.get())

            self.disable_proc()
            self.ingredient_list = "".join([str(f"{items}\n") for items in self.customers_order])
            self.list_label1.configure(text=self.ingredient_list,justify=LEFT)
            total_price = 0
            self.total_label.configure(text=f"Total: ${total_price:.2f}")
            self.error_label.configure(text=info,justify=LEFT)

        except: # This will put an error message to the user if it encountered an error
            self.error_label.configure(text=f"Can't reset\n{order_type.title()} order",justify=LEFT)
            self.disable_proc()


    def on_enter(self,event,image_type):
        '''This method will change the image to the menu after the user hover on it'''
        if image_type == 'bread':
            self.image_label_frame1.config(image=bread_menu_image)
        elif image_type == 'meat':
            self.image_label_frame2.config(image=meat_menu_image)
        elif image_type == 'garnish':
            self.image_label_frame3.config(image=garnish_menu_image)
    
    def on_leave(self,event,image_type):
        '''This method will change the image back after the user stop hover on it'''
        if image_type == 'bread':
            self.image_label_frame1.config(image=image_name1)
        elif image_type == 'meat':
            self.image_label_frame2.config(image=image_name2)
        elif image_type == 'garnish':
            self.image_label_frame3.config(image=image_name3)

# Main Program

# Adjusted the window to make it not resizable for future proofing
window3 = Tk()
window3.title("Ordering Interface")
window3.configure(bg=light_peach)
window3.geometry("700x418")
window3.resizable(0,0)

# Loads the image to add in the order interface
bread_image = "images\Hamito.gif"
image_name1 = PhotoImage(file=bread_image)
meat_image = "images\Todo.gif"
image_name2 = PhotoImage(file=meat_image)
garnish_image = "images\Yuji.gif"
image_name3 = PhotoImage(file=garnish_image)

# Loads the images for the hover menu
bread_menu = "images\menu_bread.gif"
bread_menu_image = PhotoImage(file=bread_menu)
meat_menu = "images\menu_meat.gif"
meat_menu_image = PhotoImage(file=meat_menu)
garnish_menu = "images\menu_garnish.gif"
garnish_menu_image = PhotoImage(file=garnish_menu)

# Call the class
Order()

# Start the mainloop
window3.mainloop()