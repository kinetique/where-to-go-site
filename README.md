# where-to-go-site
Homework for week 2 Web-Programming

The user can view the list of places, details of a specific place, add new places and choose a random place based on the rating.

### Features
View the list of places in the order of creation. 

- Detailed view of an individual place.

- Add new places via a form.

- Select a random place with a weight by rating.

- Anonymous session to save the selected places.

## Installation

Clone the repository:

```
git clone <repository_url>
cd <project_folder_name>
```

Create and activate a virtual environment:
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
Install Django:

```pip install django```

Apply migrations:

```python manage.py migrate```

Run the project:

```python manage.py runserver```

Open in browser: http://127.0.0.1:8000/