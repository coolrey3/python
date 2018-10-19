import sys
from cx_Freeze import setup
from cx_Freeze import Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "MRT Device Manager",
        version = "0.1",
        description = "Device Manager!",
        #options = {"build_exe": build_exe_options},
        executables = [Executable("mrtdevicemanager.pyw")])
