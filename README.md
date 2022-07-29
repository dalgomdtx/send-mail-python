# Enviar Correo con Python
Enviar correo electronico con archivo adjunto usando Python

El código base funciona con correos enviados usando el servicio de google a cualquier otro dominio.  
El código puede adaptarse para usar otros dominios con pequeñas modificaciones ( in progress )

## Primeras configuraciones
### Necesitas habilitar la verificación en 2 pasos de tu cuenta.
Se puede hacer accediendo a este apartado de [configuración](https://myaccount.google.com/signinoptions/two-step-verification) de Google.
____
### Necesitas la contraseña de 16 digitos que se usa en este código
Se obtiene accediendo al apartado de [contraseñas de aplicaciones](https://myaccount.google.com/apppasswords) de Google.  
Crear una nueva entrada personalizada con el nombre que tu desees.
- ![pass-app-01](https://user-images.githubusercontent.com/93104850/180913838-94132875-f027-408f-9c69-08fa3803e21f.png)
- ![pass-app-02](https://user-images.githubusercontent.com/93104850/180913897-efadf675-3e09-4cf1-bbdc-7d0fbdcdf67a.png)

En este ejemplo, la contraseña generada se guardo en una variable de entorno llamada "EMAIL_PASSWORD".  
Puedes escribir directamente tu contrañena en el código, reemplazando `os.environ.get('EMAIL_PASSWORD')` por tu contraseña en la linea 8
```sh
Antes:
  email_password = os.environ.get('EMAIL_PASSWORD')
  
Despues:
  email_password = 'tu contraseña'
```
> ## Recuerda NO compartir la clave, es privada.

Ahora todo lo que necesitas es clonar o descargar el repositorio, hacer las modificaciones necesarias y a ejecutar.


---

<p align="center">⭐️<a href="https://github.com/dalgomdtx"><b>DalgomdtX</b></a> :copyright: 2022</p>
