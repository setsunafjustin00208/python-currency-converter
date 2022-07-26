import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
c = CurrencyRates()
b = BtcConverter()

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
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

def root():
	main.withdraw()
	root = tk.Toplevel(main)
	root.resizable(False,False)
	root.geometry("400x420")
	

	root.title("Real Time Currency Converter Improved")

	Tops = Frame(root,bg = 'blue',pady = 5, width =1550, height = 50)
	Tops.grid(row=0,column=0)


	headlabel = tk.Label(Tops,font=('lato black', 15,'bold'),text = 'One On One Conversion', bg= 'blue',fg='white',compound='left') 
	headlabel.grid(row=1, column=0,padx=55)

		 
	

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

	def exitroot():
		root.destroy()
		main.deiconify()

	root.protocol("WM_DELETE_WINDOW", exitroot)
	CurrencyCode_list = ["PHP", "USD", "EUR", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "SGD", "THB", "ZAR"]

	label1 = tk.Label(root,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
	label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)

	label1 = tk.Label(root,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
	label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)

	label1 = tk.Label(root,font=('lato black', 13,'bold'), text = "To:  ", fg = "black") 
	label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)

	label1 = tk.Label(root,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
	label1.grid(row=8, column=0, padx=20, pady=12, sticky=W)


	Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
	Label_1.grid(row=5, column=0,sticky=W)



	FromCurrency_option = ttk.Combobox(root, value=CurrencyCode_list, state='readonly') 
	ToCurrency_option = ttk.Combobox(root, value=CurrencyCode_list, state='readonly') 

	FromCurrency_option.set("currency") 
	ToCurrency_option.set("currency") 

	FromCurrency_option.grid(row = 3, column = 0) 
	ToCurrency_option.grid(row = 4, column = 0) 


	Amount1_field = tk.Entry(root) 
	Amount1_field.grid(row=2,column=0,padx=20,pady=10,)

	Amount2_field = tk.Entry(root,state='readonly')
	Amount2_field.grid(row=8,column=0,padx=90,pady=10, sticky=E) 
	

	tk.Label(root,text="").grid(row=7)


	Label_9 =Button(root, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="blue",fg = "white",command=RealTimeCurrencyConversion)
	Label_9.grid(row=6, column=0)

	Label_9 =Button(root, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
	Label_9.grid(row=9, column=0)

	center(root)
	root.mainloop()
	

def second():
	main.withdraw()
	second = tk.Toplevel(main)
	second.resizable(False,False)
	second.geometry("400x440")
	CurrencyCode_list = ["PHP", "USD", "EUR", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "SGD", "THB", "ZAR"]

	def exit_second():
		second.destroy()
		main.deiconify()

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

				

	second.protocol("WM_DELETE_WINDOW", exit_second)
	Tops = tk.Frame(second,bg = 'orange',pady = 5, width =1550, height = 50)
	Tops.grid(row=0,column=0)

	headlabel = tk.Label(Tops,font=('lato black', 15,'bold'),text = 'One to All Conversion', bg= 'orange',fg='white') 
	headlabel.grid(row=0, column=0,padx=95)

	label1 = tk.Label(second,font=('lato black', 13,'bold'), text = "Amount:  ", fg = "black") 
	label1.grid(row=2, column=0, padx=10, pady=12, sticky=W)

	Amount_field = tk.Entry(second) 
	Amount_field.grid(row=2,column=0,pady=1)

	FromCurrency = ttk.Combobox(second,state='readonly', values=CurrencyCode_list)
	FromCurrency.set("currency")
	FromCurrency.grid(column=0, row=3)
	tk.Button(second, text = "Convert", font=('Century Gothic', 10, 'italic','bold'),fg='white',bg='orange',command=multicurrencyConversion).grid(row=4, column=0,pady=10,ipadx=10)
	getRateview= ttk.Treeview(second)
	getRateview["columns"]=("1")
	getRateview.heading("#0",text="Country Code")
	getRateview.column("#0", width=100,minwidth=100, stretch=tk.NO)
	getRateview.heading("1",text="Forex Exchange Value")
	getRateview.column("1", width=150,minwidth=150, stretch=tk.NO)
	getRateview.grid(column=0, row=5)
	Label_9 =Button(second, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=delete_multi)
	Label_9.grid(row=6, column=0, pady=5)

	center(second)



def third():
	main.withdraw()
	third = tk.Toplevel(main)
	third.resizable(True,False)
	third.geometry("400x420")
	CurrencyCode_list = ["PHP", "USD", "EUR", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "SGD", "THB", "ZAR"]
	

	

	def exit_third():
		third.destroy()
		main.deiconify()

	def delete_current():
		FromCurrency.set("currency")
		getRateview.delete(*getRateview.get_children())

	def getRates():
		a = 0

		base = FromCurrency.get()

		if(base == "currency"):
			tkinter.messagebox.showwarning("Error !!", "Currency Not Selected.\n Please select a Currency form menu.")

		else:
			try:
				convert = c.convert(CurrencyCode_list[a-1], base, 1)

			except Exception as e:
				e = tkinter.messagebox.showerror("Error!!"," The Connection to the Internet is Lost!")			
			else:
				while a < 33:
					a = a + 1
					convert = c.convert(CurrencyCode_list[a-1],base, 1)
					converted_amt = float("{:.2f}".format(convert))
					getRateview.insert("", a,text=CurrencyCode_list[a-1], values=converted_amt)
			

	third.protocol("WM_DELETE_WINDOW", exit_third)
	

	Tops = tk.Frame(third,bg = 'navy',pady = 5, width =1550, height = 50)
	Tops.grid(row=0,column=0)

	headlabel = tk.Label(Tops,font=('lato black', 15,'bold'),text = 'Rates Per Country', bg= 'navy',fg='white',) 
	headlabel.grid(row=1, column=0,padx=110)

	label1 = tk.Label(third,font=('lato black', 11,'bold'), text = "Base Currency:  ", fg = "black") 
	label1.grid(row=2, column=0, padx=20, pady=12, sticky=W)


	FromCurrency = ttk.Combobox(third,state='readonly', values=CurrencyCode_list)
	FromCurrency.set("currency")
	FromCurrency.grid(column=0, row=2,sticky=E,padx=120)

	

	tk.Button(third, text = "Get Rates", font=('Century Gothic', 10, 'italic','bold'),fg='white',bg='navy',command=getRates).grid(row=3, column=0,pady=10,ipadx=10)
	getRateview= ttk.Treeview(third)
	getRateview["columns"]=("1")
	getRateview.heading("#0",text="Country Code")
	getRateview.column("#0", width=100,minwidth=100, stretch=tk.NO)
	getRateview.heading("1",text="Forex Exchange Value")
	getRateview.column("1", width=150,minwidth=150, stretch=tk.NO)
	getRateview.grid(column=0, row=4)
	Label_9 =Button(third, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=delete_current)
	Label_9.grid(row=5, column=0, pady=5)

	center(third)

def fourth():
	main.withdraw()
	fourth = tk.Toplevel(main)
	fourth.resizable(False,False)
	fourth.geometry("400x350")
	

	fourth.title("Real Time Currency Converter Improved")

	Tops = Frame(fourth,bg = 'green',pady = 5, width =1550, height = 50)
	Tops.grid(row=0,column=0)

	headlabel = tk.Label(Tops,font=('lato black', 15,'bold'),text = 'Bit Coin conversion', bg= 'green',fg='white',compound='left') 
	headlabel.grid(row=1, column=0,padx=75)

		 
	

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

	def clear_all(): 
		Amount2_field.configure(state=NORMAL) 
		Amount2_field.delete(0, tk.END)
		Amount_field.delete(0, tk.END)
		Amount2_field.configure(state='readonly') 
		FromCurrency_option.set("currency") 
		

	def exitfourth():
		fourth.destroy()
		main.deiconify()

	fourth.protocol("WM_DELETE_WINDOW", exitfourth)
	CurrencyCode_list = ["PHP", "USD", "EUR", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "SGD", "THB", "ZAR"]

	
	label1 = tk.Label(fourth,font=('lato black', 13,'bold'), text = "Bitcoin amount:  ", fg = "black") 
	label1.grid(row=3, column=0, padx=20, pady=12, sticky=W)

	label1 = tk.Label(fourth,font=('lato black', 13,'bold'), text = "From:  ", fg = "black") 
	label1.grid(row=4, column=0, padx=20, pady=12, sticky=W)


	label1 = tk.Label(fourth,font=('lato black', 13,'bold'), text = "Converted Amount:  ", fg = "black") 
	label1.grid(row=5, column=0, padx=20, pady=12, sticky=W)


	Label_1 =Label(fourth, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
	Label_1.grid(row=5, column=0,sticky=W)


	Amount_field = tk.Entry(fourth)
	Amount_field.grid(row=3,column=0,padx=90,pady=10, sticky=E) 


	FromCurrency_option = ttk.Combobox(fourth, value=CurrencyCode_list, state='readonly') 
	

	FromCurrency_option.set("currency") 
	FromCurrency_option.grid(row = 4, column=0)
	
	Amount2_field = tk.Entry(fourth,state='readonly')
	Amount2_field.grid(row=5,column=0,padx=90,pady=10, sticky=E) 
	

	tk.Label(fourth,text="").grid(row=7)


	Label_9 =Button(fourth, font=('arial', 13,'bold'), text="Convert",padx=2,pady=2, bg="green",fg = "white",command=bitcoinconv)
	Label_9.grid(row=6, column=0)

	Label_9 =Button(fourth, font=('arial', 13,'bold'), text="Clear All",padx=2,pady=2, bg="white",fg = "red",command=clear_all)
	Label_9.grid(row=9, column=0)

	center(fourth)
	fourth.mainloop()


main = tk.Tk()
# ====Frame Set-up ==== #

main.geometry("400x350")
main.resizable(False,False)

# ==== End of Frame Set-up ==== #

# ==== Title === #


main.title("Real Time Currency Converter Improved")

# ==== End Title === #

# === Header === #

tk.Label(main, font=('Arial',12,'bold'),text = 'Real Time Currency Converter Improved',fg='black', compound="left").grid(row=1, column=0, padx=13)

# === End Of Header === #

# === Button Options === #

tk.Button(main, font=('Century Gothic', 15), text='One to one Conversion', bg='#2ED07BFFe',fg='white',command=root).grid(row=3, column=0,padx=10,pady=10)
tk.Button(main, font=('Century Gothic', 15), text='One to all Conversion', bg='orange',fg='white', command=second).grid(row=4, column=0,padx=10,pady=10)
tk.Button(main, font=('Century Gothic', 15), text='Rates per Country',bg='navy', fg='white', command=third).grid(row=5, column=0,padx=10,pady=10)
tk.Button(main, font=('Century Gothic', 15), text='Crypto Currency',bg='green', fg='white', command=fourth).grid(row=6, column=0,padx=10,pady=10)

# ============= #

# Frame Execution
center(main)
main.mainloop()

# ============= #
