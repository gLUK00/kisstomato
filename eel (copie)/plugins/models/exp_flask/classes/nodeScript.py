# kisstomato-classe-a-start-user-code-kisstomato
# kisstomato-classe-a-stop-user-code-kisstomato

from core import generator, nodeElement

# kisstomato-classe-b-start-user-code-kisstomato
# kisstomato-classe-b-stop-user-code-kisstomato

# Script autonome
# Argument :
# - node : object : (obligatoire) noeud du script
class nodeScript(nodeElement):
    def __init__(self, node):
        # kisstomato-init-a-start-user-code-kisstomato
        # kisstomato-init-a-stop-user-code-kisstomato

        self.node = node

        # kisstomato-init-b-start-user-code-kisstomato
        self.items = self._getItems( node )
        
        self.args = []
        for oArg in generator.getNodesByTypes( self.node, 'script/arguments/argument' ):
            oItems = self._getItems( oArg )
            self.args.append( { "name": oArg[ "text" ], "desc": oItems[ "desc" ][ 'value' ], "require": oItems[ "require" ][ 'value' ] == True, "type": oItems[ "type" ][ 'value' ] } )
        
        self.sections = []
        for oSection in generator.getNodesByTypes( self.node, 'script/sections/section' ):
            oItems = self._getItems( oSection )
            self.sections.append( { "name": oSection[ "text" ], "desc": oItems[ "desc" ][ 'value' ] } )
        
        self.functions = []
        for oFonction in generator.getNodesByTypes( self.node, 'script/fonctions/fonction' ):
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

    # determine si la description doit etre affichee au demarrage
    def printDescOnStart(self):
        oResult = None

        # kisstomato-methode-printDescOnStart-start-user-code-kisstomato
        oResult = self.items[ 'print_desc' ][ 'value' ] == True
        # kisstomato-methode-printDescOnStart-stop-user-code-kisstomato

        return oResult

    # recupere l'ensemble des arguments
    def getArgs(self):
        oResult = None

        # kisstomato-methode-getArgs-start-user-code-kisstomato
        oResult = self.args
        # kisstomato-methode-getArgs-stop-user-code-kisstomato

        return oResult

    # Retourne la liste des sections
    def getSections(self):
        oResult = None

        # kisstomato-methode-getSections-start-user-code-kisstomato
        oResult = self.sections
        # kisstomato-methode-getSections-stop-user-code-kisstomato

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