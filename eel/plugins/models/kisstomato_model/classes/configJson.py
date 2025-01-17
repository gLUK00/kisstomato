from core import generator, nodeElement

class configJson(nodeElement):
    oEls = []
    def __init__(self, oProject):
        self.project = oProject

        # pour les elements
        self.oEls = generator.getNodesByTypes( self.project[ 'data' ], 'elements/element' )
        for oEl in self.oEls:
            oEl[ 'items' ] = self._getItems( oEl )

            # recupere les types d'enfants
            sChildrenType = ''
        
            # controle la presence des references enfants
            oTmpChilds = generator.getNodesByTypes( oEl, 'element/element_childrens_type/element_children_type' )
            for oTmpChild in oTmpChilds:
                oRefItems = self._getItems( oTmpChild )
                if 'ref_element' not in oRefItems:
                    continue

                # recupere le type
                oRefNodeType = generator.getNodeById( oRefItems[ 'ref_element' ][ 'value' ], self.project[ 'data' ] )
                if not oRefNodeType:
                    continue
                if sChildrenType != '':
                    sChildrenType += ', '
                sChildrenType += '"' + oRefNodeType[ 'text' ].lower() + '"'
            
            oEl[ 'children-type' ] = sChildrenType

            # controle si il y a des enfants "item"
            oChildItems = []
            oTmpChilds = generator.getNodesByTypes( oEl, 'element/items/item' )
            for oTmpChild in oTmpChilds:
                oTmpChild[ 'items' ] = self._getItems( oTmpChild )
                oChildItems.append( oTmpChild )

            oEl[ 'child-items' ] = oChildItems

            # determine si l'element peut etre deplace
            oEl[ 'move-on-parent' ] = "move-on-parent" in oEl[ 'items' ] and oEl[ 'items' ][ 'move-on-parent' ]
        
        # pour les proprietes
        self.oPrs = generator.getNodesByTypes( self.project[ 'data' ], 'properties/property' )
        for oPr in self.oPrs:
            oPr[ 'items' ] = self._getItems( oPr )

    # retourne le type d'element en fonction de l'id du noeud
    def getTypeFromId( self, sId ):
        oRefNodeType = generator.getNodeById( sId, self.project[ 'data' ] )
        if not oRefNodeType:
            return ''
        return oRefNodeType[ 'text' ]