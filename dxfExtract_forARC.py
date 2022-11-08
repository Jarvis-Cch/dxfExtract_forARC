from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys
import ezdxf
import numpy as np
import matplotlib as mpl

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


#Loading DXF file
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

#helper function
def print_entity(e):
    print("LINE on layer: %s\n" % e.dxf.layer)
    print("start point: %s\n" % e.dxf.start)
    print("end point: %s\n" % e.dxf.end)

msp = doc.modelspace()
#Sample Code for extracting all the lines start point and end point
# for e in msp:
#     if e.dxftype() == "LINE":
#         print_entity(e)

#Extract all points
# pointslist = [] #Declare list to store the dxf points coordinates
# i = 0
# for e in msp:
#     if e.dxftype() == "LINE":
#         if i == 0:
#             pointslist.append(e.dxf.start)
#             pointslist.append(e.dxf.end)
#             #print("Point ", i+1, " : ", "%s\n" % e.dxf.start)
#             #print("Point ", i+2, " : ", "%s\n" % e.dxf.end)
#             i = i + 1
#         else:
#             #print("Point ", i+2, " : ", "%s\n" % e.dxf.end)
#             pointslist.append(e.dxf.end)
#             i = i + 1
#     else:
#         print(vars(e.dxf))
#         print(e.dxftype())
        # print(e.dxf.location)
pointslist = np.array([list(e.dxf.location.xyz) for e in msp if e.dxftype() == "POINT"])
#pointslist = np.array[pointslist]
print(pointslist)
sys.exit()