cd ..
cd Software
cd Backend

SET softwareDir=%cd%
cd ..
cd ..
cd venv
cd Scripts

python.exe "%softwareDir%/runserver.py"
PAUSE