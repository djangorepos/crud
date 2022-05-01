CRUD application for user management. Running on server AWS EC2, ip 54.167.96.246
Documentation on swagger:
http://54.167.96.246/swagger/

User fields:
- username (unique)
- first_name
- last_name
- email (valid email address.)
- password (min length 8. at least one number and one letter )
- type ("Admin", "Driver')

Deployment:
- docker-compose up --build
- docker exec -it  test_repo_1_web_1 python manage.py collectstatic --noinput
- docker exec -it  test_repo_1_web_1 python manage.py migrate
- docker-compose up

