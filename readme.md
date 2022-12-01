# Running project

---

## 📢 **Installing Django with pip in a Virtual Environment.** 📢

1. Setup python on windows - <https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013>
2. Setup python on linux - <https://www.makeuseof.com/install-python-ubuntu/>
3. Setup python on mac - <https://www.dataquest.io/blog/installing-python-on-mac/#:~:text=Install%20Python%203%20with%20the%20Official%20Installer&text=First%2C%20download%20an%20installer%20package,Python%20installer%20on%20your%20Mac.>

---

### Install postgres database
* Create database called `kurasa-backend`

### Steps to setup kurasa project:

* Clone the project [click here](https://gitlab.com/inclusion/api-numbre-uno)
* Navigate to your project directory where we have manage.py file
* Create a virtual environment within the project directory using the python command that is compatible with your version of Python. We will call our virtual environment my_env.
```python
python3 -m venv my_env
```
* To install packages into the isolated environment, you must activate it by typing:
`Activating `python virtual environment.
```python
source my_env/bin/activate
```
Your prompt should change to reflect that you are now in your virtual environment. It will look something like:
```python
(my_env) root@rooname:~/config
```
* Installing project requirements. `Ensure you're terminal is opened in your project directory where we have requirements.txt file`
```python
pip install -r requirements.txt
```
* Paste this in your `.env` file found in `config/.env`
```python
EMAIL_HOST=smtp.zoho.com
EMAIL_HOST_USER=daniel@kurasa.co
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=daniel@kurasa.co
EMAIL_PORT=587
EMAIL_HOST_PASSWORD=3p3ez79RVyZg.5e

MODE=DEV
MEDIA_ROOT=media

DATABASE_URL1=sqlite:///db.sqlite3
DATABASE_URL=postgresql://postgres:Larry@98@localhost:5432/kurasa-backend

username=root
password=fpxNmvqkFvHnmxne4pnT

```
* Change database connection string in .env file above to meet your specifications.
```python
DATABASE_URL=postgresql://username:password@localhost:port/database-name
```
* Migrate the database (this example uses SQLite by default) using the migrate command with the manage.py application. Migrations apply any changes you have made to your Django models, to your database schema.
```python
python manage.py migrate
```
You will see something like this:
```python
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
```
* Then run your project 
```python
python manage.py runserver
```
* Open project in your browser. [click here](http://127.0.0.1:8000)