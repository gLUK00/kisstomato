# kisstomato-class-import-start-user-code-kisstomato
import ephem, datetime, calendar
# kisstomato-class-import-stop-user-code-kisstomato

"""
Classe outil d'aide à la création d'image
"""

class imageHelper:
    """
    Classe outil d'aide à la création d'image
    """

    # kisstomato-class-properties-start-user-code-kisstomato
    _instance = None
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self):
        # kisstomato-class-init-start-user-code-kisstomato
        pass
        # kisstomato-class-init-stop-user-code-kisstomato

    """
    Méthode singleton
    """
    @staticmethod
    def get():
        oResult = None

        # kisstomato-class-methode-get-start-user-code-kisstomato
        if imageHelper._instance is None:
            imageHelper._instance = imageHelper()
        oResult = imageHelper._instance
        # kisstomato-class-methode-get-stop-user-code-kisstomato
        return oResult

    """
    Retourne un vecteur de carte du ciel à partir d'un timestamp
    """
    # Argument :
    # - iTime : number : (obligatoire) Timestamp de référence
    def skymap2time(self, iTime):
        oResult = None

        # kisstomato-class-methode-skymap2time-start-user-code-kisstomato
        
        oResult = []

        # conversion de la date
        date_time = datetime.datetime.fromtimestamp(iTime)
        sDate = datetime.datetime.strptime( str(date_time), '%Y-%m-%d %H:%M:%S' )

        # pour toutes les planetes
        for p in [ ephem.Mercury( sDate ), ephem.Venus( sDate ), ephem.Mars( sDate ), ephem.Jupiter( sDate ), ephem.Saturn( sDate ), ephem.Uranus( sDate ), ephem.Neptune( sDate ), ephem.Pluto( sDate ), ephem.Sun( sDate ), ephem.Moon( sDate ), ephem.Phobos( sDate ), ephem.Deimos( sDate ), ephem.Io( sDate ), ephem.Europa( sDate ), ephem.Ganymede( sDate ), ephem.Callisto( sDate ), ephem.Mimas( sDate ), ephem.Enceladus( sDate ), ephem.Tethys( sDate ), ephem.Dione( sDate ), ephem.Rhea( sDate ), ephem.Titan( sDate ), ephem.Hyperion( sDate ), ephem.Iapetus( sDate ), ephem.Ariel( sDate ), ephem.Umbriel( sDate ), ephem.Titania( sDate ), ephem.Oberon( sDate ), ephem.Miranda( sDate ) ]:
            oResult.append( self.normalize( p.a_ra + 0.0, 0, 6.5 ) )
            oResult.append( self.normalize( p.a_dec + 0.0, -0.5, +0.5 ) )
            if 'earth_distance' in dir(p):
                oResult.append( self.normalize( p.earth_distance + 0.0, 0, 50 ) )
            if 'phase' in dir(p) and p.name != 'Sun':
                oResult.append( self.normalize( p.phase + 0.0, 0, 100 ) )
            if 'mag' in dir(p):
                oResult.append( self.normalize( p.mag + 0.0, -27, 15 ) )

        # kisstomato-class-methode-skymap2time-stop-user-code-kisstomato
        return oResult

    """
    Normalise une valeur sur un place de 0 à 1
    """
    # Arguments :
    # - iVal : number : (obligatoire) Valeur d'entrée
    # - iMin : number : (obligatoire) Valeur minimum
    # - iMax : number : (obligatoire) Valeur maximum
    def normalize(self, iVal, iMin, iMax):
        oResult = None

        # kisstomato-class-methode-normalize-start-user-code-kisstomato
        # Normalize value linearly between min and max to range [0,1]
        if iMax == iMin:  # Prevent division by zero
            oResult = 0
        else:
            oResult = max(0, min(1, (iVal - iMin) / (iMax - iMin)))
        # kisstomato-class-methode-normalize-stop-user-code-kisstomato
        return oResult

    """
    Retourne une date à partir d'un timestamp
    """
    # Argument :
    # - iTime : number : (obligatoire) Timestamp de référence
    def date2str(self, iTime):
        oResult = None

        # kisstomato-class-methode-date2str-start-user-code-kisstomato
        dt = datetime.datetime.fromtimestamp(iTime)
        oResult = dt.strftime("%d/%m/%Y %H:%M:%S")
        # kisstomato-class-methode-date2str-stop-user-code-kisstomato
        return oResult

    """
    Vectorisation de la date, sous la forme : 3 positions,
	- 1 position concernant le mois, 1/12,
	- 1 position concernant le jour de la semaine, 1/7,
	- 1 position concernant l’heure, 1/24,
    """
    # Argument :
    # - iTime : number : (obligatoire) Timestamp de référence
    def date2vec(self, iTime):
        oResult = None

        # kisstomato-class-methode-date2vec-start-user-code-kisstomato
        # Convertir le timestamp en datetime
        dt = datetime.datetime.fromtimestamp(iTime)
        
        # Extraire le mois (1-12) avec sous-graduation journalière et normaliser sur ~0-1
        num_days_in_month = calendar.monthrange(dt.year, dt.month)[1]
        day_factor = (dt.day - 1.0) / (num_days_in_month - 1.0) if num_days_in_month > 1 else 0.0
        month = ((dt.month - 1.0) + day_factor) / 12.0
        
        # Extraire le jour de la semaine (0-6) et normaliser sur 0-1
        weekday = dt.weekday() / 6.0  # dt.weekday() est 0 pour Lundi, 6 pour Dimanche
        
        # Extraire l'heure (0-23) avec sous-graduation par minute et normaliser sur ~0-1
        minute_factor_for_hour = dt.minute / 60.0 # Progression dans l'heure (0.0 à ~0.983)
        hour = (dt.hour + minute_factor_for_hour) / 24.0 # Normalise sur ~0 (début 00:00) à ~1 (fin 23:59)
        
        # Concaténer les résultats
        oResult = [month, weekday, hour]

        #print( oResult )

        # kisstomato-class-methode-date2vec-stop-user-code-kisstomato
        return oResult

    """
    Distance entre les halvings : 1 position,
	avec les dates suivantes :
	- 28/11/2012 : 1354057200
	- 09/07/2016 : 1468015200
	- 11/05/2020 : 1589148000
	- 19/04/2024 : 1713477600
	- 01/04/2028 : 1838095200
	- 01/04/2032 : 1964344800
    """
    # Argument :
    # - iTime : number : (obligatoire) Timestamp de référence
    def halvingPosition(self, iTime):
        oResult = None

        # kisstomato-class-methode-halvingPosition-start-user-code-kisstomato
        halving_timestamps = [
            1354057200,  # 28/11/2012
            1468015200,  # 09/07/2016
            1589148000,  # 11/05/2020
            1713477600,  # 19/04/2024
            1838095200,  # 01/04/2028
            1964344800   # 01/04/2032
        ]

        # recherche de la position min et max
        min_ts = float(halving_timestamps[0])
        max_ts = float(halving_timestamps[-1])
        for iPos in range( len( halving_timestamps ) ):
            if halving_timestamps[ iPos ] < iTime:
                min_ts = float(halving_timestamps[ iPos ])
            if halving_timestamps[ iPos ] > iTime:
                max_ts = float(halving_timestamps[ iPos ])
                break
        
        # determine le % de progression
        iDiffTime = max_ts - min_ts
        iOnePercent = iDiffTime / 100
        oResult =  ( ( iTime - min_ts ) / iOnePercent ) * 0.01

        #print( oResult )

        # kisstomato-class-methode-halvingPosition-stop-user-code-kisstomato
        return oResult

    """
    Converti le vecteur de l'orderbook en structure
    """
    # Argument :
    # - vec : array : (obligatoire) Vecteur de l'orderbook
    def vec2Orderbook(self, vec):
        oResult = None

        # kisstomato-class-methode-vec2Orderbook-start-user-code-kisstomato
        
        oValVentes = vec[ : 19 ]
        oValAchats = vec[ 19 : ]
        oResult = {
            "ventes": [],
            "achats": []
        }

        # Parcours des ventes avec un pas de 2
        for i in range(0, len(oValVentes), 2):
            if i+1 < len(oValVentes):
                oResult["ventes"].append({
                    "price": oValVentes[i],
                    "volume": oValVentes[i+1]
                })

        # Parcours des achats avec un pas de 2
        for i in range(0, len(oValAchats), 2):
            if i+1 < len(oValAchats):
                oResult["achats"].append({
                    "price": oValAchats[i],
                    "volume": oValAchats[i+1]
                })

        # kisstomato-class-methode-vec2Orderbook-stop-user-code-kisstomato
        return oResult

