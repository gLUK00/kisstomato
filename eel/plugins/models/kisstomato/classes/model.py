from core import generator

class model:
    def __init__(self, oProject):
        self.project = oProject
    
    # recupere le nom
    def asGetJsonCreateNewProject(self):
        return 'properties' in self.project and self.project[ 'properties' ][ 'impl-getJsonCreateNewProject' ]

    # recupere la description
    def asOpenProject(self):
        return 'properties' in self.project and self.project[ 'properties' ][ 'impl-openProject' ]
    
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
