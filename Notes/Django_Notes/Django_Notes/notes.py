# manage.py -- > starting point file, sets environment variables and other things , invokes system after deploying in production
# it runs first time , present in root level
# inside Django_Notes folder is called as Project Level or Project Folder
# cache.py -- optimization
# settings.py --> whole configuration is written here
# for static url to work we have to mention static directories to make sure static asset is loaded from a complete path {% load static %}
# when simply using load without confifuring settings.py and setting up the complete path ... it just takes the path like "<--- here its not complete --->/static/styles.css"