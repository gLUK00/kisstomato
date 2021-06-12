FROM node:lts-alpine

# définit le dossier 'app' comme dossier de travail
WORKDIR /app

# copie 'package.json' et 'package-lock.json' (si disponible)
#COPY ./package*.json ./

# copie les fichiers et dossiers du projet dans le dossier de travail (par exemple : le dossier 'app')
#COPY . /app
ADD . /app

# installe les dépendances du projet
RUN npm install -g @vue/cli
#RUN npm install --global vuetype
#RUN npm install

# construit l'app pour la production en la minifiant
#RUN npm run build
#RUN npm run dev

EXPOSE 8080 8000

#CMD npm run serve ; vue ui
CMD ["sh","-c","npm run serve & vue ui"]
#CMD [ "http-server", "dist" ]

