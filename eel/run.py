import eel, random, os, sys, json, time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# inclusion des elements communs
from core import config
from routes import app, model, project

# chargement du fichier de configuration
config.load()

# en mode dev
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global eel
        if event.src_path.endswith(".py") or event.src_path.endswith(".json"):
            
            print("Fichier modifié, redémarrage de l'application...")
            
            # fermeture est reouverture de l'application
            eel.close_all()
            os.execv(sys.executable, [os.path.basename(sys.executable)] + sys.argv)

def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        exit()

# recupere tous les projets
@eel.expose
def get_all_models():
    return model.getAll()

# generation d'un fichier pour un nouveau projet
@eel.expose
def get_create_file_project( data ):
    return project.createFileProject( data )

# fenetre de selection des fichiers de type "save-as"
@eel.expose
def app_save( text, ext, initialfile ):
    return app.saveAs( text, ext, initialfile )

# retourne tous les projets
@eel.expose
def get_all_projects():
    return project.getAll()

# supprime un projet
@eel.expose
def del_project( filename, deletefile ):
    return project.delProject( filename, deletefile )

if __name__ == '__main__':
    """observer = Observer()
    observer.schedule(MyHandler(), '.', recursive=True)
    observer.start()
    """
    eel.init('web')
    eel.start( 'index.html', size=(1200, 1200), port=config.configuration[ "port" ] )