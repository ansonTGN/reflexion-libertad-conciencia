# Cuando las ideologías piensan por nosotros · edición en 5 idiomas

Web editorial estática de Ángel A. Urbina Sánchez. Incluye el ensayo en **español, catalán, inglés, portugués europeo y francés**; fotografía de portada, modo claro/oscuro, índice navegable, indicador de lectura y enlaces al artículo de origen en *La Razón*.

## Estructura

```text
index.html                 Español (URL /)
ca/index.html              Català  (URL /ca/)
en/index.html              English (URL /en/)
pt/index.html              Português (URL /pt/)
fr/index.html              Français (URL /fr/)
assets/style.css           Estilo común, responsive
assets/site.js             Selector de idioma, tema, lectura y compartir
assets/biblioteca-libertad.webp   Fotografía de portada
assets/portada-social.webp       Vista previa de redes
assets/favicon.svg
source/index.es.html       Fuente editorial original en español
translations.py            Textos editoriales en los 4 idiomas adicionales
build_multilingual.py      Generador de las cinco páginas
build_page.py              Alias de compatibilidad
netlify.toml               Sitio HTML estático; publish = "."
```

## Vista previa en Ubuntu

```bash
cd ~/Descargas/reflexion-libertad-web
python3 -m http.server 8000
```

Navega a `http://localhost:8000/` y cambia el idioma en la cabecera. Para comprobar una página directamente, usa `http://localhost:8000/ca/`, `/en/`, `/pt/` o `/fr/`.

## Publicar en el repositorio existente

El repositorio es `https://github.com/ansonTGN/reflexion-libertad-conciencia`. Si la carpeta de `~/Descargas/reflexion-libertad-web` ya contiene `.git` y apunta a ese repositorio (compruébalo con `git remote -v`), **no la clones de nuevo**.

Descomprime el ZIP sobre dicha carpeta con `unzip -o` (o copia los archivos del ZIP a tu clon local), y ejecuta:

```bash
cd ~/Descargas/reflexion-libertad-web
git status
git add -A
git commit -m "Publicar edición multilingüe ES CA EN PT FR"
git push origin main
```

Si hay modificaciones concurrentes en el remoto, comprueba primero `git fetch origin` y no fuerces la subida.

## Netlify

Con el repositorio GitHub ya vinculado a Netlify, `git push origin main` activa el despliegue. Si todavía no está vinculado, selecciona **Add new project → Import an existing project → GitHub**, elige `ansonTGN/reflexion-libertad-conciencia` y configura:

- **Production branch:** `main`
- **Build command:** vacío
- **Publish directory:** `.`

Netlify sirve automáticamente `index.html` en las subcarpetas al navegar a `/ca/`, `/en/`, `/pt/` y `/fr/`.

## Cambiar traducciones

Edita `translations.py` o el original español en `source/index.es.html`; después, en un entorno con `beautifulsoup4`, regenera:

```bash
python3 -m pip install beautifulsoup4
python3 build_multilingual.py
```

Los HTML finales **ya están incluidos**: no necesitas Python, pip ni dependencias durante el despliegue en Netlify.

## Detalles técnicos

- Navegación por idioma mediante páginas estáticas. El cambio conserva el ancla de la sección actual (por ejemplo `#libertad`).
- Cada página tiene `lang`, título, descripción, `og:locale` y enlaces entre versiones lingüísticas.
- El modo oscuro queda guardado en `localStorage` y se mantiene al cambiar de idioma.
- Las traducciones son **adaptaciones editoriales fieles al argumento**, no una traducción literal párrafo por párrafo. Recomendable revisión de estilo por una persona nativa antes de la difusión institucional.
- Se mantiene el artículo de referencia como enlace externo; la web no reproduce el contenido protegido de dicho artículo.
- Para SEO avanzado, cuando conozcas el dominio definitivo, configura URLs canónicas absolutas y etiquetas `hreflang` con URL absoluta (ahora las alternancias son relativas).
- La portada de redes utiliza `/assets/portada-social.webp`; algunas plataformas necesitan una URL absoluta para obtener la vista previa: actualízala cuando se conozca el dominio real.

© 2026 Ángel A. Urbina Sánchez.
