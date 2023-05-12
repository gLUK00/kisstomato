virtualenv venv

rem python -m venv C:\Users\S31155\Documents\share_vm\si_macif\kisstomato\eel\venv

call ".\venv\Scripts\activate.bat"

Set "VIRTUAL_ENV=C:\Users\S31155\Documents\share_vm\si_macif\kisstomato\eel\venv"

rem lancement de l'application
rem pip install -r requirements.txt
python run.py

call ".\venv\Scripts\deactivate.bat"
