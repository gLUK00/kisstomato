import datetime

def printShowTime(timestamp):
    """
    Convertit un timestamp Unix en chaîne de caractères formatée.
    
    Args:
        timestamp (int): Timestamp Unix en secondes
        
    Returns:
        str: Date formatée "jj/mm/aaaa hh:mm:ss"
    """
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%d/%m/%Y %H:%M:%S")
