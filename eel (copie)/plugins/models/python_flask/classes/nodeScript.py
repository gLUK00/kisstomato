from core import generator

class nodeScript:
    def __init__(self, oNode):
        self.node = oNode

        # map les items
        self.values = {}
        for oItem in oNode[ 'li_attr' ][ 'items' ]:
            self.values[ oItem[ 'id' ] ] = oItem[ 'value' ]
    
    # recupere le nom
    def getName(self):
        return self.node[ 'text' ]

    # recupere la description
    def getDesc(self):
        return self.values[ 'desc' ]
    
    # determine si la description doit etre affichee au demarrage
    def printDescOnStart(self):
        return 'print_desc' in self.values and self.values[ 'print_desc' ] == True
    
    # recupere l'ensemble des arguments
    def getArgs(self):
        oArgs = generator.getNodesByTypes( self.node, 'script/app_arguments/argument' )
        
        oResults = []
        for oArg in oArgs:
            oResult = { 'name': oArg[ 'text' ] }
            for oItem in oArg[ 'li_attr' ][ 'items' ]:
                oResult[ oItem[ 'id' ] ] = oItem[ 'value' ]
            oResults.append( oResult )

        return oResults
