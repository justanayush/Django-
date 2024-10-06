# manage.py -- > starting point file, sets environment variables and other things , invokes system after deploying in production
# it runs first time , present in root level
# inside Django_Notes folder is called as Project Level or Project Folder
# cache.py -- optimization
# settings.py --> whole configuration is written here
# for static url to work we have to mention static directories to make sure static asset is loaded from a complete path {% load static %}
# when simply using load without confifuring settings.py and setting up the complete path ... it just takes the path like "<--- here its not complete --->/static/styles.css"
# manage.py is responsible for running of server and making of apps
# when we use manage.py startapp Django just creates the apps not install them , main project never have an idea that an app is created
# first step after this is to aware the main project about new app created
# urls.py in main project refers to sub urls.py in the apps
# control transfer is done to sub urls.py on the main urls.py file 
# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. --> we dont write sql directly django orm takes care of that ,due migrations are compoleted using python manage.py migrate , making tables for database kinda