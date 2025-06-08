from core import generator, nodeElement

class tmpClasse(nodeElement):
    oRoots = []
    def __init__(self, oNode):
        self.node = oNode
        self.desc = self._getItems( oNode )[ 'desc' ][ 'value' ]

        # recuperation des arguments
        self.args = []
        for oArg in generator.getNodesByTypes( oNode, 'classe/constructor_args/argument' ):
            oItems = self._getItems( oArg )
            self.args.append( { 'name': oArg[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ], 'require': oItems[ 'require' ][ 'value' ], 'type': oItems[ 'type' ][ 'value' ] } )

        # recuperation des methodes
        self.methodes = []
        for oM in generator.getNodesByTypes( oNode, 'classe/methodes/methode' ):
            oItems = self._getItems( oM )
            oMethode = { 'name': oM[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ], 'return-val': oItems[ 'return-val' ][ 'value' ], 'args': [] }

            # pour les arguments
            for oArg in generator.getNodesByTypes( oM, 'methode/arguments/argument' ):
                oArgItems = self._getItems( oArg )
                oMethode[ 'args' ].append( { 'name': oArg[ 'text' ], 'desc': oArgItems[ 'desc' ][ 'value' ], 'require': oArgItems[ 'require' ][ 'value' ], 'type': oArgItems[ 'type' ][ 'value' ] } )

            self.methodes.append( oMethode )