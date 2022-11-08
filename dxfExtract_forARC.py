from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys
import ezdxf
import numpy as np

#Obtain filename & path from user input from File Explorer GUI
Tk().withdraw() #keep away the root window
filename = askopenfilename()
print(filename)
if filename.endswith('.dxf'):
    print("File type correct")
else:
    print("File type incorrect")
    print("The program exits")
    sys.exit()


#Loading and checking DXF file
print("Checking .dxf file...")
try:
    doc = ezdxf.readfile(filename)
except IOError:
    print(f"Not a .dxf file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)

print(".dxf file ok")

#Create model space and extract all points in .dxf
msp = doc.modelspace()
pointslist = np.array([list(e.dxf.location.xyz) for e in msp if e.dxftype() == "POINT"])

#Print all points in terminal
print(pointslist)
sys.exit()