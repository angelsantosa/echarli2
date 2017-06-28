Crear ambiente:
================
<i>
mkvirtualenv --python=/usr/bin/python3.4 echarli2_env
</i>

Cargar el ambiente:
===================
<i>
source ~/.virtualenvs/echarli2_env/bin/activate
 </i>
 
Instalación
============
<i>
  pip install --upgrade setuptools pip
  pip install path.py
  pip install BaseSettings
  pip install django-countries
  pip install jsonify
  pip install geopy
  >pip install corsheaders
  >pip install slugfield
  pip install django-slug-preview
  pip install sites
  pip install -r requirements/local.txt
</i>
 
Compilar CSS (se utiliza SASS  de Ruby)
=======================================
<i>
sass --watch echarli2/static/sass/echarli.scss:echarli2/static/css/echarli.css
</i>

Iniciar el servicio:
=====================
./manage.py runserver 172.0.1.1:8000
