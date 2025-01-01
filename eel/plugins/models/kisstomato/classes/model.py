from core import generator, nodeElement

class model(nodeElement):
    oRoots = []
    def __init__(self, oProject):
        self.project = oProject
        self.oRoots = []
        
        # recupere les noeuds root
        # controle la presence des references enfants
        oTmpRoots = generator.getNodesByTypes( self.project[ 'data' ], 'roots/root' )
        for oTmpRoot in oTmpRoots:
            oItems = self._getItems( oTmpRoot )
            if 'ref_element' not in oItems:
                continue
            oRoot = { 'id': oTmpRoot[ 'text' ].lower() }
            
            # recupere le noeud cible
            oRefNode = generator.getNodeById( oItems[ 'ref_element' ][ 'value' ], self.project )
            if not oRefNode:
                continue
            oRoot[ 'text' ] = oRefNode[ 'text' ]
            if 'icon' in oRefNode:
                oRoot[ 'icon' ] = oRefNode[ 'icon' ]
            if 'color' in oRefNode:
                oRoot[ 'color' ] = oRefNode[ 'color' ]
            
            # pour tous les types d'enfants
            sTypes = ''
            oChilds = generator.getNodesByTypes( oTmpRoot, 'link_childs/link_child' )
            for oRefChild in oChilds:
                oRefItems = self._getItems( oRefChild )
                if 'ref_element' not in oRefItems:
                    continue
                
                # recupere le type
                oRefNodeType = generator.getNodeById( oRefItems[ 'ref_element' ][ 'value' ], self.project )
                if not oRefNodeType:
                    continue
                if sTypes != '':
                    sTypes += ', '
                sTypes += '"' + oRefNodeType[ 'text' ].lower() + '"'
            oRoot[ 'children-type' ] = sTypes
            
            self.oRoots.append( oRoot )
    
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
