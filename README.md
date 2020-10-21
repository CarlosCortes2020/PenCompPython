# Introducción al pensamiento computacional con Python.
## En este repositorio colocaré información y apuntes.
### El proyecto  incluirá una pagian WEB en GitHub Pages.

ssh-keygen -t rsa -b 4096 -C "cicc81@gmail.com"

Siguente paso revisar la llave publica

ssh-rsa AAAAB3NzaC...dw== cicc81@gmail.com

Verificando si el proceso SSh esta corriendo
eval $(ssh-agent -s)

Agregar la llave al servidor
ssh-add ~/.ssh/id_rsa

En GitHub en la opcion settings->SSh and GPG keys->
crear nueva llave y copiar código de llave publica.

---------

En GitHub vamos al repositorio y en la seccion Code->Clone->SSH copiamos el enlace, y en la terminal ejecutamos:

cd al directorio del proyecto de interes

ejecuta...

git remote -v y muestra la ruta de origin para fetch y push

origin  git@github.com:CarlosCortes2020/PenCompPython.git (fetch)
origin  git@github.com:CarlosCortes2020/PenCompPython.git (push)

Una vez verificadas las rutas, ejecutamos comando

git rmeote set-url origin git@github.com:CarlosCortes2020/PenCompPython.git

donde la ultima url es la ruta con SSH


###End
