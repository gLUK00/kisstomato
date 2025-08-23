from core import generator, nodeElement

class javascript(nodeElement):
    oRoots = []
    def __init__(self, oJs):
        oItems = self._getItems( oJs )
        self.name = oJs[ 'text' ]
        self.desc = oItems[ 'desc' ][ 'value' ]

        # recupere les sections
        self.sections = []
        for oSection in generator.getNodesByTypes( oJs, 'javascript/js_sections/section' ):
            oItems = self._getItems( oSection )
            self.sections.append( { 'name': oSection[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ] } )

        # recupere les fonctions
        self.fonctions = []
        for oFonction in generator.getNodesByTypes( oJs, 'javascript/fonctions/fonction' ):
            oItems = self._getItems( oFonction )

            # recupere les arguments
            oArgs = []
            for oArg in generator.getNodesByTypes( oFonction, 'fonction/arguments/argument' ):
                oItemsA = self._getItems( oArg )
                oArgs.append( { 'name': oArg[ 'text' ], 'desc': oItemsA[ 'desc' ][ 'value' ], 'require': oItemsA[ 'require' ][ 'value' ], 'type': oItemsA[ 'type' ][ 'value' ] } )

            self.fonctions.append( { 'name': oFonction[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ], 'args': oArgs, 'return-val': oItems[ 'return-val' ][ 'value' ] } )

        # recupere les jquery_ready
        self.jquerys_ready = []
        for oJQR in generator.getNodesByTypes( oJs, 'javascript/jquerys/jquery_ready' ):
            oItems = self._getItems( oJQR )
            self.jquerys_ready.append( { 'name': oJQR[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ] } )

        # recupere les jquery_on
        self.jquerys_on= []
        for oJQO in generator.getNodesByTypes( oJs, 'javascript/jquerys/jquery_on' ):
            oItems = self._getItems( oJQO )
            self.jquerys_on.append( { 'name': oJQO[ 'text' ], 'desc': oItems[ 'desc' ][ 'value' ], 'event': oItems[ 'event' ][ 'value' ], 'selector': oItems[ 'selector' ][ 'value' ] } )
