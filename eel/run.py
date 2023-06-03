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
            
            print("Fichier modifie, redemarrage de l'application...")
            
            # fermeture est reouverture de l'application
            eel.close_all()
            os.execv(sys.executable, [os.path.basename(sys.executable)] + sys.argv)

def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        exit()

if __name__ == '__main__':
    """observer = Observer()
    observer.schedule(MyHandler(), '.', recursive=True)
    observer.start()
    """
    eel.init('web')
    eel.start( 'index.html', size=(600, 1200), port=config.configuration[ "port" ] )