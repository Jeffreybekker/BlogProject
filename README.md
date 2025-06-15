# BlogProject

## Description
<p>This is a simple Django blog application. On the homepage, you'll see a list of all blog posts with their titles and a short preview. Clicking on a blog post will take you to the full article.</p>

## Table of contents
* [BlogProject](#blogproject)
  * [Description](#description)
  * [URL Endpoints](#url-endpoints)
  * [Installation](#installation)
  * [Updating Blog](#updating-blog)
  * [Screenshots](#screenshots)

## URL Endpoints
<ul>
  <li>http://127.0.0.1:8000/blog/</li>
  <li>http://127.0.0.1:8000/blog/&lt;id&gt;/</li>
  <li>http://127.0.0.1:8000/admin/</li>
</ul>

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Jeffreybekker/BlogProject.git
    cd BlogProject
    ```

2. Create a virtual environment and install dependencies:
    If you do not have pipenv installed, install it first:
    ```bash
    pip install pipenv
    ```
    Then install dependencies using the `Pipfile` and `Pipfile.lock`:
    ```bash
    pipenv install
    ```
    This will also create and set up the virtual environment.

3. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

4. Create a `.env` file in the root of the project with the following content:
    ```env
    SECRET_KEY='your_secret_key'
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    WEATHER_API_KEY='your_api_key'
    ```

5. Generate a Django `SECRET_KEY` (optional):
    Start the Python shell:
    ```bash
    python
    ```
    En voer het volgende in:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
    Kopieer de gegenereerde sleutel en gebruik die bij `SECRET_KEY` in je `.env`-bestand.

6. Run the development server:
    ```bash
    python manage.py runserver
    ```
    Bezoek vervolgens: [http://127.0.0.1:8000/blog](http://127.0.0.1:8000/blog)

## Updating Blog
<p>Log in op het admin panel via <a href="http://127.0.0.1:8000/admin">http://127.0.0.1:8000/admin</a>.</p>
<p>Klik op <strong>Posts</strong> en voeg een nieuwe blog toe via <strong>ADD</strong>.</p>
<p>Om een blog te verwijderen klik je op <strong>DELETE</strong>.</p>
<p>Ga naar <a href="http://127.0.0.1:8000/blog">/blog</a> om alle blogs te bekijken.</p>

## Screenshots
![Homepage Screenshot](https://github.com/user-attachments/assets/f0ff613b-b29e-44c3-a62d-b8db8dfcd285)
![Post Detail Screenshot](https://github.com/user-attachments/assets/ce1a417c-436e-4af4-b7bb-b3df9c334e06)
![Admin Panel Screenshot](https://github.com/user-attachments/assets/02e29bf2-a51b-4759-a0d8-92f9ec050f73)
