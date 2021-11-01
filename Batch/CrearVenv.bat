cd ..
RD /S venv

echo instalar virtual env
PAUSE
call pip install virtualenv && call virtualenv venv

echo paquetes de instalacion
PAUSE
cd venv && ^
cd scripts && ^
call python.exe -m pip install flask==1.1.2 && ^
call python.exe -m pip install pyodbc && ^
call python.exe -m pip install Flask-Sqlalchemy
PAUSE