# Django SmartBase Admin Demo



📦 This is a demonstration project for [Django SmartBase Admin](https://github.com/SmartBase-SK/django-smartbase-admin), a modern and customizable Django admin interface built for real-world applications.

> 🔗 **Documentation**:  
> https://github.com/SmartBase-SK/django-smartbase-admin-docs

---

## ❓ About

This demo shows how to:

- Configure and register custom admin views using `django-smartbase-admin`
- Structure menu items and dashboards
- Use dynamic filtering, and custom UI components
- Integrate real-world models (catalog, product, purchase etc.) in a modern admin

## ⚙️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/SmartBase-SK/Django-SmartBase-Admin-Demo.git
cd Django-SmartBase-Admin-Demo
```
2. **Install requirements**

```bash
pip install -r requirements.txt
OR
rye sync
```
**3. Create .env file**:
```
DOCKER_DEV_SETUP=1
ENVIRONMENT=dev
PGBOUNCER_HOST=localhost
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=demo
POSTGRES_USER=demo
POSTGRES_PASSWORD=password
REDIS_HOST=localhost
REDIS_PORT=6379
LOGSTASH_HOST=logstash
DJANGO_SETTINGS_MODULE=project.settings
DB_HOST=db
DB_USER=demo
DB_NAME=demo
DB_PASSWORD=password
PGDATA=pgdata
```
**4. Run docker containers**

```bash
docker compose up -d
```
**5. Prepare database**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
**6. Run server**

```bash
python manage.py runserver
```

Then open http://localhost:8000/sb-admin/ in your browser.