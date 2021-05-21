apt update
apt-get install mysql-client libmysqlclient-dev
python3 -m pip install -r requirements.txt
cp ./misc/admin.py /usr/local/lib/python3.8/dist-packages/django_celery_monitor/admin.py
cp ./misc/managers.py /usr/local/lib/python3.8/dist-packages/django_celery_monitor/managers.py

echo "success"