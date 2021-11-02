cd ..
cd venv
cd Scripts
call activate

SET VenvDir=%cd%
cd ..
cd ..
cd Software
cd Front

python -m http.server 8081
PAUSE