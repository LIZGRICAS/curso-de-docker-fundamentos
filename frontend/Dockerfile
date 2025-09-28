# Usa la imagen base de Nginx para servir los archivos estáticos
FROM nginx:latest

# Copia el contenido de la carpeta frontend local al directorio HTML de Nginx
COPY /sitio /usr/share/nginx/html

# Exponer el puerto 80 para servir la aplicación
EXPOSE 80
