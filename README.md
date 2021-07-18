# Python Niram

This is a simple module to get coloured text in linux, max , and also in android termux (not supported in windows CMD)
## Installation 
### Using pypi
You can install Niram using pypi. Execute..
```console
python3 -m pip install Niram
```
### Using setup.py 
You can install Niram module by source code. Download source code from <a href="https://abam.herokuapp.com/projects/Niram">Here</a>
Download the zip file and unzip the file.(Use ```unzip``` command) Then execute setup.py install.
```console
cd Niram-1.0.4
python3 setup.py install
```

## Usage
```python
from Niram import Colours
Colours().colour(colour_code,your_text,second=your_next_colour_code)
```
This will return the formated text
here colour_code is a number of the colour get it by executing
```console
python3 -m Niram -c
```
This will list out all colours and responsible number
Second argument is your text and third argument "second" is the background colour or any other colour you need 

## Requirements
 This module don't need any additional requirements