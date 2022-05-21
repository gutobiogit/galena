FROM python:3.8-alpine
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
# install bash in the alpine image
RUN apk add --no-cache bash
# copy every content from the local file to the image
COPY . /app
# make start script executable
RUN chmod +x /app/start.sh
# configure the container to run in an executed manner
CMD /app/start.sh
