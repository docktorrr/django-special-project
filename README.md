# django-special-project
Django project for creation of promo sites and services

## Consists of: ##
* Contest app - Users can post their works as text messages, images, videos etc. Other users can vote for these works
* Quiz app - Quiz has number of questions, each question has number of answers (correct/incorrect or with the points value)
* Question/answer app - User asks, expert/editor answers
* Publications app - Articles

## Installation ##
* Install requirements: pip install -r requirements.txt
* Create settings_local.py with database settings
* python manage.py syncdb --all
* python manage.py migrate
