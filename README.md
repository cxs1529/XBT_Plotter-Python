# XBT PLOTTER (Python script)

Download all the files to the same directory and run it from there (the .bin and .csv are not necessary).

The main script is *xbt2ascii.py* -> RUN this script on a terminal or Visual Studio Code.
Go to the directory where the scripts are located with *cd path* and then execute 
*python xbt2ascii.py* or *python3 xbt2ascii.py* or *py xbt2ascii.py*

**If using a terminal with no graphic interface or running the script in the cloud**, make *enableBrowse = False* since this will trigger an error when trying to open the browser GUI.

Edit the xbt2ascii.py file to enter the binary file path manually.   
Edit the xbt2ascii.py file to change the configuration:  
- Enable/disable plots (profile and map)
- Select type of map to display
- Edit xbtxxxxx.bin full path
- Enable/disable terminal print of all T vs D values
- Set number of datapoints to display in the terminal
- Enable/disable export to TXT file


Necessary libraries that may be needed to install with pip install libraryname before running the script (use *pip3* if pip doesn’t work):
- *pip install bitstring*
- *pip install matplotlib*
- *pip install basemap*
- *pip install numpy*
- *pip install tkinter*  >> Tkinter usually comes with the latest Python versions so may not be necessary to install.

dataRanges.csv is not necessary, but if changes are made to data ranges, then update either the dataRanges.py table, or the .csv (then you’ll have to use get_range_list() to create a new table with the updated values).


## GOOGLE COLAB

https://colab.research.google.com/drive/1-hVG7snOz2_a-fhNR5_hwSeZ3xPoIFJ1?usp=sharing

Click on the folder icon and it will open a temporary directory that will be used to handle files in the current runtime environment.
Drag and drop an XBT binary file to this folder, then right click and *copy path*. Assign this path to the binfile variable: *binfile = “copiedPath”* under USER CONFIGURATION.

![colab-output-file](https://github.com/cxs1529/XBT_Plotter-Python/assets/150298128/2ec6f197-06ee-4a0c-bc76-8f1cb2c0e73f)

