import eel
import sys
if sys.version_info[0] == 3:
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog
else:
    from Tkinter import *
    import Tkinter as tk
    from Tkinter import filedialog

from core import config

# affichage de la fenetre d'enregistrement sous
def saveAs( text, ext, initialfile ):
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    filename = filedialog.asksaveasfilename(initialdir=config.getPathBase(),
        defaultextension='.' + ext,
        initialfile=initialfile,
        filetypes=[ (text,"." + ext) ]
    )

    root.update()

    return filename

# affichage de la fenetre de selection d'un repertoire
def setDir( text ):

    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    dirName = filedialog.askdirectory(initialdir=text)

    root.update()

    return dirName

# affichage de la fenetre de selection d'un fichier
def setFile( text, ext ):
    
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    filename = filedialog.askopenfilename(initialdir=config.getPathBase(),
        defaultextension='.' + ext,
        filetypes=[ (text,"." + ext) ]
    )

    root.update()

    return filename

# ouvre une nouvelle fenetre
def newWindow( file ):
    eel.show( file )
