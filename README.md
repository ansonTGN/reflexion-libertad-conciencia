# Cuando las ideologías piensan por nosotros

Sitio web editorial estático, adaptable a móviles, con el texto completo del ensayo y enlaces al artículo original publicado en *La Razón*.

## Contenido del proyecto

- `index.html`: artículo completo, HTML semántico y metadatos para compartir.
- `assets/style.css`: diseño responsive, modo oscuro y estilos para imprimir.
- `assets/site.js`: alternancia claro/oscuro, indicador de progreso y copia de enlace.
- `assets/favicon.svg`: icono vectorial.
- `netlify.toml`: despliegue y cabeceras de seguridad.
- `robots.txt`: permiso de rastreo.
- `.gitignore`: archivos que no deben versionarse.
- `build_page.py`: script que regenera `index.html` desde el contenido incorporado (opcional; la web ya está compilada).

## 1. Previsualización en Ubuntu

Desde la carpeta del proyecto:

```bash
python3 -m http.server 8000
```

Abre `http://localhost:8000` en tu navegador. Para detener, `Ctrl+C`.

## 2. Publicar el proyecto en GitHub

```bash
cd reflexion-libertad-web

git init
git add .
git commit -m "Publicar ensayo sobre libertad de conciencia"
git branch -M main
```

### Opción A: GitHub CLI (`gh`)

```bash
gh auth status
# Si hace falta: gh auth login

gh repo create reflexion-libertad-conciencia --public --source=. --remote=origin --push
```

La opción `--public` publica los archivos fuente. Sustituye por `--private` si prefieres un repositorio privado; Netlify necesita autorización para conectarse.

### Opción B: repositorio creado desde la web de GitHub

1. Crea en GitHub un repositorio vacío llamado `reflexion-libertad-conciencia` (sin README, licencia ni .gitignore).
2. En tu equipo, añade el remoto usando **tu nombre de usuario**:

```bash
git remote add origin https://github.com/TU_USUARIO/reflexion-libertad-conciencia.git
git push -u origin main
```

## 3. Desplegar con Netlify

1. Accede a https://app.netlify.com/ e inicia sesión.
2. Selecciona **Add new project** / **Import an existing project** (la denominación puede variar).
3. Selecciona **GitHub**, autoriza el acceso, y elige `reflexion-libertad-conciencia`.
4. Configura:
   - Branch to deploy: `main`.
   - Build command: **dejar vacío** (no hay compilación).
   - Publish directory: `.` (raíz del repositorio; ya aparece en `netlify.toml`).
5. Selecciona **Deploy**.
6. En el sitio desplegado, abre la URL terminada en `.netlify.app` y comprueba que funciona.
7. Opcionalmente, entra en **Domain management** y configura el subdominio del sitio o un dominio propio.

## 4. Actualizar el texto y volver a desplegar

Para editar pequeños detalles de presentación, modifica `index.html` y `assets/style.css`.

**Importante:** `index.html` también se puede generar mediante `build_page.py`. Si ejecutas ese script, reemplazará el HTML actual. Para cambiar el contenido largo de forma reproducible, edita el array `sections` dentro de `build_page.py` y ejecuta:

```bash
python3 build_page.py
git add .
git commit -m "Actualizar reflexión"
git push
```

Con el repositorio conectado, Netlify suele realizar un despliegue automático con cada `push` a `main`.

## Validaciones recomendadas

- Abrir en móvil y escritorio; comprobar índice y modo oscuro.
- Pulsar **Leer el artículo original** y comprobar que abre el enlace esperado.
- Confirmar que el sitio usa `https://`.
- Probar los enlaces externos, que se abren en pestaña nueva.
- Validar el HTML con el validador W3C si se hacen modificaciones complejas.

## Notas

- Sin frameworks, cookies ni servicios de terceros necesarios para funcionar.
- El contenido del artículo de *La Razón* **no se reproduce**: se enlaza al original.
- No se ha incluido `sitemap.xml` ni URL canónica porque el dominio final depende del despliegue.
- Para una imagen de previsualización en LinkedIn/WhatsApp, se puede añadir más adelante `og:image` con su URL pública absoluta.


## Versión editorial ilustrada

La portada incluye una imagen original generada para este ensayo (`assets/biblioteca-libertad.webp`), además de una versión adaptada a redes (`assets/portada-social.webp`). Se incluye una reflexión sobre la causa palestina, distinguiendo la solidaridad humanitaria de sus posibles usos políticos, en el capítulo «Las ideologías cambian...».

**Edición**: El texto de referencia está en `build_page.py`; ejecuta `python3 build_page.py` para regenerar `index.html`. El despliegue de Netlify sigue siendo estático (`publish = "."`).
