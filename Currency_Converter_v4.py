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
        self.title_label = Label(self, text='Currency Converter by MoneyCounters', bg='green', fg='white', font=(font, 18, "bold"), width=33, height=3, relief='ridge')

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
        
        # Create 'help' button for abbreviations of currency symbols
        #First, create new window that displays the abbreviations
        def help():
            newwin = Tk()
            newwin.title("Reference")
            newwin.maxsize(400,300)
            newwin.minsize(400,300)
            newcanvas = Canvas(newwin, height = 400, width = 300)
            newcanvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
            newframe = Frame(newwin, bg ="green")
            newframe.place(relwidth = 1, relheight = 1)
            newlabel = Label(newframe, fg ="green", anchor = "nw", justify = "left", bd =4)
            newlabel.place(relx = 0.05, rely = 0.05,relwidth = 0.90, relheight = 0.90)            

            # Create the text widget
            text_widget = tk.Text(newlabel, height=200, width=100)

            # Pack it into our tkinter application
            text_widget.pack()

            # Insert explanations of currency symbols into the text widget
           
            text_widget.insert(tk.END,"""ABBREVIATIONS:

AED - United Arab Emirates Dirham
AFN - Afghan Afghani
ALL - Albanian Lek
AMD - Armenian Dram
ANG - Netherlands Antillean Guilder
AOA - Angolan Kwanza
ARS - Argentine Peso
AUD - Australian Dollar
AWG - Aruban Florin
AZN - Azerbaijani Manat
BAM - Bosnia -Herzegovina Convertible Mark
BBD - Barbadian Dollar
BDT - Bangladeshi Taka
BGN - Bulgarian Lev
BHD - Bahraini Dinar
BIF - Burundian Franc
BMD - Bermudan Dollar
BND - Brunei Dollar
BOB - Bolivian Boliviano
BRL - Brazilian Real
BSD - Bahamian Dollar
BTC - Bitcoin
BTN - Bhutanese Ngultrum
BWP - Botswanan Pula
BYN - Belarusian Ruble
BZD - Belize Dollar
CAD - Canadian Dollar
CDF - Congolese Franc
CHF - Swiss Franc
CLF - Chilean Unit of Account (UF)
CLP - Chilean Peso
CNH - Chinese Yuan (Offshore)
CNY - Chinese Yuan
COP - Colombian Peso
CRC - Costa Rican Colón
CUC - Cuban Convertible Peso
CUP - Cuban Peso
CVE - Cape Verdean Escudo
CZK - Czech Republic Koruna
DJF - Djiboutian Franc
DKK - Danish Krone
DOP - Dominican Peso
DZD - Algerian Dinar
EGP - Egyptian Pound
ERN - Eritrean Nakfa
ETB - Ethiopian Birr
EUR - Euro
FJD - Fijian Dollar
FKP - Falkland Islands Pound
GBP - British Pound Sterling
GEL - Georgian Lari
GGP - Guernsey Pound
GHS - Ghanaian Cedi
GIP - Gibraltar Pound
GMD - Gambian Dalasi
GNF - Guinean Franc
GTQ - Guatemalan Quetzal
GYD - Guyanaese Dollar
HKD - Hong Kong Dollar
HNL - Honduran Lempira
HRK - Croatian Kuna
HTG - Haitian Gourde
HUF - Hungarian Forint
IDR - Indonesian Rupiah
ILS - Israeli New Sheqel
IMP - Manx pound
INR - Indian Rupee
IQD - Iraqi Dinar
IRR - Iranian Rial
ISK - Icelandic Króna
JEP - Jersey Pound
JMD - Jamaican Dollar
JOD - Jordanian Dinar
JPY - Japanese Yen
KES - Kenyan Shilling
KGS - Kyrgystani Som
KHR - Cambodian Riel
KMF - Comorian Franc
KPW - North Korean Won
KRW - South Korean Won
KWD - Kuwaiti Dinar
KYD - Cayman Islands Dollar
KZT - Kazakhstani Tenge
LAK - Laotian Kip
LBP - Lebanese Pound
LKR - Sri Lankan Rupee
LRD - Liberian Dollar
LSL - Lesotho Loti
LYD - Libyan Dinar
MAD - Moroccan Dirham
MDL - Moldovan Leu
MGA - Malagasy Ariary
MKD - Macedonian Denar
MMK - Myanma Kyat
MNT - Mongolian Tugrik
MOP - Macanese Pataca
MRU - Mauritanian Ouguiya
MUR - Mauritian Rupee
MVR - Maldivian Rufiyaa
MWK - Malawian Kwacha
MXN - Mexican Peso
MYR - Malaysian Ringgit
MZN - Mozambican Metical
NAD - Namibian Dollar
NGN - Nigerian Naira
NIO - Nicaraguan Córdoba
NOK - Norwegian Krone
NPR - Nepalese Rupee
NZD - New Zealand Dollar
OMR - Omani Rial
PAB - Panamanian Balboa
PEN - Peruvian Nuevo Sol
PGK - Papua New Guinean Kina
PHP - Philippine Peso
PKR - Pakistani Rupee
PLN - Polish Zloty
PYG - Paraguayan Guarani
QAR - Qatari Rial
RON - Romanian Leu
RSD - Serbian Dinar
RUB - Russian Ruble
RWF - Rwandan Franc
SAR - Saudi Riyal
SBD - Solomon Islands Dollar
SCR - Seychellois Rupee
SDG - Sudanese Pound
SEK - Swedish Krona
SGD - Singapore Dollar
SHP - Saint Helena Pound
SLL - Sierra Leonean Leone
SOS - Somali Shilling
SRD - Surinamese Dollar
SSP - South Sudanese Pound
STD - São Tomé and Príncipe Dobra (pre -2018)
STN - São Tomé and Príncipe Dobra
SVC - Salvadoran Colón
SYP - Syrian Pound
SZL - Swazi Lilangeni
THB - Thai Baht
TJS - Tajikistani Somoni
TMT - Turkmenistani Manat
TND - Tunisian Dinar
TOP - Tongan Pa'anga
TRY - Turkish Lira
TTD - Trinidad and Tobago Dollar
TWD - New Taiwan Dollar
TZS - Tanzanian Shilling
UAH - Ukrainian Hryvnia
UGX - Ugandan Shilling
USD - United States Dollar
UYU - Uruguayan Peso
UZS - Uzbekistan Som
VEF - Venezuelan Bolívar Fuerte (Old)
VES - Venezuelan Bolívar Soberano
VND - Vietnamese Dong
VUV - Vanuatu Vatu
WST - Samoan Tala
XAF - CFA Franc BEAC
XAG - Silver Ounce
XAU - Gold Ounce
XCD - East Caribbean Dollar
XDR - Special Drawing Rights
XOF - CFA Franc BCEAO
XPD - Palladium Ounce
XPF - CFP Franc
XPT - Platinum Ounce
YER - Yemeni Rial
ZAR - South African Rand
ZMW - Zambian Kwacha
ZWL - Zimbabwean Dollar""",)
            
            #format text font and as read-only in text widget
            text_widget.configure(font = (font, 11),fg='green', state = 'disabled')
            
            #create 'back' button in new window to return to main window
            newbutton = Button(newframe, text = "Back",font = (font, 11),  bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = lambda:newwin.destroy())
            newbutton.place(relx = 0.76, rely = 0.82, relwidth = 0.14, relheight = 0.11)
            newwin.mainloop()
        
        #create 'help' button in main window
        self.help_button = Button(self, text='Help', fg='black',width=7, command=help)

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
        self.help_button.place (x=200, y=400, anchor = 'center')


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
            convert_error = messagebox.showwarning('WARNING!', "Sorry, that's an invalid entry\nPlease use integers or decimals")
            return convert_error


if __name__ == '__main__':
    converter = CurrencyConverter('https://api.exchangerate.host/latest')
    Main(converter)
    mainloop()
