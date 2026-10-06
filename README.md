# AI-Assisted Box Selection System

## Overview

A Django-based system that recommends a suitable shipping box for
an order based on product dimensions and weight.

## Features

- Product management
- Box management
- Product dimension validation
- Weight capacity validation
- Lowest-cost suitable box recommendation
- Django admin interface
- Automated tests

## Technologies

- Python
- Django
- SQLite
- HTML
-CSS

## Project Structure

box_selection_system/
|__ Box_Selector/
|__ box_selector_app/
|__ AI_USAGE.md
|__ CHAT_TRANSCRIPT.md
|__ manage.py
|__ README.md
|__ TEST_CASES.md
|__ TEST_OUTPUT.md

## Setup

```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## What did i learn from this project?

What did I learn?

- I learned how to model products and boxes in Django.
- I understood how to validate dimensions and weight.
- I learned how to select the lowest-cost suitable box.
- I learned how to write and run Django test cases.
- I understood the importance of verifying AI-generated code before using it.