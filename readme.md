# Table of Contents
- [Introduction](#introduction)
- [Features I'm working on](#features-im-working-on)
- [Installation or Set Up](#installation-or-set-up)

## Introduction

- This website is a platform for video courses where users can register and pay for courses. After registering, users can select a course, proceed to payment, and then start watching the videos inside the website.
- The videos are securely stored on cloudinary.
- The payment system is powered by Paypal.

## Features Im working on

- Users ability to view their payment history.
- Users can track where they left off.
- Forgot password feature.

## Installation or Set Up

1. Clone repository using your method of preference (git clone or github desktop)
2. Create a new virtual environment: ```virtualenv env```
3. Activate your virtual environment: ```source env/Scripts/activate```
4. Install dependencies: ```pip install -r requirements.txt```
5. Generate a new SECRET_KEY for settings.py: ```from django.core.management.utils import get_random_secret_key```
6. Set up your database. You can create a new "db.sqlite3" and then: ```python manage.py makemigrations```
7. Migrate db: ```python manage.py migrate```
8. Create a new superuser: ```python manage.py createsuperuser```
9. Set up your media files.