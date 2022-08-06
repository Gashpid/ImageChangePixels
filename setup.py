import sys
import os
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes' : []}
base = 'Win32GUI'
exe = Executable(
    script = 'ImageChangePixels.py',
    initScript = None,
    base = 'Win32GUI',
    targetName = 'ImageChangePixels.exe',
)

setup( name = 'ImageChangePixels', 
        version = '1.0',
        description = 'ImageChangePixels',
        options = {'build_exe': build_exe_options},
        executables = [Executable('ImageChangePixels.py', base = base)])
