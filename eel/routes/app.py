import eel

# importation du CORE
from core import app

# fenetre de selection des fichiers de type "save-as"
@eel.expose
def app_set_file( text, ext ):
    return app.setFile( text, ext )

# affichage de la fenetre d'enregistrement sous
@eel.expose
def app_save( text, ext, initialfile ):
    return app.saveAs( text, ext, initialfile )

# affichage d'une nouvelle fenetre
@eel.expose
def app_new_window( file ):
    app.newWindow( file )