#
#solo_project
#techskill sets
# Python, flask framework,jinja2,postgresql,HTML/CSS

#Download and run flask app:
#command line:
$git clone git@github.com:ccx1010sky/solo_project.git
$cd solo_project

#Installation
solo_project$pip3 install Flask
solo_project$pip3 install python-dotenv
solo_project$pip3 install psycopg2

#Database
solo_project$brew install postgresql
solo_project$dropdb product_manager
solo_project$create product_manager
solo_project$psql -d product_manager -f product_manager.sql

#Start the app
solo_project$flask run






