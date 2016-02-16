
#Job Application Simplificator

##To run the project

 1. Clone project: `git clone https://github.com/kate-v-stepanova/JAS.git`
 2. Navigate to the directory: `cd JAS`
 3. Create virtual environment with [conda](#conda) or [virtualenv](#virtualenv):
 4. Install required packages: `pip install -r pip_requirements.txt`
 5. Create database: `python manage.py syncdb`
 6. Run project: `python manage.py runserver`
 7. Open browser: http://127.0.0.1:8000

###<a name="conda"></a>Create virtual environment with conda:
1. Create virtual environment: `conda create -n jas python=2.7`
2. Activate virtual environment: `source activate jas`
 
###<a name="virtualenv"></a>Create virtual environment with virtualenv:
1. Create directory: `mkdir .jas`
2. Create virtual environment: `virtualenv .jas`
3. Activate virtual environment: `source .jas/bin/activate`
