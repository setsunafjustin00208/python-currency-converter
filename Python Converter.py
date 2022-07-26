import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from unit_converter.converter import convert, converts
from PIL import ImageTk, Image


c = CurrencyRates()
b = BtcConverter()


#========= CENTERED WINDOW CONFIGURATION =========#

def center(win):
   win.update_idletasks()
   width = win.winfo_width()
   frm_width = win.winfo_rootx() - win.winfo_x()
   win_width = width + 2 * frm_width
   height = win.winfo_height()
   titlebar_height = win.winfo_rooty() - win.winfo_y()
   win_height = height + titlebar_height + frm_width
   x = win.winfo_screenwidth() // 2 - win_width // 2
   y = win.winfo_screenheight() // 2 - win_height // 2
   win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
   win.deiconify()

#========= CENTERED WINDOW CONFIGURATION =========#

#========= CURRENCY CONERTER ===========#

def CurrencyConverter():
       
       #+++++ List of Currency +++++#
       
       CurrencyCode_list = ["PHP", "USD", "EUR", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "SGD", "THB", "ZAR"]
       
       #+++++ List of Currency +++++#
       
       def one():
              
              def exit_one():
                     one.destroy()
                     curcon.deiconify()
              
              #========= One To One Currency Converter Window =========#
              
              
              #+++++ One to One Currency Converter Window Configuration +++++#
              
              curcon.withdraw()
              one = tk.Toplevel(curcon)
              one.resizable(False,False)
              one.geometry("400x400")
              one.title("One to One Conversion")
              one.protocol("WM_DELETE_WINDOW", exit_one)
              
              #+++++ One to One Currency Converter Window Configuration +++++#
              
              #++++ One to One Currency Converter Window Logos +++++#
              
              oneiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\1-to-1.png").resize((50,65), Image.ANTIALIAS)
              oneicon = ImageTk.PhotoImage(oneiconimage)
              
              oneimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\peso-icon.png")
              one.iconphoto(False,oneimage)
              
              #++++ One to One Currency Converter Window Logos +++++#
              
              #======= Functions of One to One Conversion ========#
              
              def RealTimeCurrencyConversion(): 
		

                     from_currency = FromCurrency_option.get() 
                     to_currency = ToCurrency_option.get()

                     if (Amount1_field.get()==""):
                            tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

                     elif (from_currency=="currency" or to_currency=="currency"):
                            tkinter.messagebox.showwarning("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

                     else:
                            try:
                                   c.convert(from_currency, to_currency, float(Amount1_field.get()))

                            except Exception as e:
                                   e = tkinter.messagebox.showerror("Error!!"," The Connection to the Internet is Lost!")

                            else:
                                   Amount2_field.configure(state=NORMAL)
                                   Amount2_field.delete(0, tk.END)
                                   new_amt = c.convert(from_currency,to_currency,float(Amount1_field.get()))
                                   new_amount = float("{:.2f}".format(new_amt))
                                   Amount2_field.insert(0, str(new_amount))
                                   Amount2_field.insert(0, str(to_currency + " "))
                                   Amount2_field.configure(state='readonly')

              def clear_all(): 
                     Amount2_field.configure(state=NORMAL)
                     Amount1_field.delete(0, tk.END) 
                     Amount2_field.delete(0, tk.END)
                     FromCurrency_option.set("currency") 
                     ToCurrency_option.set("currency") 
                     Amount2_field.configure(state='readonly')
             
               
              #======= Functions of One to One Conversion ========#
              
              #=============== One To One Currency Converter Main GUI ================#
              
              
              tk.Label(one,font=('lato black', 17,'bold'),text = ' One On One Conversion',fg='black',compound='left', image=oneicon).grid(row=0, column=0,padx=32)
              label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
              label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)

              label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
              label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)

              label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
              label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)

              label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
              label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)


              Label_1 =Label(one, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
              Label_1.grid(row=5, column=0,sticky=W)



              FromCurrency_option = ttk.Combobox(one, value=CurrencyCode_list, state='readonly') 
              ToCurrency_option = ttk.Combobox(one, value=CurrencyCode_list, state='readonly') 

              FromCurrency_option.set("currency") 
              ToCurrency_option.set("currency") 

              FromCurrency_option.grid(row = 3, column = 0) 
              ToCurrency_option.grid(row = 4, column = 0) 


              Amount1_field = tk.Entry(one) 
              Amount1_field.grid(row=2,column=0,padx=10,pady=10,)

              Amount2_field = tk.Entry(one,state='readonly')
              Amount2_field.grid(row=8,column=0,padx=80,pady=10, sticky=E) 
              

              tk.Label(one,text="").grid(row=7)


              Label_9 =Button(one, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="blue",fg = "white",command=RealTimeCurrencyConversion)
              Label_9.grid(row=6, column=0)

              Label_9 =Button(one, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
              Label_9.grid(row=9, column=0)
             
              
              #=============== One To One Currency Converter Main GUI ================#
              
              
              
              
              #+++ One To One Currency Converter Window Execution +++#
              
              center(one)
              one.mainloop()
              
              #+++ One To One Currency Converter Window Execution +++#
              
              #========= One To One Currency Converter Window =========#
       def second():
              
              def exit_second():
                     second.destroy()
                     curcon.deiconify()
              
              #============= One to all Conversion Window =============#
              
              
              #+++++ One to all Conversion Window Configuration +++++#
              
              second = tk.Toplevel(curcon)
              second.resizable(False,False)
              second.geometry("400x470")
              second.title("One to All Conversion")
              second.protocol("WM_DELETE_WINDOW", exit_second)
              
              #+++++ One to all Conversion Window Configuration +++++#
              
              
              #+++++ One to all Conversion Functions +++++#
              
              def delete_multi():
                     Amount_field.delete(0, tk.END) 
                     FromCurrency.set("currency")
                     getRateview.delete(*getRateview.get_children())

              def multicurrencyConversion():
                     a = 0

                     base = FromCurrency.get()
                     amount = Amount_field.get()

                     if(base == "currency"):
                            tkinter.messagebox.showwarning("Error !!", "Currency Not Selected.\n Please select a Currency form menu.")

                     elif(amount == ""):
                            tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

                     else:
                            try:
                                   convert = c.convert(base, CurrencyCode_list[a-1],float(Amount_field.get()))

                            except Exception as e:
                                   e = tkinter.messagebox.showerror("Error!!"," The Connection to the Internet is Lost!")
                            else:
                                   while a < 33:
                                          a = a + 1
                                          convert = c.convert(base, CurrencyCode_list[a-1], float(Amount_field.get()))
                                          converted_amt = float("{:.2f}".format(convert))
                                          getRateview.insert("", a, text=CurrencyCode_list[a-1], values=converted_amt)

              
              #+++++ One to all Conversion Functions +++++#
              
              
              #+++++ One to All Conversion Logos +++++#
              
              secondiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\1-to-all.png").resize((50,65), Image.ANTIALIAS)
              secondicon = ImageTk.PhotoImage(secondiconimage)
              
              secondimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\peso-icon.png")
              second.iconphoto(False,secondimage)
              
              #+++++ One to All Conversion Logos +++++#
              
              
              #========== One To All Conversion Main GUI ==========#
              
              tk.Label(second,font=('lato black', 17,'bold'),text = ' One On All Conversion',fg='black',compound='left', image=secondicon).grid(row=0, column=0,padx=32)
              
              label1 = tk.Label(second,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
              label1.grid(row=2, column=0, padx=20, pady=5, sticky=W)
              
              Amount_field = tk.Entry(second) 
              Amount_field.grid(row=2,column=0,padx=10,pady=10)
              
              label2 = tk.Label(second,font=('lato black', 13,'bold'), text = "Currency:  ", fg = "black") 
              label2.grid(row=3, column=0, padx=20, pady=5, sticky=W)
              
              FromCurrency = ttk.Combobox(second,state='readonly', values=CurrencyCode_list)
              FromCurrency.set("currency")
              FromCurrency.grid(column=0, row=3)
              
              tk.Button(second, text = "Convert", font=('Century Gothic', 10, 'italic','bold'),fg='white',bg='orange',command=multicurrencyConversion).grid(row=4, column=0,pady=5,ipadx=10)
              
              getRateview= ttk.Treeview(second)
              getRateview["columns"]=("1")
              getRateview.heading("#0",text="Country Code")
              getRateview.column("#0", width=100,minwidth=100, stretch=tk.NO)
              getRateview.heading("1",text="Forex Exchange Value")
              getRateview.column("1", width=150,minwidth=150, stretch=tk.NO)
              getRateview.grid(column=0, row=5,pady=5)
              
              Label_9 =Button(second, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=delete_multi)
              Label_9.grid(row=6, column=0, pady=5)
              
              
              
              #========== One To All Conversion Main GUI ==========#

              
              
              #+++++ One to all Conversion Window Execution +++++#
              
              center(second)
              second.mainloop()
              
              #+++++ One to all Conversion Window Execution +++++#
              
              
              #============= One to all Conversion Window =============#
              
       def third():
              
              def exit_third():
                     third.destroy()
                     curcon.deiconify()
              
              #============= Rate per Country Window =============#
              
              
              #+++++ Rate per Country Window Configuration +++++#
              
              third = tk.Toplevel(curcon)
              third.resizable(False,False)
              third.geometry("400x420")
              third.title("One to All Conversion")
              third.protocol("WM_DELETE_WINDOW", exit_third)
              
              #+++++ Rate per Country Window Configuration +++++#
              
              
              #+++++ Rate per Country Conversion Functions +++++#
              
              def delete_multi():
                     FromCurrency.set("currency")
                     getRateview.delete(*getRateview.get_children())

              def multicurrencyConversion():
                     a = 0

                     base = FromCurrency.get()

                     if(base == "currency"):
                            tkinter.messagebox.showwarning("Error !!", "Currency Not Selected.\n Please select a Currency form menu.")

                     else:
                            try:
                                   convert = c.convert(CurrencyCode_list[a-1], base,1)

                            except Exception as e:
                                   e = tkinter.messagebox.showerror("Error!!"," The Connection to the Internet is Lost!")
                            else:
                                   while a < 33:
                                          a = a + 1
                                          convert = c.convert(CurrencyCode_list[a-1], base,1)
                                          converted_amt = float("{:.2f}".format(convert))
                                          getRateview.insert("", a, text=CurrencyCode_list[a-1], values=converted_amt)

              
              #+++++ Rate per Country Conversion Functions +++++#
              
              
              #+++++ Rate per Country Conversion Logos +++++#
              
              thirdiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\globe.png").resize((50,50), Image.ANTIALIAS)
              thirdicon = ImageTk.PhotoImage(thirdiconimage)
              
              thirdimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\peso-icon.png")
              third.iconphoto(False,thirdimage)
              
              #+++++ Rate per Country Conversion Logos +++++#
              
              
              #========== Rate per Country Conversion Main GUI ==========#
              
              tk.Label(third,font=('lato black', 17,'bold'),text = ' Rates Per Country',fg='black',compound='left', image=thirdicon).grid(row=0, column=0,padx=70)
              
              
              label2 = tk.Label(third,font=('lato black', 13,'bold'), text = "Base Currency:  ", fg = "black") 
              label2.grid(row=3, column=0, padx=20, pady=5, sticky=W)
              
              FromCurrency = ttk.Combobox(third,state='readonly', values=CurrencyCode_list)
              FromCurrency.set("currency")
              FromCurrency.grid(column=0, row=3, padx=110, sticky=E)
              
              tk.Button(third, text = "Convert", font=('Century Gothic', 10, 'italic','bold'),fg='white',bg='navy',command=multicurrencyConversion).grid(row=4, column=0,pady=5,ipadx=10)
              
              getRateview= ttk.Treeview(third)
              getRateview["columns"]=("1")
              getRateview.heading("#0",text="Country Code")
              getRateview.column("#0", width=100,minwidth=100, stretch=tk.NO)
              getRateview.heading("1",text="Forex Exchange Value")
              getRateview.column("1", width=150,minwidth=150, stretch=tk.NO)
              getRateview.grid(column=0, row=5,pady=5)
              
              Label_9 =Button(third, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=delete_multi)
              Label_9.grid(row=6, column=0, pady=5)
              
       
              #========== Rate per Country Main GUI ==========#

              
              
              #+++++ Rate per Country Window Execution +++++#
              
              center(third)
              third.mainloop()
              
              #+++++ Rate per Country Window Execution +++++#
              
              
              #============= Rate per Country Conversion Window =============#
                   
       def fourth():
              
              def exit_fourth():
                     fourth.destroy()
                     curcon.deiconify()
       
              #=========== Bitcoin Conversion Window ===========#
              
              #+++++ Bitcoin Conversion Window Configuration +++++#
              
              curcon.withdraw()
              fourth = tk.Toplevel(curcon)
              fourth.resizable(False,False)
              fourth.geometry("400x380")
              fourth.title("Bitcoin Conversion")
              fourth.protocol("WM_DELETE_WINDOW", exit_fourth)
              
              #+++++ Bitcoin Conversion Window Configuration +++++#
              
              
              #+++++ Bitcoin Conversion Logos +++++#
              
              fourthiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\bitcoin.png").resize((50,50), Image.ANTIALIAS)
              fourthicon = ImageTk.PhotoImage(fourthiconimage)
              
              fourthimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\bitcoin.png")
              fourth.iconphoto(False,fourthimage)
              
              #+++++ Bitcoin Conversion Logos +++++#
              
              
              #======= Functions of Bitcoin Conversion ========#
              
              def clear_all(): 
                     
                     Amount2_field.configure(state=NORMAL) 
                     Amount2_field.delete(0, tk.END)
                     Amount_field.delete(0, tk.END)
                     Amount2_field.configure(state='readonly') 
                     FromCurrency_option.set("currency") 
                     
              def bitcoinconv(): 

                     from_currency = FromCurrency_option.get() 
                     amount = Amount_field.get()

                     if (from_currency=="currency"):
                            tkinter.messagebox.showwarning("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

                     elif(amount == ""):
                            tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

                     else:
                            try:
                                   b.get_latest_price(from_currency)

                            except Exception as e:
                                   e = tkinter.messagebox.showerror("Error!!"," The Connection to the Internet is Lost!")

                            else:
                                   Amount2_field.configure(state=NORMAL)
                                   Amount2_field.delete(0, tk.END)
                                   new_amt = float(b.get_latest_price(from_currency)*float(amount))
                                   new_amount = float("{:.2f}".format(new_amt))
                                   Amount2_field.insert(0, str(new_amount))
                                   Amount2_field.insert(0, str(from_currency + " "))
                                   Amount2_field.configure(state='readonly')
              
              
              #======= Functions of Bitcoin Conversion ========#
              
              
              #============== Bitcoin Conversion Main GUI =============#
              
              
              tk.Label(fourth,font=('lato black', 17,'bold'),text = ' Bitcoin Conversion',fg='black',compound='left', image=fourthicon).grid(row=0, column=0,padx=60)
              
              label1 = tk.Label(fourth,font=('lato black', 13,'bold'), text = "Bitcoin Amount:  ", fg = "black") 
              label1.grid(row=2, column=0, padx=20, pady=15, sticky=W)
              
              Amount_field = tk.Entry(fourth) 
              Amount_field.grid(row=2,column=0,padx=110,pady=15, sticky=E)
              
              label1 = tk.Label(fourth,font=('lato black', 13,'bold'), text = "To Target:  ", fg = "black") 
              label1.grid(row=3, column=0, padx=20, pady=15, sticky=W)
              
              FromCurrency_option = ttk.Combobox(fourth, value=CurrencyCode_list, state='readonly') 
              FromCurrency_option.set("currency") 
              FromCurrency_option.grid(row = 3, column=0, pady=15, padx=100, sticky=E)
              
              Label_9 =Button(fourth, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="green",fg = "white",command=bitcoinconv)
              Label_9.grid(row=4, column=0, padx=20, pady=15)
              
              label1 = tk.Label(fourth,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
              label1.grid(row=5, column=0, padx=20, pady=15, sticky=W)
              
              Amount2_field = tk.Entry(fourth,state='readonly')
              Amount2_field.grid(row=5,column=0,padx=85,pady=15, sticky=E)
              
              Label_9 =Button(fourth, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
              Label_9.grid(row=6, column=0, padx=20, pady=15)
              
              #============== Bitcoin Conversion Main GUI =============#
              
              
              #+++ Bitcoin Conversion Window Execution +++#
              
              center(fourth)
              fourth.mainloop()
              
              #+++ Bitcoin Conversion Window Execution +++#
              
              #=========== Bitcoin Conversion Window ===========#
              
       def exit_curcon():
              curcon.destroy()
              main.deiconify()
              
       #===== Currency Converter Window Configuration =====#
       
       main.withdraw()
       curcon = tk.Toplevel(main)      
       curcon.geometry("400x400")
       curcon.resizable(False,False)
       curcon.protocol("WM_DELETE_WINDOW", exit_curcon)
       
       #===== Currency Converter Window Configuration =====#
       
       
       #===== Currency Converter Menu Window =====#
       
       
       #+++ Icons for Currency Converter Window +++#
       
       curconiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\peso-icon.png").resize((40,40), Image.ANTIALIAS)
       curconicon = ImageTk.PhotoImage(curconiconimage)
       
       onetooneimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\1-to-1.png").resize((115,115), Image.ANTIALIAS)
       onetoone = ImageTk.PhotoImage(onetooneimage)
       
       onetoallimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\1-to-all.png").resize((115,115), Image.ANTIALIAS)
       onetoall = ImageTk.PhotoImage(onetoallimage)
       
       rates = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\globe.png").resize((115,115), Image.ANTIALIAS)
       rates = ImageTk.PhotoImage(rates)
       
       bitcoinimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\bitcoin.png").resize((115,115), Image.ANTIALIAS)
       bitcoin = ImageTk.PhotoImage(bitcoinimage)
       
       #+++ Icons for Currency Converter Window +++#
       
       
       #++++ Currency Converter Menu window Title ++++++#
       
       curcon.title("Currency Converter")
       iconimagecurcon = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\peso-icon.png")
       curcon.iconphoto(False,iconimagecurcon)
       
       #++++ Currency Converter Menu window Title ++++++#
       
       #=============== One To One Currency Converter Main GUI ================#

       
       #++++ Currency Converter Menu window Header ++++++#
       
       tk.Label(curcon, font=('Arial',20,'bold'), text = 'Currency Converter',fg='black', compound="left", image=curconicon).grid(row=1, column=0, padx=50, pady=5)
       
       #++++ Currency Converter Menu window Title ++++++#
       
       #+++ Button Selection +++#
       
       tk.Button(curcon, font=('Century Gothic', 11, 'bold'), text=' 1 to 1 Conversion ', compound=TOP ,bg='#2ED07BFFe',fg='white', image=onetoone, command=one).grid(row=3, column=0,padx=50,pady=10, sticky=W)
       tk.Button(curcon, font=('Century Gothic', 11, 'bold'), text='1 to all Conversion', compound=TOP ,bg='orange',fg='white', image=onetoall, command=second).grid(row=3, column=0,padx=50,pady=10, sticky=E)
       tk.Button(curcon, font=('Century Gothic', 11, 'bold'), text=' Rate per Country ', compound=TOP , bg='navy', fg='white', image=rates, command=third).grid(row=4, column=0,padx=50,pady=10, sticky=W)
       tk.Button(curcon, font=('Century Gothic', 11, 'bold'), text='Bitcoin Conversion', compound=TOP ,bg='green', fg='white',image=bitcoin, command=fourth).grid(row=4, column=0,padx=50,pady=10, sticky=E)
       
       #+++ Button Selection +++#
       
       
       #=============== One To One Currency Converter Main GUI ================#
       
       #===== Currency Converter Menu Window =====#
       
       
       #========= Currency Converter Menu Window Execution =============#
       
       center(curcon)
       curcon.mainloop()
       
      #========= Currency Converter Menu Window Execution =============#
      
#========= CURRENCY CONERTER ===========#


#========= LENGTH CONVERTER ===========#

def length():
       LengthUnit_list = ["mm", "cm", "dm", "m", "dam", "hm", "km", "Mm", "Gm", "Tm", "Pm", "Em", "Zm", "Ym", "inch", "foot", "yard", "mile", "furlong", "chain"]
       
       def exit_one():
              one.destroy()
              main.deiconify()
              
              
       #+++++ Length Converter Window Configuration +++++#
              
       main.withdraw()
       one = tk.Toplevel(main)
       one.resizable(False,False)
       one.geometry("400x400")
       one.title("One to One Conversion")
       one.protocol("WM_DELETE_WINDOW", exit_one)
              
       #+++++ Length Currency Converter Window Configuration +++++#
              
       #++++ Length Currency Converter Window Logos +++++#
              
       oneiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\length.png").resize((50,65), Image.ANTIALIAS)
       oneicon = ImageTk.PhotoImage(oneiconimage)
              
       oneimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\length.png")
       one.iconphoto(False,oneimage)
              
       #++++ Length Converter Window Logos +++++#
              
       #======= Functions of Length Conversion ========#
              
       def LengthConversion(): 
              
              from_length = FromLength_option.get() 
              to_length = ToLength_option.get()
              
              if (Amount1_field.get()==""):
                     tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

              elif (from_length=="Length Unit" or to_length=="Length Unit"):
                     tkinter.messagebox.showwarning("Error !!","Length Unit Not Selected.\n Please select FROM and TO Currency form menu.")

              else:
                     Amount2_field.configure(state=NORMAL)
                     Amount2_field.delete(0, tk.END)
                     #print(converts(str(Amount1_field.get())+" "+str(from_length),str(to_length)))
                     new_amt = converts(str(Amount1_field.get())+" "+str(from_length),str(to_length))
                     new_amount = float(new_amt)
                     Amount2_field.insert(0, str(" " + to_length))
                     Amount2_field.insert(0, str(new_amount))
                     Amount2_field.configure(state='readonly')

       def clear_all(): 
              Amount2_field.configure(state=NORMAL)
              Amount1_field.delete(0, tk.END) 
              Amount2_field.delete(0, tk.END)
              FromLength_option.set("Length Unit") 
              ToLength_option.set("Length Unit") 
              Amount2_field.configure(state='readonly')
             
               
              #======= Functions of Length Conversion ========#
              
       #=============== Length Converter Main GUI ================#
              
              
       tk.Label(one,font=('lato black', 17,'bold'),text = ' Length Coversion',fg='black',compound='left', image=oneicon).grid(row=0, column=0,padx=67)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
       label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
       label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
       label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
       label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)
       Label_1 =Label(one, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
       Label_1.grid(row=5, column=0,sticky=W)
       FromLength_option = ttk.Combobox(one, value=LengthUnit_list, state='readonly') 
       ToLength_option = ttk.Combobox(one, value=LengthUnit_list, state='readonly') 
       FromLength_option.set("Length Unit") 
       ToLength_option.set("Length Unit") 
       FromLength_option.grid(row = 3, column = 0) 
       ToLength_option.grid(row = 4, column = 0) 
       Amount1_field = tk.Entry(one) 
       Amount1_field.grid(row=2,column=0,padx=10,pady=10,)
       Amount2_field = tk.Entry(one,state='readonly')
       Amount2_field.grid(row=8,column=0,padx=80,pady=10, sticky=E) 
       
       tk.Label(one,text="").grid(row=7)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="grey",fg = "white",command=LengthConversion)
       Label_9.grid(row=6, column=0)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
       Label_9.grid(row=9, column=0)
       
       
       #=============== Length Converter Main GUI ================#
       
       
       
       
       #+++ Length Converter Window Execution +++#
       
       center(one)
       one.mainloop()
       
       #+++ Length Converter Window Execution +++#
       
       #========= Length Converter Window =========#
       
#========= LENGTH CONVERTER ===========#


#========= WEIGHT CONVERTER =========#

def weight():
       weighthUnit_list = ["mg", "cg", "dg", "g", "dag", "hg", "kg", "Mg", "Gg", "Tg", "Pg", "Eg", "Zg", "Yg"]
       
       def exit_one():
              one.destroy()
              main.deiconify()
              
              
       #+++++ weight Converter Window Configuration +++++#
              
       main.withdraw()
       one = tk.Toplevel(main)
       one.resizable(False,False)
       one.geometry("400x400")
       one.title("Weight Conversion")
       one.protocol("WM_DELETE_WINDOW", exit_one)
              
       #+++++ weight Currency Converter Window Configuration +++++#
              
       #++++ weight Currency Converter Window Logos +++++#
              
       oneiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\ws.png").resize((50,65), Image.ANTIALIAS)
       oneicon = ImageTk.PhotoImage(oneiconimage)
              
       oneimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\ws.png")
       one.iconphoto(False,oneimage)
              
       #++++ weight Converter Window Logos +++++#
              
       #======= Functions of weight Conversion ========#
              
       def weightConversion(): 
              
              from_weight = Fromweight_option.get() 
              to_weight = Toweight_option.get()
              
              if (Amount1_field.get()==""):
                     tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

              elif (from_weight=="weight unit" or to_weight=="weight unit"):
                     tkinter.messagebox.showwarning("Error !!","Weight Unit Not Selected.\n Please select FROM and TO Currency form menu.")

              else:
                     Amount2_field.configure(state=NORMAL)
                     Amount2_field.delete(0, tk.END)
                     new_amt = converts(str(Amount1_field.get())+" "+str(from_weight),str(to_weight))
                     new_amount = float(new_amt)
                     Amount2_field.insert(0, str(" " + to_weight))
                     Amount2_field.insert(0, str(new_amount))
                     Amount2_field.configure(state='readonly')

       def clear_all(): 
              Amount2_field.configure(state=NORMAL)
              Amount1_field.delete(0, tk.END) 
              Amount2_field.delete(0, tk.END)
              Fromweight_option.set("weight unit") 
              Toweight_option.set("weight unit") 
              Amount2_field.configure(state='readonly')
             
               
              #======= Functions of weight Conversion ========#
              
       #=============== weight Converter Main GUI ================#
              
              
       tk.Label(one,font=('lato black', 17,'bold'),text = ' Weight Coversion',fg='black',compound='left', image=oneicon).grid(row=0, column=0,padx=67)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
       label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
       label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
       label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
       label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)
       Label_1 =Label(one, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
       Label_1.grid(row=5, column=0,sticky=W)
       Fromweight_option = ttk.Combobox(one, value=weighthUnit_list, state='readonly') 
       Toweight_option = ttk.Combobox(one, value=weighthUnit_list, state='readonly') 
       Fromweight_option.set("Weight Unit") 
       Toweight_option.set("Weight Unit") 
       Fromweight_option.grid(row = 3, column = 0) 
       Toweight_option.grid(row = 4, column = 0) 
       Amount1_field = tk.Entry(one) 
       Amount1_field.grid(row=2,column=0,padx=10,pady=10,)
       Amount2_field = tk.Entry(one,state='readonly')
       Amount2_field.grid(row=8,column=0,padx=80,pady=10, sticky=E) 
       
       tk.Label(one,text="").grid(row=7)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="white",fg = "black",command=weightConversion)
       Label_9.grid(row=6, column=0)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
       Label_9.grid(row=9, column=0)
       
       
       #=============== Length Converter Main GUI ================#
       
       
       
       
       #+++ Length Converter Window Execution +++#
       
       center(one)
       one.mainloop()
       
       #+++ Length Converter Window Execution +++#
       
       #========= Length Converter Window =========#
       
#========= WEIGHT CONVERTER ===========#


#========= TEMPERATURE CONVERTER =========#

def temp():
       TemperatureUnit_list = ["°C", "°F"]
       
       def exit_one():
              one.destroy()
              main.deiconify()
              
              
       #+++++ Temperature Converter Window Configuration +++++#
              
       main.withdraw()
       one = tk.Toplevel(main)
       one.resizable(False,False)
       one.geometry("400x400")
       one.title("Temperature Conversion")
       one.protocol("WM_DELETE_WINDOW", exit_one)
              
       #+++++ Temperature Currency Converter Window Configuration +++++#
              
       #++++ Temperature Currency Converter Window Logos +++++#
              
       oneiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\thermo.png").resize((50,50), Image.ANTIALIAS)
       oneicon = ImageTk.PhotoImage(oneiconimage)
              
       oneimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\thermo.png")
       one.iconphoto(False,oneimage)
              
       #++++ Temperature Converter Window Logos +++++#
              
       #======= Functions of Temperature Conversion ========#
              
       def TemperatureConversion(): 
              
              from_Temperature = FromTemperature_option.get() 
              to_Temperature = ToTemperature_option.get()
              
              if (Amount1_field.get()==""):
                     tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

              elif (from_Temperature=="Temperature unit" or to_Temperature=="Temperature unit"):
                     tkinter.messagebox.showwarning("Error !!","Temperature Unit Not Selected.\n Please select FROM and TO Currency form menu.")

              else:
                     Amount2_field.configure(state=NORMAL)
                     Amount2_field.delete(0, tk.END)
                     new_amt = converts(str(Amount1_field.get())+" "+str(from_Temperature),str(to_Temperature))
                     new_amount = float(new_amt)
                     Amount2_field.insert(0, str(" " + to_Temperature))
                     Amount2_field.insert(0, str(new_amount))
                     Amount2_field.configure(state='readonly')

       def clear_all(): 
              Amount2_field.configure(state=NORMAL)
              Amount1_field.delete(0, tk.END) 
              Amount2_field.delete(0, tk.END)
              FromTemperature_option.set("Temperature unit") 
              ToTemperature_option.set("Temperature unit") 
              Amount2_field.configure(state='readonly')
             
               
              #======= Functions of Temperature Conversion ========#
              
       #=============== Temperature Converter Main GUI ================#
              
              
       tk.Label(one,font=('lato black', 17,'bold'),text = ' Temperature Coversion',fg='black',compound='left', image=oneicon).grid(row=0, column=0,padx=37)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
       label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
       label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
       label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
       label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)
       Label_1 =Label(one, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
       Label_1.grid(row=5, column=0,sticky=W)
       FromTemperature_option = ttk.Combobox(one, value=TemperatureUnit_list, state='readonly') 
       ToTemperature_option = ttk.Combobox(one, value=TemperatureUnit_list, state='readonly') 
       FromTemperature_option.set("Temperature Unit") 
       ToTemperature_option.set("Temperature Unit") 
       FromTemperature_option.grid(row = 3, column = 0) 
       ToTemperature_option.grid(row = 4, column = 0) 
       Amount1_field = tk.Entry(one) 
       Amount1_field.grid(row=2,column=0,padx=10,pady=10,)
       Amount2_field = tk.Entry(one,state='readonly')
       Amount2_field.grid(row=8,column=0,padx=80,pady=10, sticky=E) 
       
       tk.Label(one,text="").grid(row=7)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="#D7650F",fg = "white",command=TemperatureConversion)
       Label_9.grid(row=6, column=0)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
       Label_9.grid(row=9, column=0)
       
       
       #=============== Temperature Converter Main GUI ================#
       
       
       
       
       #+++ Temperature Converter Window Execution +++#
       
       center(one)
       one.mainloop()
       
       #+++ Temperature Converter Window Execution +++#
       
       #========= Temperature Converter Window =========#       

#========= TEMPERATURE CONVERTER =========#


#========= ELECTRICITY CONVERTER =========#

def elec():
       ElectricityUnit_list = ["mW", "cW", "dW", "W", "daW", "hW", "kW", "MW", "GW", "TW", "PW", "EW", "ZW", "YW"]
       
       def exit_one():
              one.destroy()
              main.deiconify()
              
              
       #+++++ Electricity Converter Window Configuration +++++#
              
       main.withdraw()
       one = tk.Toplevel(main)
       one.resizable(False,False)
       one.geometry("400x400")
       one.title("Temperature Conversion")
       one.protocol("WM_DELETE_WINDOW", exit_one)
              
       #+++++ Electricity Currency Converter Window Configuration +++++#
              
       #++++ Electricity Currency Converter Window Logos +++++#
              
       oneiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\thunder.png").resize((50,50), Image.ANTIALIAS)
       oneicon = ImageTk.PhotoImage(oneiconimage)
              
       oneimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\thunder.png")
       one.iconphoto(False,oneimage)
              
       #++++ Electricity Converter Window Logos +++++#
              
       #======= Functions of Temperature Conversion ========#
              
       def ElectricityConversion(): 
              
              from_Electricity = FromElectricity_option.get() 
              to_Electricity = ToElectricity_option.get()
              
              if (Amount1_field.get()==""):
                     tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

              elif (from_Electricity=="Electricity unit" or to_Electricity=="Electricity unit"):
                     tkinter.messagebox.showwarning("Error !!","Electricity Unit Not Selected.\n Please select FROM and TO Currency form menu.")

              else:
                     Amount2_field.configure(state=NORMAL)
                     Amount2_field.delete(0, tk.END)
                     new_amt = converts(str(Amount1_field.get())+" "+str(from_Electricity),str(to_Electricity))
                     new_amount = float(new_amt)
                     Amount2_field.insert(0, str(" " + to_Electricity))
                     Amount2_field.insert(0, str(new_amount))
                     Amount2_field.configure(state='readonly')

       def clear_all(): 
              Amount2_field.configure(state=NORMAL)
              Amount1_field.delete(0, tk.END) 
              Amount2_field.delete(0, tk.END)
              FromElectricity_option.set("Electricity unit") 
              ToElectricity_option.set("Electricity unit") 
              Amount2_field.configure(state='readonly')
             
               
              #======= Functions of Electricity Conversion ========#
              
       #=============== Electricity Converter Main GUI ================#
              
              
       tk.Label(one,font=('lato black', 17,'bold'),text = ' Electricity Coversion',fg='black',compound='left', image=oneicon).grid(row=0, column=0,padx=47)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
       label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
       label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
       label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
       label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)
       Label_1 =Label(one, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
       Label_1.grid(row=5, column=0,sticky=W)
       FromElectricity_option = ttk.Combobox(one, value=ElectricityUnit_list, state='readonly') 
       ToElectricity_option = ttk.Combobox(one, value=ElectricityUnit_list, state='readonly') 
       FromElectricity_option.set("Electricity Unit") 
       ToElectricity_option.set("Electricity Unit") 
       FromElectricity_option.grid(row = 3, column = 0) 
       ToElectricity_option.grid(row = 4, column = 0) 
       Amount1_field = tk.Entry(one) 
       Amount1_field.grid(row=2,column=0,padx=10,pady=10,)
       Amount2_field = tk.Entry(one,state='readonly')
       Amount2_field.grid(row=8,column=0,padx=80,pady=10, sticky=E) 
       
       tk.Label(one,text="").grid(row=7)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="#59D5D7",fg = "white",command=ElectricityConversion)
       Label_9.grid(row=6, column=0)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
       Label_9.grid(row=9, column=0)
       
       
       #=============== Electricity Converter Main GUI ================#
       
       
       #+++ Electricity Converter Window Execution +++#
       
       center(one)
       one.mainloop()
       
       #+++ Electricity Converter Window Execution +++#
       
       #========= Electricity Converter Window =========#
       
#========= ELECTRICITY CONVERTER =========# 


#========= TIME CONVERTER =========# 

def time():
       TimeUnit_list = ["ms", "cs", "ds", "s", "das", "hs", "ks", "Ms", "Gs", "Ts", "Ps", "Es", "Zs", "Ys","min",'h']
       
       def exit_one():
              one.destroy()
              main.deiconify()
              
              
       #+++++ Electricity Converter Window Configuration +++++#
              
       main.withdraw()
       one = tk.Toplevel(main)
       one.resizable(False,False)
       one.geometry("400x400")
       one.title("Time Conversion")
       one.protocol("WM_DELETE_WINDOW", exit_one)
              
       #+++++ Electricity Currency Converter Window Configuration +++++#
              
       #++++ Electricity Currency Converter Window Logos +++++#
              
       oneiconimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\timer.png").resize((50,50), Image.ANTIALIAS)
       oneicon = ImageTk.PhotoImage(oneiconimage)
              
       oneimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\timer.png")
       one.iconphoto(False,oneimage)
              
       #++++ Electricity Converter Window Logos +++++#
              
       #======= Functions of Temperature Conversion ========#
              
       def TimeConversion(): 
              
              from_Time = FromTime_option.get() 
              to_Time = ToTime_option.get()
              
              if (Amount1_field.get()==""):
                     tkinter.messagebox.showwarning("Error !!","Amount Not Entered.\n Please a valid amount.")

              elif (from_Time=="Time unit" or to_Time=="Time unit"):
                     tkinter.messagebox.showwarning("Error !!","Time Unit Not Selected.\n Please select FROM and TO Currency form menu.")

              else:
                     Amount2_field.configure(state=NORMAL)
                     Amount2_field.delete(0, tk.END)
                     new_amt = converts(str(Amount1_field.get())+" "+str(from_Time),str(to_Time))
                     new_amount = float(new_amt)
                     Amount2_field.insert(0, str(" " + to_Time))
                     Amount2_field.insert(0, str(new_amount))
                     Amount2_field.configure(state='readonly')

       def clear_all(): 
              Amount2_field.configure(state=NORMAL)
              Amount1_field.delete(0, tk.END) 
              Amount2_field.delete(0, tk.END)
              FromTime_option.set("Time unit") 
              ToTime_option.set("Time unit") 
              Amount2_field.configure(state='readonly')
             
               
              #======= Functions of Time Conversion ========#
              
       #=============== Time Converter Main GUI ================#
              
              
       tk.Label(one,font=('lato black', 17,'bold'),text = ' Time Coversion',fg='black',compound='left', image=oneicon).grid(row=0, column=0,padx=77)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
       label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
       label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
       label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)
       label1 = tk.Label(one,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
       label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)
       Label_1 =Label(one, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
       Label_1.grid(row=5, column=0,sticky=W)
       FromTime_option = ttk.Combobox(one, value=TimeUnit_list, state='readonly') 
       ToTime_option = ttk.Combobox(one, value=TimeUnit_list, state='readonly') 
       FromTime_option.set("Time Unit") 
       ToTime_option.set("Time Unit") 
       FromTime_option.grid(row = 3, column = 0) 
       ToTime_option.grid(row = 4, column = 0) 
       Amount1_field = tk.Entry(one) 
       Amount1_field.grid(row=2,column=0,padx=10,pady=10,)
       Amount2_field = tk.Entry(one,state='readonly')
       Amount2_field.grid(row=8,column=0,padx=80,pady=10, sticky=E) 
       
       tk.Label(one,text="").grid(row=7)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="#D71C9B",fg = "white",command=TimeConversion)
       Label_9.grid(row=6, column=0)
       Label_9 =Button(one, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
       Label_9.grid(row=9, column=0)
       
       
       #=============== Time Converter Main GUI ================#
       
       
       #+++ Time Converter Window Execution +++#
       
       center(one)
       one.mainloop()
       
       #+++ Time Converter Window Execution +++#
       
       #========= Time Converter Window =========#

#========= TIME CONVERTER =========#     
  
  
#=============== MAIN MENU ================#


#+++ Main window initializer +++#

main = tk.Tk()

#+++ Main window initializer +++#


#+++ Frame Set-up +++#

main.geometry("400x400")
main.resizable(False,False)

#+++ Frame Set-up +++#


#+++ Logos +++#

iconimage = PhotoImage(file = "D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\scale.png")
main.iconphoto(False,iconimage)

logoimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\scale.png").resize((40,30), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logoimage)

pesoimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\peso.png").resize((100,100), Image.ANTIALIAS)
peso = ImageTk.PhotoImage(pesoimage)

rulerimage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\length.png").resize((100,100), Image.ANTIALIAS)
ruler = ImageTk.PhotoImage(rulerimage)

weightingscaleImage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\ws.png").resize((100,100), Image.ANTIALIAS)
weightingscale = ImageTk.PhotoImage(weightingscaleImage)

thermoImage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\thermo.png").resize((100,100), Image.ANTIALIAS)
thermo = ImageTk.PhotoImage(thermoImage)

electricityImage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\thunder.png").resize((100,100), Image.ANTIALIAS)
electricity = ImageTk.PhotoImage(electricityImage)

timerImage = Image.open("D:\\Justin's Files\\Documents\\python projects\\Python Converter\\images\\timer.png").resize((100,100), Image.ANTIALIAS)
timer = ImageTk.PhotoImage(timerImage)

#+++ Logos +++#


#+++ Title +++#

main.title("Python Converter Program")

#+++ Title +++#


#+++ Header Title +++#

tk.Label(main, font=('Century Gothic',17,'bold'),text = ' Python Converter Program', fg='black',compound="left", image=logo).grid(row=2, column=0, padx=24)

#+++ Header Title +++#


#+++ Button Selection +++#

tk.Button(main, font=('Century Gothic', 10, 'bold'), text='Currency', compound=BOTTOM , bg='#2ED07BFFe',fg='white', image=peso, command=CurrencyConverter).grid(row=3, column=0,padx=30,pady=20, sticky=W)
tk.Button(main, font=('Century Gothic', 10, 'bold'), text='Length', compound=BOTTOM , bg='grey',fg='white', image=ruler, command = length).grid(row=3, column=0,padx=30,pady=20)
tk.Button(main, font=('Century Gothic', 10, 'bold'), text='Weight', compound=BOTTOM , bg='white',fg='black', image=weightingscale, command = weight).grid(row=3, column=0,padx=30,pady=10, sticky=E)
tk.Button(main, font=('Century Gothic', 10, 'bold'), text='Temperature', compound=BOTTOM , bg='#D7650F',fg='white', image=thermo, command = temp).grid(row=5, column=0,padx=30,pady=10, sticky=W)
tk.Button(main, font=('Century Gothic', 10, 'bold'), text='Electricity', compound=BOTTOM , bg='#59D5D7',fg='white', image=electricity, command = elec).grid(row=5, column=0,padx=30,pady=10)
tk.Button(main, font=('Century Gothic', 10, 'bold'), text='Time', compound=BOTTOM , bg='#D71C9B',fg='white', image=timer, command = time).grid(row=5, column=0,padx=30,pady=10, sticky=E)

#+++ Button Selection +++#


#+++ Window Execution +++#

center(main)
main.mainloop()

#+++ Window Execution +++#

#=============== MAIN MENU CONFIGURATION ================#