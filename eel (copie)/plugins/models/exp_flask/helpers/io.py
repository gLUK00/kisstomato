import json, base64

# creation d'un fichier JSON
def createJsonFile( file, oJson ):
    def dumper(obj):
        try:
            return obj.toJSON()
        except:
            if isinstance( obj, bytes ):
                return base64.b64encode( obj ).decode( 'utf-8' )
            return obj.__dict__
    try:
        f = open( file, "w", encoding="utf-8" )
        f.write( json.dumps( oJson, default=dumper, indent=4 ) )
        f.close()
    except Exception as e:
        print( 'putJsonOnFile : ' + file + ' : ' + str( e ) )
        return False

    return True