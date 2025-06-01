# kisstomato-class-import-start-user-code-kisstomato
import ephem, datetime
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
        iRange = iMax - iMin
        iDiffMin = abs( iVal - iMin )
        iStep = iRange / 100
        oResult = ( iDiffMin / iStep ) * 0.01
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

