
class nodeScript:
    def __init__(self, oNode):
        self.node = oNode

        # map les items
        self.values = {}
        for oItem in oNode[ 'li_attr' ][ 'items' ]:
            self.values[ oItem[ 'id' ] ] = oItem[ 'value' ]

    # recupere la description
    def getDesc(self):
        return self.values[ 'desc' ]
    
    # determine si la description doit etre affichee au demarrage
    def printDescOnStart(self):
        return 'print_desc' in self.values and self.values[ 'print_desc' ] == True