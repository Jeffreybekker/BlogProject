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
    ```

5. Generate a Django `SECRET_KEY`:<br>
    Start the Python shell:
    ```bash
    python
    ```
    And paste the following:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
    Copy the generated key and use it at SECRET_KEY in your .env-file.

6. Run the development server:
    ```bash
    python manage.py runserver
    ```
    Visit: [http://127.0.0.1:8000/blog](http://127.0.0.1:8000/blog)

7. Create superuser to be able to login in the Admin panel:
    ```
    python manage.py createsuperuser
    ```
    Simply follow the steps in the terminal. This login you'll use to access the Admin panel.

## Updating Blog
<p>Log in to the admin panel via <a href="http://127.0.0.1:8000/admin">http://127.0.0.1:8000/admin</a>.</p>
<p>Click on <strong>Posts</strong> and add a new blog post via <strong>ADD</strong>.</p>
<p>To delete a blog post, click on <strong>DELETE</strong>.</p>
<p>Go to <a href="http://127.0.0.1:8000/blog">/blog</a> to view all blog posts.</p>


## Screenshots
![Homepage Screenshot](https://github.com/user-attachments/assets/f0ff613b-b29e-44c3-a62d-b8db8dfcd285)
![Post Detail Screenshot](https://github.com/user-attachments/assets/ce1a417c-436e-4af4-b7bb-b3df9c334e06)
![Admin Panel Screenshot](https://github.com/user-attachments/assets/02e29bf2-a51b-4759-a0d8-92f9ec050f73)
