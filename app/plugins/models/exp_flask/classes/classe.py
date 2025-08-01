# kisstomato-classe-a-start-user-code-kisstomato
# kisstomato-classe-a-stop-user-code-kisstomato

from core import generator, nodeElement

# kisstomato-classe-b-start-user-code-kisstomato
# kisstomato-classe-b-stop-user-code-kisstomato

# Classe de génération des classes
# Argument :
# - node : object : (obligatoire) node de la classe
class classe(nodeElement):
    def __init__(self, node):
        # kisstomato-init-a-start-user-code-kisstomato
        # kisstomato-init-a-stop-user-code-kisstomato

        self.node = node

        # kisstomato-init-b-start-user-code-kisstomato
        self.items = self._getItems( node )
        self.argsInits = []
        self.methodes = []
        for oFonction in generator.getNodesByTypes( self.node, 'classe/classe-methodes/fonction' ):
            oItems = self._getItems( oFonction )
            
            # determine le nom de la fonction            
            sName = oFonction[ "text" ]
            if sName == "__init__":
                
                # recupere les arguments
                for oArg in generator.getNodesByTypes( oFonction, 'fonction/arguments/argument' ):
                    oArgItems = self._getItems( oArg )
                    self.argsInits.append( { "name": oArg[ "text" ], "desc": oArgItems[ "desc" ][ 'value' ], "require": oArgItems[ "require" ][ 'value' ] == True, 'type': oArgItems[ "type" ][ 'value' ] } )
            else:
                
                # recupere la fonction
                oFon = { "name": sName, "desc": oItems[ "desc" ][ 'value' ], "exception": self._getItemsValue( oItems, "exception", False ), "return": self._getItemsValue( oItems, "return", None ), "static": self._getItemsValue( oItems, "static", False ), 'args': [] }
                
                # recupere les arguments
                for oArg in generator.getNodesByTypes( oFonction, 'fonction/arguments/argument' ):
                    oArgItems = self._getItems( oArg )
                    oFon[ 'args' ].append( { "name": oArg[ "text" ], "desc": oArgItems[ "desc" ][ 'value' ], "require": oArgItems[ "require" ][ 'value' ] == True, 'type': oArgItems[ "type" ][ 'value' ], "exception": self._getItemsValue( oItems, "exception", False ) } )
                
                # ajoute la fonction
                self.methodes.append( oFon )
        # kisstomato-init-b-stop-user-code-kisstomato

    # Retourne le nom de la classe
    def getName(self):
        oResult = None

        # kisstomato-methode-getName-start-user-code-kisstomato
        oResult = self.node[ 'text' ]
        # kisstomato-methode-getName-stop-user-code-kisstomato

        return oResult

    # recupere la description
    def getDesc(self):
        oResult = None

        # kisstomato-methode-getDesc-start-user-code-kisstomato
        oResult = self.items[ 'desc' ][ 'value' ]
        # kisstomato-methode-getDesc-stop-user-code-kisstomato

        return oResult

    # Retourne les arguments du constructeur
    def getArgsInit(self):
        oResult = None

        # kisstomato-methode-getArgsInit-start-user-code-kisstomato
        oResult = self.argsInits
        # kisstomato-methode-getArgsInit-stop-user-code-kisstomato

        return oResult

    # Retourne la listes des méthodes
    def getMethodes(self):
        oResult = None

        # kisstomato-methode-getMethodes-start-user-code-kisstomato
        oResult = self.methodes
        # kisstomato-methode-getMethodes-stop-user-code-kisstomato

        return oResult

    # Retourne le nom de la classe héritée
    def getHeritage(self):
        oResult = None

        # kisstomato-methode-getHeritage-start-user-code-kisstomato
        oResult = self.items[ 'heritage' ][ 'value' ]
        # kisstomato-methode-getHeritage-stop-user-code-kisstomato

        return oResult

    # kisstomato-methodes-a-start-user-code-kisstomato
    # kisstomato-methodes-a-stop-user-code-kisstomato

# kisstomato-classe-c-start-user-code-kisstomato
# kisstomato-classe-c-stop-user-code-kisstomato