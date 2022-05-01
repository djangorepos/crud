CRUD application for user management.
User fields:
- username (unique)
- first_name
- last_name
- email (valid email address.)
- password (min length 8. at least one number and one letter )
- type ("Admin", "Driver')

docker-compose build
docker run -it web python manage.py makemigrations
docker run -it web python manage.py migrate
docker run -it web python manage.py collectstatic
docker run -it web python manage.py createsuperuser(if you need django-admin)
docker-compose up