from core import generator, nodeElement

class module(nodeElement):
    oRoots = []
    def __init__(self, oModule):
        oItems = self._getItems( oModule )
        self.name = oModule[ 'text' ]
        self.desc = oItems[ 'desc' ][ 'value' ]

        # recupere les fonctions
        self.fonctions = []
        for oFonction in generator.getNodesByTypes( oModule, 'module/fonctions/fonction' ):
            oItems = self._getItems( oFonction )

            # recupere les arguments
            oArgs = []
            for oArg in generator.getNodesByTypes( oFonction, 'fonction/arguments/argument' ):
                oItemsA = self._getItems( oArg )
                oArgs.append( { 'name': oArg[ 'text' ], 'desc': oItemsA[ 'desc' ][ 'value' ], 'require': oItemsA[ 'require' ][ 'value' ], 'type': oItemsA[ 'type' ][ 'value' ] } )

            self.fonctions.append( { 'name': oFonction[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ], 'args': oArgs, 'return-val': oItems[ 'return-val' ][ 'value' ], 'exception': oItems[ 'exception' ][ 'value' ] } )