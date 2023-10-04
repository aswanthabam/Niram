![Available Colors](https://raw.githubusercontent.com/aswanthabam/Niram/images/banner.png)

# Python Niram

This is a simple module to get coloured text in linux, max , and also in android termux (not supported in windows CMD)

## Installation

### Using pypi

You can install Niram using pypi. Execute..

```console
python3 -m pip install Niram
```

### Using setup.py

You can install Niram module by source code. Download source code from <a href="https://abam.herokuapp.com/projects/Niram">Link is not available. Checkout Github instead</a>

Download the zip file and unzip the file.(Use `unzip` command) Then execute setup.py install.

```console
cd Niram-1.0.4
python3 setup.py install
```

## Usage

```python
from Niram import Colours
obj = Colours() # Create a object
# Print using print() method
obj.print("Your Text Goes here",110) # 110 is the colour code
obj.print(["Hi","How are you?","Checkout niram"],[22,119,220],seperator="\n") # print multiple text with multiple colours
# Get formatted string using colour() method
txt = obj.colour(273,"Your text goes here") # returns the string representing the coloured text
print(txt) # Print the formatte text
txt2 = obj.format(["Example","Formatting"],[80,51],seperator=", ",end=" - Niram") # Gives foramted string with multiple colors
print(txt2)
```

This will return the formated text
here colour_code is a number of the colour get it by executing

```console
python3 -m Niram -c
```

This will list out all colours and responsible number
Second argument is your text and third argument "second" is the background colour or any other colour you need

### Available Colors

![Available Colors](https://raw.githubusercontent.com/aswanthabam/Niram/images/colors.png)

## Requirements

This module don't need any additional requirements
