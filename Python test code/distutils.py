import os
import sys

if len(sys.argv)>1:
    none
else:
    File = input("which script to exe?")
    os.system(            "c:/python34/Scripts/cxfreeze" + File)
    print("Done")

