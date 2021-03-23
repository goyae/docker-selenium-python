FROM python:3.9.1-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /app

#install google-chrome
RUN apt-get update -y
RUN	apt-get install -y unzip
RUN	apt-get install -y vim
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable
 
#install selenium
RUN pip install selenium
 
#install ChromeDriver
ADD https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip
 
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

WORKDIR /code
