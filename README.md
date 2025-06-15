# Blog

## Description
<p>You can find all the blogs on the main page. It gives a title of the blog and a short preview of what is written inside the blog. If you want to read more, you have to click on the blog and you'll be redirected to the selected blog.</p>

## Table of contents
* [Blog](#blog)
  * [Description](#description)
  * [Url Endpoints](#url-endpoints)
  * [Installation](#installation)
  * [Updating Blog](#updating-blog)
  * [Screenshots](#screenshots)

## URL Endpoints
<ul>
  <li>http://127.0.0.1:8000/posts/</li>
  <li>http://127.0.0.1:8000/posts/id</li> (id = number)
  <li>http://127.0.0.1:8000/admin/</li>
</ul>

## Installation
1. Clone the Repository:
```
git clone https://github.com/Jeffreybekker/BlogProject.git
cd BlogProject
```
2. Create a virtual environment and install dependencies:
If you do not have pipenv installed, then run first:
```
pip install pipenv
```
Install dependencies from Pipfile and Pipfile.lock:
```
pipenv install
```
This also creates a virtual environment.
3. Activate the virtual environment:
```
pipenv shell
```
4. Create .env-file in the root of the project with the following:
```
SECRET_KEY='your_secret_key'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```
5. Generate Django SECRET_KEY:
Start de python shell:
```
python
```
And then run:
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Copy the generated secret key and paste it at SECRET_KEY from your .env-file.
6. Run the server:
```
python manage.py runserver
```
## Updating Blog
<p>Login in on the admin panel.</p>
<p>Then click on Posts and ADD.</p>
<p>You can also delete a blog by clicking on DELETE.</p>
<p>Visit <a href="http://127.0.0.1:8000/posts">posts</a> to see all the updated content.</p>

## Screenshots
![image](https://github.com/user-attachments/assets/f0ff613b-b29e-44c3-a62d-b8db8dfcd285)
![image](https://github.com/user-attachments/assets/ce1a417c-436e-4af4-b7bb-b3df9c334e06)
![image](https://github.com/user-attachments/assets/02e29bf2-a51b-4759-a0d8-92f9ec050f73)
