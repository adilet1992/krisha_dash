FROM python:3
WORKDIR /usr/src/app
COPY . .
EXPOSE 8050
RUN pip3 install -r requirements.txt
CMD python krisha_dash.py