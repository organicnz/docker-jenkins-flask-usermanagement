FROM python:3.7.6

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt
RUN pip3 install flask

# Bundle app source
COPY . /usr/src/app

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["pytest -v"]
