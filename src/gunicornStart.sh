gunicorn -b 0.0.0.0:80 --log-level=info --log-file /var/log/web.log hello:app
