FROM python:3.9.0

WORKDIR /home/

RUN echo 'eufnckgisk'

RUN git clone https://github.com/limajin/gis_1.git
# 깃허브 주소 code 누르면 복사가능함

WORKDIR /home/gis_1/

#RUN echo "SECRET_KEY='django-insecure-yz!89n1nafiln7zc=cti#8(&7&(zff3_tmbo58yu267fs$wj-m'" > .env
## .env 파일에 있는 거 복 붙

RUN pip install -r reqirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient


EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=gis_1.settings.deploy && python manage.py migrate --settings=gis_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_1.settings.deploy gis_1.wsgi --bind 0.0.0.0:8000"]
# 꼭 쌍따옴표로 해줄 것