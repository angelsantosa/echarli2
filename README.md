Crear ambiente:
mkvirtualenv --python=/usr/bin/python3.4 echarli2_env
Cargar el ambiente:
source ~/.virtualenvs/echarli2_env/bin/activate
 
Instalación
  pip install --upgrade setuptools pip
  pip install path.py
  pip install BaseSettings
  pip install django-countries
  pip install jsonify
  pip install geopy
  pip install corsheaders
  pip install slugfield
  pip install django-slug-preview
  pip install sites
  pip install -r requirements/local.txt
 
 
Compilar CSS (se utiliza SASS  de Ruby)
sass --watch echarli2/static/sass/echarli.scss:echarli2/static/css/echarli.css
 
Iniciar el servicio:
./manage.py runserver 172.31.38.186:8000
