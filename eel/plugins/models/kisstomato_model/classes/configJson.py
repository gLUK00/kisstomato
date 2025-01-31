from core import generator, nodeElement

class configJson(nodeElement):
    oEls = []
    def __init__(self, oProject):
        self.project = oProject

        # pour les elements
        self.oEls = generator.getNodesByTypes( self.project[ 'data' ], 'elements/element' )
        for oEl in self.oEls:
            oEl[ 'items' ] = self._getItems( oEl )

            # recupere l'icone
            oEl[ 'icon' ] = 'fa-' + oEl[ 'items' ][ 'icon' ][ 'value' ][ 'style' ] + ' fa-' + oEl[ 'items' ][ 'icon' ][ 'value' ][ 'icon' ]
            oEl[ 'color' ] = oEl[ 'items' ][ 'icon' ][ 'value' ][ 'color' ]

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

            # controle la presence de "on-create"
            oOnCreates = []
            for oOnCreate in generator.getNodesByTypes( oEl, 'element/on_create_add/element_on_create_add' ):
                oRefItems = self._getItems( oOnCreate )
                if 'ref_element' not in oRefItems:
                    continue

                # recupere l'element
                oRefNodeEle = generator.getNodeById( oRefItems[ 'ref_element' ][ 'value' ], self.project[ 'data' ] )
                if not oRefNodeEle:
                    continue
                oOnCreates.append( { "id": oRefNodeEle[ 'text' ], "text": self._getItems( oRefNodeEle )[ 'desc' ][ 'value' ] } )

            oEl[ 'on-create-add' ] = oOnCreates

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