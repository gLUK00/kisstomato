import os
from core import config

# affichage de la fenetre d'enregistrement sous
def saveAs( dialog_title_text, ext, initialfile_name ):
    """
    Original: Opened a native 'save as' dialog.
    New: Constructs a potential full server-side path. 
    The actual file saving/download is handled by the calling Flask route and browser.
    'dialog_title_text' is the original dialog title, now mostly for logging.
    'initialfile_name' is the suggested base name for the file.
    Returns a constructed filename string (e.g., /path/to/base/initialfile_name.ext).
    """
    print(f"Warning: core.app.saveAs called. Dialog title was '{dialog_title_text}'. This function no longer shows a GUI dialog.")
    print(f"It will construct a path based on initialfile_name: '{initialfile_name}' and ext: '.{ext}' within path_base: '{config.getPathBase()}'")
    
    filename_with_ext = initialfile_name
    if ext and not initialfile_name.endswith(f".{ext}"):
        filename_with_ext = f"{initialfile_name}.{ext}"
    
    constructed_path = os.path.join(config.getPathBase(), filename_with_ext)
    # Ensure the directory exists if we were to write here, though this function itself doesn't write.
    # os.makedirs(os.path.dirname(constructed_path), exist_ok=True)
    return constructed_path

# affichage de la fenetre de selection d'un repertoire
def setDir( dir_path_from_client ):
    """
    Original: Opened a native 'select directory' dialog, using 'text' as initialdir.
    New: Accepts a directory path string provided by the client.
    Can perform validation on the path.
    Returns the directory path string.
    """
    print(f"core.app.setDir received path: {dir_path_from_client}")
    # Optional: Add validation
    # if not os.path.isdir(dir_path_from_client):
    #     print(f"Warning: Provided path '{dir_path_from_client}' is not a valid directory or not accessible.")
    #     return None # Or raise an error
    return dir_path_from_client

# affichage de la fenetre de selection d'un fichier
def setFile( file_path_from_client, ext ):
    """
    Original: Opened a native 'select file' dialog, using 'text' as dialog title and 'ext' for filter.
    New: Accepts a file path string provided by the client and an expected extension.
    Can perform validation on the path and extension.
    Returns the file path string.
    """
    print(f"core.app.setFile received path: {file_path_from_client}, expected extension: .{ext}")
    # Optional: Add validation
    # if not os.path.isfile(file_path_from_client):
    #     print(f"Warning: Provided path '{file_path_from_client}' is not a valid file or not accessible.")
    #     return None # Or raise an error
    return file_path_from_client
