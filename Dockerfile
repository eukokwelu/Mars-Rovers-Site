FROM tiangolo/uwsgi-nginx-flask:python3.8
ENV STATIC_URL /static
ENV STATIC_PATH /app/mars_rover/static
COPY requirements.txt /tmp/

RUN Python -m pip install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

COPY . /app
