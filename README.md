# UROPS2020

INITIAL TEST:

Main program is RunSeshat.py
The program will take a xml (converting it to scgink format) and pass it through the seshat model and output a tex file.
It will also generate a png file to visualize the pen input

Requirements:
1. a folder named "SCG" to store the converted scgink file
2. a folder named "Input" to store the xml file
3. a folder named "Plots" to store the png file
4. a folder named "Latex" to store the tex file
5. GetLatex.py needs to be inside the Seshat folder

Customized dits are required to adjust for directory paths in the .py files

TO run the program (given a input xml file named "test."):
1. $ python3 RunSeshat test. 


UPDATE:

The file NewPageClass.py creates a Page objection.
The loadlines method takes in a xopp file and run seshat to get the individual lines of the file and stores them in the dictionary in the lines attribute

UPDATE:
New class Document added.
It takes in a xopp file. It has the attribute pages, which is a dictionary of NewPage class for each page of the xopp.
