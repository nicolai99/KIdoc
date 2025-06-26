# KIdoc

## installation

docker-compose build \
docker-compose up

## Notes

### Django

Connect to Django Container (default name django)\
```docker exec -it django  bin/sh```

### Migration

```
python manage.py migrate
python manage.py loaddata data.json
python manage.py createsuperuser
```

### API Key

Place the Google API developer key in your ```.env``` file.

### Access

http://localhost:5173/home

### links

* https://primevue.org/setup/
* https://axios-http.com/docs/intro
* https://django-ninja.dev/
* https://docs.djangoproject.com/en/5.2/
* https://tailwindcss.com/