FROM python:latest
RUN mkdir -p /usr/local/src/assg
WORKDIR /usr/local/src/assg

RUN mkdir -p static
RUN mkdir -p templates
RUN mkdir -p Output
ENV ak 1
ENV sak 1
ADD app.py .
ADD functions.py .
ADD Usernames.txt .
ADD static static/.
ADD Templates templates/.

RUN pip install flask
RUN pip install pandas
RUN pip install sklearn
RUN pip install scipy
RUN pip install boto
EXPOSE 80
CMD ["sh","-c","python /usr/local/src/assg/app.py ${ak} ${sak}"]
