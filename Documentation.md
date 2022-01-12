# Documentation
## Inside App Folder
### migrations
Contains records of the changes done on the database.
### templatetags
File are used to render or perform operations on the frontend data.
### admin
Used for registering tables in the admin UI.
### apps
To load the INSTALLED_APPS and setup signals
### consumers
Has the server for the websocket communication
### models
Used to define tables and their attributes.
### signals
Signals the websocket server in consumers when database is changed.
### views
Contains functions that the url redirect to and other APIs.
## Inside Proj Folder
### asgi
To start an Asynchronous Server Gateway Interface for event driven server.
### routing
URL routing for the ASGI views(classes in app/consumers.py).
### settings
Has required settings to run the server.
### urls
URL routing for the WSGI views.py functions.
### wsgi
To start a Web Server Gateway Interface for generic web development.
## Inside Static Folder
### css
Icons, mainstyle, w3 and materialize css files all pages.
### js
Main script for all pages and downloaded jquery file.
### fonts
Fonts for templates.
### images
Contain logo image.
### channels
Contains the code to create websocketbridge.
## Inside Templates Folder
### matches
 * Matchs list page.
 * Perform CRUD operations on matches.
### tournaments
 * Tournaments list page.
 * Perform CRUD operations on tournaments.
### teams
 * Teams list page.
 * Perform CRUD operations on teams.
### scorecard
 * Scorecard page for a match.
 * Live Section
 * Commentary Section
### comment
 Live comments entry page. 
### login
 Login page for organizer and commentator. 
### home
 Crimpulse Home page. 
### matchstart
 Start a match page. 
### Components
 Contains html components used by other pages.
## Other Files
### manage
 Tool for executing the Django-specific tasks like starting a new app within the project and running the development server.
 ### Procfile
 Specifies the commands that are executed by the app on startup in Heroku.
 ### requirements
 Contains the list of modules required to run the project.
 ### runtime 
 Specifies the runtime enviroment and its version. 
