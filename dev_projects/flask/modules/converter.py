# kisstomato-module-import-start-user-code-kisstomato
import datetime, pandas as pd
# kisstomato-module-import-stop-user-code-kisstomato

"""
Module d'aide à la conversion
"""

# kisstomato-module-properties-start-user-code-kisstomato
# kisstomato-module-properties-stop-user-code-kisstomato

"""
Conversion d'un timestamp en timestamp arrondi à la minute
"""
# Argument :
# - time : number : (obligatoire) Timestamp d'entrée
def time2minutes(time):
    oResult = None

    # kisstomato-methode-time2minutes-start-user-code-kisstomato
    
    #date_time = datetime.datetime.fromtimestamp( time )
    #ts = pd.Timestamp( date_time )
    #oResult = int( ts.round('1min').timestamp() ) - ( 2 * 3600 )
    oResult = (time // 60) * 60
            
    # kisstomato-methode-time2minutes-stop-user-code-kisstomato

    return oResult

# kisstomato-module-end-start-user-code-kisstomato
# kisstomato-module-end-stop-user-code-kisstomato