rem kisstomato-start-sh-a-start-user-code-kisstomato
rem kisstomato-start-sh-a-stop-user-code-kisstomato

virtualenv venv

call ".\venv\Scripts\activate.bat"

rem kisstomato-start-sh-b-start-user-code-kisstomato
rem kisstomato-start-sh-b-stop-user-code-kisstomato

pip install -r requirements.txt

rem definition du fichier de configuration
SET conf="configuration.json"

rem kisstomato-start-sh-c-start-user-code-kisstomato
rem kisstomato-start-sh-c-stop-user-code-kisstomato

python flask_app.py %conf%

rem kisstomato-start-sh-d-start-user-code-kisstomato
rem kisstomato-start-sh-d-stop-user-code-kisstomato

call ".\venv\Scripts\deactivate.bat"

rem kisstomato-start-sh-e-start-user-code-kisstomato
rem kisstomato-start-sh-e-stop-user-code-kisstomato
