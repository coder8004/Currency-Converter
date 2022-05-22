# Currency Converter - Group project FS2022 

Project Language: Python

Group ID: XXX

## Table of contents
* [Introduction](#Introduction)
* [Project-Description](#Project-Description)
* [Installations](#Installations)
* [How-does-it-work](#How-does-it-work)
* [Source](#Source)


## Introduction
This project is part of the mandatory curriculum of the course "7,789 | 8,789 Skills: Programming with Advanced Computer Languages” supervised by Dr. Mario Silic at the University of St. Gallen. It was created by a group of students consisting of six people namely Sara Aeppli (15-XXX-XXX), Kimberly ANG Xiuqi, Cornel Bienz, Luis Contreras, Florian Grob and Marc Wallach. 


## Project-Description
The base of the code is an existing one: 

However we adjusted a few things:
* Background color (from grey to green) in all party of the converter
* Fonts (from XX to calibri)
* Titel: added "by Moneycounters" 
* Sizes of boxes/fields/labels
* Places of the boxes/fields/labels
* changed the displayed decimal places to 3 

Additionally, we added a few things:
* Time Stamp next to the date
* a "Help" bottom that shows abbreviation of common Currencies 

## Installations
The following programs were used to analyse and test the code:
* Python 3.9 
* Anaconda 3
* Jupyter Notebook and VS Code (visual studio code - program)

The following packages and modules are REQUIRED to run the code: 
* tkinter
* requests
* datetime

## How-does-it-work?
First the above mentionned packages and modules need to be imported. 

Secondly, the program for converting a given amount into another currency must be coded with real-time data for the rates. Therefore, the data needs to be retrieved from the following API: 'https://api.exchangerate.host/latest'

The Convert method follows the following logic: Base-currency set as CHF, convert the amount into CHF, cross multiplication between the amount and the rate
Additionally, we define two musts for the output number:
* results are limited to 3 decimal places
* comma should be added every 3 numbers
       
       
Then...


For the User Interface a window with all the boxes is created:


Last



## Sources
* https://github.com/MBobyPratama/Currency-Converter-Tkinter/blob/master/Currency_Converter.py
* https://pytutorial.com/get-capital-currency-python
* https://www.xe.com/
* https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
* https://copyassignment.com/currency-converter-desktop-application-in-python/




