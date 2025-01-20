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
            oMethode = { 'name': oM[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ], 'args': [] }

            # pour les arguments
            for oArg in generator.getNodesByTypes( oM, 'methode/arguments/argument' ):
                oArgItems = self._getItems( oArg )
                oMethode[ 'args' ].append( { 'name': oArg[ 'text' ], 'desc': oArgItems[ 'desc' ][ 'value' ], 'require': oArgItems[ 'require' ][ 'value' ], 'type': oArgItems[ 'type' ][ 'value' ] } )



            self.methodes.append( oMethode )
"""

"id": "6258dacd-88b5-45bf-a265-b9efc5411e76",
                    "text": "nodeScript",
                    "li_attr": {
                        "type": "classe",
                        "items": [
                            {
                                "id": "desc",
                                "value": "Script autonome"
                            }
                        ]
                    },

"""