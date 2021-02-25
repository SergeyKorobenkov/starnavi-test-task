## Test task for StarNavi

### Deploy:
Use next steps to deploy it to your computer:
```
python -m venv venv 
source venv/Scripts/activate (or ". venv/bin/activate" for linux)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
After all it will be available at ```http://127.0.0.1:8000/```

## Available methods

### Work with users
```POST /auth/registration/```
```
form-data with:
    email: <email>
    username: <str>
    password: <str>
```
```POST /auth/login/```
```
form-data with:
    email: <email>
    username: <str>
    password: <str>
It return Bearer Token which need for work with service
```

```PUT /auth/pass-change/```
```
Bearer Token and form-data with:
    old_password: <str>
    new_password: <str>
    confirmed_password: <str>
```
### Work with posts
```POST api/new-post/```
```
Bearer Token and form-data with:
    text: <str>
```
```POST api/like-post/```
```
Bearer Token and form-data with:
    post_id: <int>
```

### Work with analytics
```GET api/analitics/```
```
Query Params:
    date_from: <YYYY-MM-DD>
    date_to: <YYYY-MM-DD>
```
```GET api/user-stats/```
```
Query Params:
    username: <str>
```