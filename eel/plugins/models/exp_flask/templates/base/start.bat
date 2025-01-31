virtualenv venv

call ".\venv\Scripts\activate.bat"

pip install -r requirements.txt
python flask_app.py

call ".\venv\Scripts\deactivate.bat"
