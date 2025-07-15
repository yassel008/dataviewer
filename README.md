
# Visor de Datos Gubernamentales

Aplicación web desarrollada en Flask para visualizar datos desde archivos `.txt`.

## Cómo usar

1. Construir imagen Docker:

```
docker build -t gov-data-viewer .
```

2. Ejecutar:

```
docker run -p 5000:5000 gov-data-viewer
```

3. Acceder a `http://localhost:5000`.

## Kubernetes

Usa los manifiestos en la carpeta `k8s/` para desplegar en un clúster local o en la nube.
