ref link :: https://docs.djangoproject.com/en/1.11/intro/

1) create project called "webpoll", create app called "poll", add it in the settings.py under "INSTALLED_APPS"

2) To start with, create a simple view, and associated url to access it from the browser
go to polls/urls.py and add
The next step is to point the root URLconf at the polls.urls module.
go to webpoll/urls.py and add

At this point run the server, and go to http://127.0.0.1:8000/polls/
you should see "Hello, world. You're at the polls index."

3) Database setup, write models for it
and the cmd prompt, python manage.py makemigrations polls
python manage.py migrate

for each time any change any models, these two commands should be used

4) create superuser
python manage.py createsuperuser

5) Run the server again, and go to http://127.0.0.1:8000/admin/
using the crdentials created on step 4, login.
This allows us to use a default interface for the models - to create/update/delete items in the database

6) But "poll" app is not shown, because we need to register it
go to polls/admin.py and register the model

add few questions

7) write some more views, check views.py

8) wire these new views into polls.urls

9) to demo templates, change the initial index view in view.py

10) add index.html in polls/templates/polls and paste the code;
update index.html so the value is passed from index view to the index.html template

so the flow:
http://127.0.0.1:8000/polls/ ->shows the list of questions passed from index view
index.html shows the list of questions in href format
when clicked, it is redirected to http://127.0.0.1:8000/polls/1/ or http://127.0.0.1:8000/polls/<question_id>/ format
this url is matched in urls.py and then associated view thats detail view from views.py is called

11) raising a 404 error
modify the view as shown
before, detail view just showed an HTTPResponse with the question_id
now using question_id it is extracting the question from the database
then passing it into a new html

12) handle simple form, re-write detail.html as shown
register choices in the admin, and add choices for each question

now the flow:
http://127.0.0.1:8000/polls (index.html) : shows the list of qustions
click any question: http://127.0.0.1:8000/polls/1 (detail view, detail.html) : shows the heading of the question, and shows choices for question to vote
click vote: http://127.0.0.1:8000/polls/1/vote (vote view which redirects to result view)

