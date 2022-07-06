This is a self study about Django admin cook book: https://readthedocs.org/projects/django-admin-cookbook/downloads/pdf/latest/


I'm following all the rules, and the code are the same, type writing and sometimes copying.

Learning a lot this new feature for me, Django admin.

Awesome file uploads, filters to Models, Optimize querys, manage multiple admins pages, override the html page admin.

Everything is awesome, thanks for everybody sharing with me this knowledge






Usage

With Python 3.10 > installed in your computer

type 

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser 
 (follow instructions)
./manage.py runserver

go to 

http://127.0.0.1:8000/entity-admin/
or 
http://127.0.0.1:8000/event-admin/

and see the beauty of django admmin working