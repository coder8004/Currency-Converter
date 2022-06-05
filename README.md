# Currency Converter - Group project FS2022 

Project Language: Python

Group ID: MoneyCounters

## Table of contents
* [Introduction](#Introduction)
* [Project-Description](#Project-Description)
* [Installations](#Installations)
* [How-does-it-work](#How-does-it-work)
* [Source](#Source)


## Introduction
This project is part of the mandatory curriculum of the course "7,789 | 8,789 Skills: Programming with Advanced Computer Languages” supervised by Dr. Mario Silic at the University of St. Gallen. It was created by a group of students consisting of six people namely Sara Aeppli, Kimberly ANG Xiuqi, Cornel Bienz, Luis Contreras, Florian Grob and Marc Wallach. 


## Project-Description
The base of the code is an existing one.

However, we adjusted a few things:
* Drop-down tabs
* A scroll bar for both the entry currency and desired output currency
* Background color (from grey to green) throughout most of the background and blue for the header
* Fonts 
* Title: added "Currency Converter by MoneyCounters" 
* Sizes of boxes/fields/labels
* Places of the boxes/fields/labels
* Changed the displayed decimal places to 3 

Additionally, we added a few things:
* Time Stamp next to the date
* A "Help" button that shows abbreviation of common Currencies 

## Installations
The following programs were used to analyze and test the code:
* Python 3.9 
* Anaconda 3
* Jupyter Notebook and VS Code (visual studio code - program)

The following packages and modules are required to run the code: 
* tkinter
* requests
* datetime

## How-does-it-work?
First, the above-mentioned packages and modules need to be imported. 

Secondly, the program for converting a given amount into another currency must be coded with real-time data for the rates. Therefore, the data needs to be retrieved from the following API: 'https://api.exchangerate.host/latest'

The Convert method follows the following logic: Base-currency set as CHF, default conversion currency to USD, cross multiplication between the amount and the rate.
Additionally, we define two format conditions for the output number:
* Results are limited to 3 decimal places
* Comma is added every 3 numbers when necessary
       
       
Last, for the user interface, a window with all the boxes is created. The end result generates a GUI with 3 user inputs, 1 output, and 1 embedded button that populates a list clarifying currency (in long form) to its respective country. 



## Sources
* https://github.com/MBobyPratama/Currency-Converter-Tkinter/blob/master/Currency_Converter.py
* https://pytutorial.com/get-capital-currency-python
* https://www.xe.com/
* https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
* https://copyassignment.com/currency-converter-desktop-application-in-python/
* https://www.askpython.com/python-modules/tkinter/tkinter-text-widget-tkinter-scrollbar
* https://openexchangerates.org/api/currencies.json
* https://www.delftstack.com/howto/python-tkinter/how-to-set-font-of-tkinter-text-widget/
* https://stackhowto.com/how-to-make-tkinter-text-widget-read-only/
![image](https://user-images.githubusercontent.com/105594393/172074517-66b8d567-c5ac-4846-a630-f3671f939c7e.png)
