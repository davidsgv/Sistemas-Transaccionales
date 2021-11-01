cd ..
cd software

SET softwareDir=%cd%
cd ..
cd venv
cd Scripts

python.exe "%softwareDir%/runserver.py"
PAUSE