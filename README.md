# 7420_Assignemnt1

This project is going to make a web application smilar with instagram.

--sqlite file need to be backup
--3.25 Success deploy web app on cloud 



##Log
##log 1
Accident delete the template folder, try to put all things put but page show "TemplateDoesNotExist". Weired : View.py code look for index.html. But error looking for question_index.html

##log 2
Doing heroku deploy. Link to the github and has master branch. Change code eg.'hello' to 'hey'. Page shows hey correctly. But try to clone everything from heroku. The code still remain 'hello'.

##log 3
Deploy heroku for add-on. Didn't vertify the account and could not add addons.

##log 4 
Has problem when installing psycopg2 -- that error occurs when it can't find the SSL library (the library not found -lssl error), so you have to tell it where it is on MacOS

##log 5
deploy heroku. Procfile xxxx.wsig  --- xxxx must the project name

##log6 
after app deploy on heroku. OperationalError occur due to hasnt run migrate. -- notice database is empty at this point(running on local)

##log6
In project repo forgot to link the heroku git. Can not remote access from terminal.

##log7
Figure out that reflect diff pages. In project urls should path('',included(app.urls)). What this does it is basically import the app.urls setting and accroding the app.urls settting to open the link. I made a mistake that I just put   path('', home) in the project url.py that's only will work on the project folder. will not turn into the app folder. By chaning to path('', include("app.urls")), #default index page. then everything works fine

##log8
remote run heroku install pillow, but everything run migrate still throw the same erros missing the pillow. 
Solution : Add pillow==7.1.1 to requirement.txt
