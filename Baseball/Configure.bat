virtualenv ..\Env
call ..\Env\Scripts\activate.bat
python -m pip install --upgrade pip==8.1.1
pip install -r REQUIREMENTS.txt

python manage.py migrate --noinput
