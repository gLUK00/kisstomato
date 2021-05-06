# simple_front


## DEV LOCAL : Lancement de vue ui
```
vue ui
```

## DEV LOCAL : developpement
```
npm run serve
```

## Compilation de l'image et génération des sources
```
docker build -t live . && docker run -v $(pwd)/output:/output live
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
