
#Job Application Simplificator

##To run the project

 1. Unpack the archive: `tar -xf trip_constructor.tar.gz`
 2. Create virtual environment: `cd trip_constructor` `mkdir .env` `virtualenv .env`
 3. Activate virtual environment: `source .env/bin/activate`
 4. Install required packages: `pip install -r pip_requirements.txt`
 5. Create database: `python manage.py syncdb`
 6. Run project: `python manage.py runserver`
 7. Open browser: http://127.0.0.1:8000
