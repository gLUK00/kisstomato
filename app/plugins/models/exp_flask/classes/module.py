# kisstomato-classe-a-start-user-code-kisstomato
# kisstomato-classe-a-stop-user-code-kisstomato

from core import generator, nodeElement

# kisstomato-classe-b-start-user-code-kisstomato
# kisstomato-classe-b-stop-user-code-kisstomato

# classe de génération des modules
# Argument :
# - node : object : (obligatoire) noeud du module
class module(nodeElement):
    def __init__(self, node):
        # kisstomato-init-a-start-user-code-kisstomato
        # kisstomato-init-a-stop-user-code-kisstomato

        self.node = node

        # kisstomato-init-b-start-user-code-kisstomato
        self.items = self._getItems( node )
        
        self.functions = []
        for oFonction in generator.getNodesByTypes( self.node, 'module/fonctions/fonction' ):
            oItems = self._getItems( oFonction )
            
            # recupere les arguments
            oArgs = []
            for oArg in generator.getNodesByTypes( oFonction, 'fonction/arguments/argument' ):
                oArgItems = self._getItems( oArg )
                oArgs.append( { "name": oArg[ "text" ], "desc": oArgItems[ "desc" ][ 'value' ], "require": oArgItems[ "require" ][ 'value' ] == True, 'type': oArgItems[ "type" ][ 'value' ] } )
            
            self.functions.append( { "name": oFonction[ "text" ], "desc": oItems[ "desc" ][ 'value' ], "exception": oItems[ "exception" ][ 'value' ] == True, "return": oItems[ "return" ][ 'value' ], 'args': oArgs })
        # kisstomato-init-b-stop-user-code-kisstomato

    # recupere le nom
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

    # recupere la liste des fonctions
    def getFunctions(self):
        oResult = None

        # kisstomato-methode-getFunctions-start-user-code-kisstomato
        oResult = self.functions
        # kisstomato-methode-getFunctions-stop-user-code-kisstomato

        return oResult

    # kisstomato-methodes-a-start-user-code-kisstomato
    # kisstomato-methodes-a-stop-user-code-kisstomato

# kisstomato-classe-c-start-user-code-kisstomato
# kisstomato-classe-c-stop-user-code-kisstomato