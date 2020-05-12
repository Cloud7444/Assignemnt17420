#Log

sqlite file need to be backup

3.25 Success deploy web app on cloud 

Date : 3.27
log 1
Accident delete the template folder, try to put all things put but page show "TemplateDoesNotExist". View.py code look for index.html. But error looking for question_index.html
Estimate : 20mins
Solution: urls.py typo mistake. missing "/" after the path.
Actual time taken: 5hours

Date : 3.28
log 2
Doing heroku deploy. Link to the github and has master branch. Change code eg.'hello' to 'hey'. Page shows hey correctly. But try to clone everything from heroku. The code still remain 'hello'.
Estimate : 1 hour
Solution: Current project has two different remote git. Figure out that when using clone from heroku. Actually clone from the heorku get remote not the github one.
Actual time taken : 4hours

Date 4.1
log 3
Deploy heroku for add-on. Didn't vertify the account and could not add addons.
Estimate : 1 hour
Solution : https://help.heroku.com/WZIGJX28/why-do-i-need-to-have-a-verified-account-for-a-free-addon-or-custom-domain
Need to verified account before using add-on
Actual time taken : 10mins

Date 4.3
log 4 
Has problem when installing psycopg2 -- that error occurs when it can't find the SSL library (the library not found -lssl error), so you have to tell it where it is on MacOS
Estimate : 1 hour
Solution : env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip3 install --upgrade psycopg2
Actual time taken : 30mins

Date 4.5
log 5
deploy heroku. Procfile xxxx.wsig  --- xxxx must the project name
Estimate : 10mins 
Solution : change the Procfile file.  XXXXX.wsig to Assignment1.wsig.
Actual time taken : 2 hours

Date 4.5
log6 
after app deploy on heroku. OperationalError occur due to hasnt run migrate. -- notice database is empty at this point(running on local)
Estimate : 10mins
Solution : Remote run bash on heroku. Run python manage.py makemigrations and migrate.
Actual time taken : 10mins

Date 4.11
log6
In project repo forgot to link the heroku git. Can not remote access from terminal.
Estimate : 10mins
Solution : Add heroku git to project.
Actual time taken : 5mins 

Date 4.15
log7
Figure out that reflect diff pages. In project urls should path('',included(app.urls)). What this does it is basically import the app.urls setting and accroding the app.urls settting to open the link. I made a mistake that I just put   path('', home) in the project url.py that's only will work on the project folder. will not turn into the app folder. By chaning to path('', include("app.urls")), #default index page. then everything works fine
Estimate : 30mins 
Actual time taken : 2hours

Date 4.16
log8
remote run heroku install pillow, but everything run migrate still throw the same erros missing the pillow. 
Solution : Add pillow==7.1.1 to requirement.txt
Estimate : 1min
Actual time taken:1 hour

Date 4.20
log9
Make user profile model, set default pic for new user.

log10 
set form filter, querySet.
