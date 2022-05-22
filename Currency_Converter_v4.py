# Import required modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import requests
import datetime as dt

# Program to convert a given amount to another currency with real-time data for rates
class CurrencyConverter:

    def __init__(self, url):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')

        #Convert()-method: Base-currency set as CHF, convert the amount into CHF, cross multiplication between the amount and the rate
    def convert(self, amount, base_currency, des_currency):
        if base_currency != 'CHF':
            amount = amount/self.rates[base_currency]

        # Limiting the result to 3 decimal places
        amount = round(amount*self.rates[des_currency], 3)
        # Add comma every 3 numbers
        amount = '{:,}'.format(amount)
        return amount

# Main window
class Main(tk.Tk):

    def __init__(self, converter):

        # Create frame with title 'Currency Converter'
        tk.Tk.__init__(self)
        self.title('Currency Converter by MoneyCounters')
        self.geometry('400x550')
        self.config(bg='green')
        self.CurrencyConverter = converter
        font = ("calibri")

        # Create title label
        self.title_label = Label(self, text='Currency Converter by MoneyCounters', bg='green', fg='white', font=(font, 20, "bold"), width=33, height=3, relief='ridge')

        # Create date label
        self.date_label = Label(self, text="Rates as of:\n" + f'{dt.datetime.now():%A, %B %d, %Y, %H : %M : %S}', bg='green', fg='white', font=(font, 12))

        # Create amount label
        self.amount_label = Label(self, text='Convert Amount: ', bg='green', fg='white', font=(font, 15))

        # Create amount entry box
        self.amount_entry = Entry(self)
        self.amount_entry.config(width=15)

        # Create 'from' label
        self.base_currency_label = Label(self, text='From Currency: ', bg='green', fg='white', font=(font, 15))

        # Create 'to' label
        self.destination_currency_label = Label(self, text='To Currency: ', bg='green', fg='white', font=(font, 15))

        # Create dropdown menus
        self.currency_variable1 = StringVar(self)
        self.currency_variable2 = StringVar(self)
        self.currency_variable1.set('CHF')
        self.currency_variable2.set('USD')

        self.currency_combobox1 = ttk.Combobox(self, width=10, textvariable=self.currency_variable1, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox2 = ttk.Combobox(self, width=10, textvariable=self.currency_variable2, values=list(self.CurrencyConverter.rates.keys()), state='readonly')

        # Create 'convert' button
        self.convert_button = Button(self, text='Convert', fg='black', width=7, command=self.processed)

        # Create converted result field
        self.final_result = Label(self, text='', bg='white', fg='green', font=(font, 15, "bold"), relief='sunken', width=35, height=2)

        # Create 'clear' button
        self.clear_button = Button(self, text='Clear All', fg='black',width=7, command=self.clear)

        #Placing, sorted by y-axis, of labels, entry box, dropdown menu, buttons, field
        self.title_label.place(x=200, y=26, anchor='center')
        self.date_label.place(x=200, y=100, anchor='center')
        self.amount_label.place(x=200, y=150, anchor='center')
        self.amount_entry.place(x=200, y=180, anchor='center')
        self.base_currency_label.place(x=125, y=220, anchor='center')
        self.destination_currency_label.place(x=275, y=220, anchor='center')
        self.currency_combobox1.place(x=125, y=250, anchor='center')
        self.currency_combobox2.place(x=275, y=250, anchor='center')
        self.convert_button.place(x=200, y=300, anchor='center')
        self.final_result.place(x=200, y=350, anchor='center')
        self.clear_button.place(x=200, y=400, anchor='center')




    # Create clear function, to clear the amount field and final result field
    def clear(self):
        clear_entry = self.amount_entry.delete(0, END)
        clear_result = self.final_result.config(text='')
        return clear_entry, clear_result

    # Create a function to perform
    def processed(self):
        try:
            given_amount = float(self.amount_entry.get())
            given_base_currency = self.currency_variable1.get()
            given_des_currency = self.currency_variable2.get()
            converted_amount = self.CurrencyConverter.convert(given_amount, given_base_currency, given_des_currency)
            # Add comma every 3 numbers
            given_amount = '{:,}'.format(given_amount)

            self.final_result.config(text=f'{given_amount} {given_base_currency} = {converted_amount} {given_des_currency}')

        # Create warning message box
        except ValueError:
            convert_error = messagebox.showwarning('WARNING!', 'Please Fill the Amount Field (integer only)!')
            return convert_error


if __name__ == '__main__':
    converter = CurrencyConverter('https://api.exchangerate.host/latest')
    Main(converter)
    mainloop()
