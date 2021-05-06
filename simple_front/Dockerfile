FROM node:lts-alpine

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN chmod 777 /app/build.sh

# generation dans le dossier /app/dist
CMD ["/app/build.sh"]
