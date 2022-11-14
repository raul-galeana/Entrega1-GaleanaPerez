A. Se tiene una sola app home, dentro de la cual se contiene forms, models, urls y views.
B. Se tiens centralizados todos los templates en una carpeta templates, en la carpeta principal.
   - Para los templates, se tiene un template "padre", llamado base.html. En él, se encuentra el formato común para todos los demás templates, los cuales "heredan" del padre en el espacio:
        {% block mi_contenido %}
        {% endblock mi_contenido %}
   - Se usan clases basadas en vista para generar los views.
   - En el template ver_mascotas_cbv se incluye un buscador. Así mismo, se incluye la opción de editar y de eliminar los datos de la base de datos.
C. Se descargó una plantilla de startbootstrap, y se guardó en la subcarpeta static, dentro de home.
D. Para los formularios, se optó por crear una clase en forms, no en models. Así mismo, se usa la API de django para formularios, en vez de programar desde html.

En la página web, se cuenta con un inicio o home, una página para ver mascotas (con buscador) y otra para crearlas / darlas de alta.

--------------------------------------------
Integrantes del grupo:
1. Raúl Galeana
2. Yesica Perez