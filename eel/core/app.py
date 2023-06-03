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

def _initRootTk():
    global root
    root = tk.Tk()
    root.wm_withdraw()
_initRootTk()

# affichage de la fenetre d'enregistrement sous
def saveAs( text, ext, initialfile ):
    global root

    filename = filedialog.asksaveasfilename(initialdir=config.configuration[ "path_base" ],
        defaultextension='.' + ext,
        initialfile=initialfile,
        filetypes=[ (text,"." + ext) ]
    )

    root.destroy()
    _initRootTk()

    return filename

# affichage de la fenetre de selection d'un fichier
def setFile( text, ext ):
    global root

    filename = filedialog.askopenfilename(initialdir=config.configuration[ "path_base" ],
        defaultextension='.' + ext,
        filetypes=[ (text,"." + ext) ]
    )

    root.destroy()
    _initRootTk()

    return filename

# ouvre une nouvelle fenetre
def newWindow( file ):
    eel.show( file )
