from core import generator, nodeElement

class initClasse(nodeElement):
    oRoots = []
    def __init__(self, oProject):

        # recuperation des arguments
        self.classes = []
        for oClasse in generator.getNodesByTypes( oProject[ 'data' ], 'classes/classe' ):
            self.classes.append( oClasse[ 'text' ] )