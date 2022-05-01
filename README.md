CRUD application for user management.
User fields:
- username (unique)
- first_name
- last_name
- email (valid email address.)
- password (min length 8. at least one number and one letter )
- type ("Admin", "Driver')

Deployment:
- docker-compose up --build
- docker exec -it web python manage.py collectstatic --noinput
- docker exec -it web python manage.py migrate
