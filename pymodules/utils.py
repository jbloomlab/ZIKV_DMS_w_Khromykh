"""Python utilities.

Written by Jesse Bloom."""


import os
import time
import subprocess
from IPython.display import Image, display


def showPDF(pdfs, width=None):
    '''Displays images in *pdfs*. Multiple images displayed side-by-side.'''
    png = '_temp.png'
    if not isinstance(pdfs, list):
        pdfs = [pdfs]
    subprocess.check_call(['convert', '-density', '134', '-trim'] + pdfs + 
            ['+append', png])
    time.sleep(0.5)
    display(Image(png, width=width))
    os.remove(png)

