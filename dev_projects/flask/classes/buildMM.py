# kisstomato-class-import-start-user-code-kisstomato
import threading
from modules import converter
# kisstomato-class-import-stop-user-code-kisstomato

"""
Classe de compilation des moyennes mobiles
"""

class buildMM(threading.Thread):
    """
    Classe de compilation des moyennes mobiles
    """

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self, indexTime, sizeRange, minutes):
        # kisstomato-class-init-start-user-code-kisstomato
        self.disponible = True
        self.indexTime = indexTime
        self.sizeRange = sizeRange
        self.minutes = minutes
        self.results = []
        # kisstomato-class-init-stop-user-code-kisstomato

    """
    compilation des moyennes mobiles
    """
    def start(self):
        try:
            # kisstomato-class-methode-start-start-user-code-kisstomato
            pass
            # kisstomato-class-methode-start-stop-user-code-kisstomato
        except Exception as e:
            # kisstomato-class-exception-start-start-user-code-kisstomato
            print( e )
            # kisstomato-class-exception-start-stop-user-code-kisstomato
            
        # kisstomato-class-finally-start-start-user-code-kisstomato
        # kisstomato-class-finally-start-stop-user-code-kisstomato 
