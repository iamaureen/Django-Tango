https://www.andreagrandi.it/2016/09/28/creating-production-ready-api-python-django-rest-framework-part-1/
[gives a demo of get method and post method]

1.create application, create app called "core" and register in settings.py under INSTALLED_APPS

2. write models and migrate using the following command
python manage.py makemigrations core
python manage.py migrate core

3. create serializers 

4. create views in views.py: add sql code and connect serializer code
				with each model

<views can be written in two more different ways (check the links)
- APIView
- ListAPIView>

5. Now we need to expose this logic to the outer space, which is done via url 
routers: we have to define mappings from http request addresses to the views 
controllers) (url will change wrt views)

6. run server: python manage.py runserver
http://127.0.0.1:8000/products/ should return an empty list as of now

7. Insert data manually 

8. run server again, http://127.0.0.1:8000/products/ will now return a json
with the sets of values just inserted.

9. use postman to post data
method: post
url: http://127.0.0.1:8000/products/
body:
name: Salamino
description: Salamino Piccante
price: 10.50

if successful, it should return the json of this entry, check using get method using the same url

10. to check database:
install DB browser for SQLite
navigate to django project and open the db.sqlite3 database


