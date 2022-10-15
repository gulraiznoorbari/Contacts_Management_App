<div align="center">
<h1>Contacts Management App</h1>
</div>

## Installation steps

Install Virtual Environment

```
pip install virtualenv
```
#### Run the below commands in the project directory:

Create Virtual Environment 

```
python -m venv <venv-name>
```

Activate the virtual environment

```
<venv-name>\Scripts\activate.bat
```

Clone the Repo and install the requirements

```
git clone https://github.com/gulraiznoorbari/Contacts_Management_App.git
cd Contacts_Management_App
pip install django
cd contacts_manager
python manage.py runserver
```

Create a Admin User

```
python manage.py createsuperuser
```
