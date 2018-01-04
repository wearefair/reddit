FROM rcarmo/alpine-python:3.6-onbuild
# Create app directory
WORKDIR /usr/src/app
# Install app dependencies
COPY . ./  
RUN pip install -r requirements.txt
# Bundle app source
EXPOSE 5000 
CMD ["gunicorn", "-w","1","-b","0.0.0.0:5000","--threads","1","reddit.wsgi:app"]
