from tkinter import *
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