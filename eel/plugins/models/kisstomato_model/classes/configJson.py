from core import generator, nodeElement

class configJson(nodeElement):
    oEls = []
    def __init__(self, oProject):
        self.project = oProject
        self.oEls = generator.getNodesByTypes( self.project[ 'data' ], 'elements/element' )
        for oEl in self.oEls:
            oEl[ 'items' ] = self._getItems( oEl )

        print( 'rrrrrrrrrrrrrrr' )
        """self.oRoots = []
        
        # recupere les noeuds root
        # controle la presence des references enfants
        oTmpRoots = generator.getNodesByTypes( self.project[ 'data' ], 'roots/root' )
        for oTmpRoot in oTmpRoots:
            oItems = self._getItems( oTmpRoot )
            oRoot = { 'id': oItems[ 'id' ][ 'value' ], 'text': oTmpRoot[ 'text' ] }
            if 'icon' in oItems and oItems[ 'icon' ][ 'value' ] != '':
                oRoot[ 'icon' ] = 'fa-' + oItems[ 'icon' ][ 'value' ][ 'style' ] + ' fa-' + oItems[ 'icon' ][ 'value' ][ 'icon' ]
                oRoot[ 'color' ] = oItems[ 'icon' ][ 'value' ][ 'color' ]
            
            # pour tous les types d'enfants
            sTypes = ''
            oChilds = generator.getNodesByTypes( oTmpRoot, 'root/link_childs/link_child' )
            for oRefChild in oChilds:
                oRefItems = self._getItems( oRefChild )
                if 'ref_element' not in oRefItems:
                    continue
                
                # recupere le type
                oRefNodeType = generator.getNodeById( oRefItems[ 'ref_element' ][ 'value' ], self.project[ 'data' ] )
                if not oRefNodeType:
                    continue
                if sTypes != '':
                    sTypes += ', '
                sTypes += '"' + oRefNodeType[ 'text' ].lower() + '"'
            oRoot[ 'children-type' ] = sTypes
            
            self.oRoots.append( oRoot )"""
    
    """
    # determine si la methode "getJsonCreateNewProject" doit etre implementee
    def asGetJsonCreateNewProject(self):
        return 'properties' in self.project and self.project[ 'properties' ][ 'impl-getJsonCreateNewProject' ]

    # determine si la methode "openProject" doit etre implementee
    def asOpenProject(self):
        return 'properties' in self.project and self.project[ 'properties' ][ 'impl-openProject' ]
    """
