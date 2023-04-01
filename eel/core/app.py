import eel
from tkinter import *
import tkinter as tk
from tkinter import filedialog

from core import config

# affichage de la fenetre d'enregistrement sous
def saveAs( text, ext, initialfile ):

    filename = filedialog.asksaveasfilename(initialdir=config.configuration[ "path_base" ],
        defaultextension='.' + ext,
        initialfile=initialfile,
        filetypes=[ (text,"." + ext) ]
    )

    return filename

# affichage de la fenetre de selection d'un fichier
def setFile( text, ext ):

    filename = filedialog.askopenfilename(initialdir=config.configuration[ "path_base" ],
        defaultextension='.' + ext,
        filetypes=[ (text,"." + ext) ]
    )

    return filename

# ouvre une nouvelle fenetre
def newWindow( file ):
    eel.show( file )
