# BizAPP development

## Run project
1) Create and switch to conda environment

```
conda create -n <name> python=3.10.9
conda activate <name>
```

2) Install dependencies

```
pip install -r requirements.txt
```

3) go to bizapp/settings.py

4) change config

  
  ```
    DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'bizapp',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': HOST_NAME,  
        'PORT': PORT_NUMBER,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
  ```

5) Make and Run migrations (for each app i think)

```
python manage.py makemigrations user_onboard
python manage.py migrate user_onboard 
```

6) Run development server

```
python manage.py runserver
```

7) Available urls

| url | page | 
|----------|----------|
| / | login page | 
| register/user/1 | onboard step 1 |
| register/user/2 | onboard step 2 |
| register/user/3 | onboard step 3 |
| dashboard | app dashboard |
| dashboard/account-setup | opening balances |
| dashboard/bank/create | create bank account |
| dashboard/office/create | create office |
| dashboard/staff/create | create staff |
| dashboard/product/create | create product |
| dashboard/loan/create | create loan |
| dashboard/software-cost/create | create software cost |
| dashboard/owner-equity/create | create owner equity |



 
