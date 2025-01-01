class nodeElement:
    
    def _getItems(self, oNode):
        oItems = {}
        if 'li_attr' in oNode and 'items' in oNode[ 'li_attr' ]:
            for o in oNode[ 'li_attr' ][ 'items' ]:
                oItem = {}
                for sI in o:
                    if sI == 'id':
                        continue
                    oItem[ sI ] = o[ sI ]
                oItems[ o[ 'id' ] ] = oItem
        return oItems