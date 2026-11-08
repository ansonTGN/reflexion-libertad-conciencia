from pathlib import Path
from html import escape
import re
root=Path(__file__).parent
article='https://www.larazon.es/cultura/woke-20-virus-muta-sobrevivir_202611086aefb48fea8d8979977d2cd4.html'
sections=[
('introduccion','Una reflexión sobre el poder, la identidad y la libertad de conciencia', '''Vivimos en una época que presume de haber alcanzado una libertad intelectual sin precedentes. Nunca habíamos tenido tanto acceso al conocimiento, tantas posibilidades de contrastar opiniones ni tantos instrumentos para cuestionar las estructuras tradicionales del poder.

Y, sin embargo, resulta paradójico observar hasta qué punto seguimos necesitando que alguien nos explique qué debemos pensar, qué causas debemos defender y quiénes son nuestros adversarios.

La lectura del artículo «Woke 2.0: El virus muta para sobrevivir», publicado en La Razón, me ha llevado a reflexionar sobre una cuestión que considero mucho más profunda que la controversia en torno a un movimiento ideológico concreto.

**¿Somos realmente libres cuando pensamos o simplemente hemos aprendido a considerar propias las ideas que otros han construido para nosotros?**

No se trata de cuestionar la legitimidad de las reivindicaciones sociales ni de negar que existan desigualdades que debamos corregir. Tampoco de descalificar las convicciones políticas de quienes piensan de manera diferente.

Se trata de comprender cómo las ideas, incluso aquellas que nacen de aspiraciones legítimas, pueden transformarse en estructuras de poder que terminan condicionando nuestra percepción de la realidad.'''),
('poder','El poder más profundo no necesita imponerse', '''Habitualmente asociamos el poder con gobiernos, instituciones, grandes empresas o recursos económicos.

Pero existe una forma de poder mucho más sutil: la capacidad de determinar cómo interpretamos el mundo.

Quien consigue establecer qué es moralmente aceptable, qué constituye una amenaza o qué opiniones merecen reconocimiento dispone de una extraordinaria capacidad de influencia.

Michel Foucault estudió cómo el poder y la producción de conocimiento se relacionan. Antonio Gramsci analizó los mecanismos mediante los cuales determinadas concepciones del mundo alcanzan una posición hegemónica y terminan pareciendo naturales.

Ambas perspectivas nos ayudan a comprender algo importante: el poder no siempre necesita prohibir.

En ocasiones le basta con conseguir que determinadas preguntas dejen de formularse.

Cuando interiorizamos completamente un marco ideológico, podemos comenzar a vigilar espontáneamente nuestras propias opiniones.

No necesariamente porque alguien nos obligue, sino porque cuestionar las creencias dominantes dentro de nuestro entorno puede significar perder reconocimiento, pertenencia o legitimidad moral.

Esta dinámica no pertenece exclusivamente a una corriente política.

Puede manifestarse en organizaciones religiosas, empresas, universidades, movimientos sociales y comunidades digitales.

Incluso quienes se presentan como adversarios del pensamiento dominante pueden terminar construyendo sus propias ortodoxias.

**El pensamiento único no se define por el contenido de las ideas, sino por la dificultad de cuestionarlas sin sufrir consecuencias.**

Y aquí aparece una paradoja inquietante: una sociedad puede multiplicar sus discursos sobre la libertad mientras reduce los espacios donde resulta posible disentir.'''),
('identidad','Necesitamos un «ellos» para construir un «nosotros»', '''Los seres humanos necesitamos pertenecer.

La familia, la comunidad, la nación, la religión o una causa compartida pueden proporcionarnos identidad y sentido.

No hay nada necesariamente negativo en ello. La pertenencia constituye una dimensión esencial de nuestra naturaleza social.

El problema comienza cuando nuestra identidad necesita permanentemente la existencia de un adversario.

En ese momento, quien piensa de manera diferente deja de ser una persona con argumentos que podemos discutir y se convierte en alguien cuya legitimidad moral ponemos en cuestión.

Ya no debatimos ideas.

Clasificamos personas.

La complejidad humana queda reducida a categorías aparentemente sencillas: progresistas y conservadores, conscientes e ignorantes, víctimas y culpables, buenos y malos.

Pero la realidad rara vez se deja encerrar en esas divisiones.

Una persona puede defender una causa justa y equivocarse profundamente en sus métodos.

Otra puede cuestionar determinados movimientos sociales sin rechazar los derechos que estos reivindican.

Confundir ambas dimensiones empobrece nuestra capacidad de comprender.

Y, sobre todo, convierte el debate público en una competición por demostrar superioridad moral.

**Cuando necesitamos deshumanizar al adversario para justificar nuestras convicciones, probablemente hemos comenzado a perder nuestra propia libertad intelectual.**'''),
('ideologias','Las ideologías cambian, pero ¿cambia nuestra relación con el poder?', '''El artículo plantea que determinados movimientos están modificando sus discursos para adaptarse a nuevas circunstancias sociales y políticas.

Esa interpretación merece ser examinada sin convertirla automáticamente en una verdad incuestionable.

Las ideologías evolucionan por razones diferentes.

En ocasiones cambian porque reconocen errores. Otras veces porque la sociedad descubre nuevas necesidades. Y también pueden modificar su lenguaje porque determinadas estrategias han dejado de resultar eficaces.

Estos procesos no son necesariamente excluyentes.

Por eso me parece insuficiente juzgar una transformación ideológica únicamente por sus nuevas consignas.

La pregunta importante es qué ocurre detrás de las palabras.

¿Se amplían realmente las libertades?

¿Se reducen desigualdades?

¿Se permite la discrepancia?

¿Se reconocen los errores?

¿Se aplican los mismos principios independientemente de quién resulte beneficiado?

Estas cuestiones permiten evaluar cualquier movimiento con criterios más sólidos que su identidad política.

Porque una ideología puede cambiar completamente su vocabulario sin modificar su relación con el poder.

Y también puede conservar sus principios fundamentales mientras aprende a corregir sus contradicciones.

**La verdadera transformación no consiste en sustituir unas consignas por otras, sino en modificar nuestra relación con la verdad, la libertad y los demás.**'''),
('indignacion','La industria de la indignación', '''Existe otra dimensión que considero especialmente relevante.

Las ideologías contemporáneas ya no compiten únicamente por el control de las instituciones.

Compiten por nuestra atención.

Y la atención se ha convertido en uno de los recursos económicos más valiosos de nuestro tiempo.

Las plataformas digitales han multiplicado nuestras posibilidades de acceder al conocimiento, pero también han creado entornos donde la indignación, el miedo y la confrontación pueden generar una enorme visibilidad.

Un mensaje que despierta emociones intensas puede circular más rápidamente que una explicación rigurosa y matizada.

Esto no significa que toda denuncia sea exagerada ni que cualquier protesta responda a una manipulación.

Significa que debemos distinguir entre la importancia real de un acontecimiento y la intensidad emocional con la que se nos presenta.

Podemos dedicar horas a discutir conflictos lejanos mientras apenas prestamos atención a los problemas de nuestro entorno.

Podemos experimentar una profunda sensación de compromiso moral sin realizar ninguna acción que transforme la realidad.

Incluso podemos llegar a confundir nuestra actividad digital con nuestra capacidad de contribuir al bienestar colectivo.

Por eso creo que hoy necesitamos formularnos una pregunta adicional cada vez que recibimos una información que despierta una reacción intensa:

**¿Por qué esta cuestión está reclamando mi atención precisamente ahora y quién se beneficia de la manera en que se me presenta?**

No se trata de sospechar de todo.

Se trata de conservar nuestra capacidad de decidir qué merece nuestro tiempo, nuestra energía y nuestra implicación emocional.'''),
('obediencia','La paradoja de defender la libertad exigiendo obediencia', '''Una de las contradicciones más profundas de los movimientos ideológicos aparece cuando sus fines declarados entran en conflicto con sus métodos.

Podemos defender la diversidad y mostrarnos intolerantes con determinadas opiniones.

Podemos reivindicar la libertad individual mientras pretendemos imponer una única concepción de la vida.

Podemos denunciar la exclusión y terminar construyendo nuevas formas de exclusión.

Y podemos defender la libertad de expresión mientras desacreditamos sistemáticamente a quienes reivindican derechos sociales.

Ninguna tradición política está completamente libre de estas contradicciones.

Por eso considero que la coherencia ética debe medirse precisamente cuando nuestros principios nos obligan a reconocer derechos a quienes no comparten nuestras convicciones.

Defender la libertad de quien piensa como nosotros resulta relativamente sencillo.

La verdadera prueba aparece cuando debemos reconocer esa misma libertad a quien cuestiona nuestras ideas.

No significa que todas las opiniones sean igualmente verdaderas ni que cualquier comportamiento deba resultar aceptable.

Significa que necesitamos distinguir entre el derecho de una persona a expresar sus ideas y la validez de los argumentos que utiliza.

**Una ética que únicamente protege a los nuestros corre el riesgo de convertirse en una estrategia de pertenencia disfrazada de principio universal.**'''),
('pensamiento','El pensamiento crítico comienza cuando cuestionamos nuestras propias certezas', '''Hay algo que me parece particularmente importante.

Resulta mucho más sencillo identificar los prejuicios de los demás que reconocer los nuestros.

Todos construimos modelos mentales para interpretar la realidad.

Todos seleccionamos información.

Todos tenemos experiencias que condicionan nuestra percepción.

Y todos podemos caer en la tentación de considerar que nuestras conclusiones son el resultado de un razonamiento independiente, mientras atribuimos las opiniones contrarias a la manipulación ideológica.

Esta asimetría es profundamente humana.

Por eso el pensamiento crítico no puede limitarse a desmontar los relatos de nuestros adversarios.

Debe dirigirse también hacia aquellas ideas que nos proporcionan seguridad, reconocimiento y satisfacción moral.

Hay algo intelectualmente liberador en reconocer que una persona con posiciones diferentes puede haber identificado una verdad que nosotros no habíamos sabido ver.

Escuchar no significa aceptar.

Comprender no implica justificar.

Y cambiar de opinión no debería interpretarse como una derrota.

Al contrario.

**La capacidad de modificar nuestras convicciones ante argumentos y evidencias mejores constituye una de las expresiones más elevadas de nuestra autonomía intelectual.**

Quizá una de las formas más profundas de madurez consista precisamente en aprender a convivir con la incertidumbre.

En aceptar que podemos estar equivocados.

En reconocer que la complejidad del mundo supera cualquier sistema ideológico que pretenda explicarlo completamente.'''),
('etica','Comprender el poder sin convertirnos en aquello que criticamos', '''Existe una cuestión que me preocupa especialmente.

Cuando aprendemos a reconocer los mecanismos de manipulación, adquirimos una capacidad que también podemos utilizar para manipular.

Podemos identificar cómo se construyen los relatos, cómo se movilizan las emociones y cómo determinadas estructuras condicionan el comportamiento colectivo.

Pero ese conocimiento nos sitúa ante una responsabilidad ética.

¿Qué hacemos con él?

Podemos utilizarlo para influir sobre otras personas de manera cada vez más eficaz.

O podemos emplearlo para proteger nuestra autonomía y contribuir a construir relaciones más libres.

Esta distinción me parece fundamental.

Comprender los mecanismos de dominación no debería conducirnos a reproducirlos.

Tampoco deberíamos confundir la lucidez con el cinismo.

Que una causa social pueda ser instrumentalizada políticamente no significa que el sufrimiento que denuncia sea inexistente.

Que una organización obtenga reconocimiento defendiendo determinados valores no demuestra que esos valores carezcan de legitimidad.

Y que una ideología cumpla funciones de poder no implica que todas sus afirmaciones sean falsas.

La sospecha permanente también puede convertirse en una prisión intelectual.

Una persona que interpreta cualquier gesto de solidaridad como una estrategia oculta termina perdiendo la capacidad de reconocer la bondad cuando aparece.

**La verdadera lucidez no consiste en descubrir intereses ocultos detrás de cada acción, sino en aprender a distinguir cuándo esos intereses explican realmente lo que estamos observando.**'''),
('libertad','La libertad de no pertenecer intelectualmente a nadie', '''Con los años he llegado a valorar cada vez más una idea: la importancia de conservar la curiosidad y la capacidad de revisar nuestras propias certezas.

La experiencia no nos hace automáticamente más sabios.

Podemos acumular conocimientos y continuar interpretando el mundo mediante los mismos prejuicios.

Podemos conocer muchas teorías y seguir siendo incapaces de escuchar a quien piensa de manera diferente.

Y podemos defender apasionadamente nuestra libertad mientras entregamos nuestra capacidad de juicio a una organización, un movimiento o una ideología.

Quizá por eso considero que aprender no consiste únicamente en incorporar nuevos conocimientos.

También significa estar dispuestos a desprendernos de interpretaciones que han dejado de ayudarnos a comprender la realidad.

La lectura del artículo sobre el denominado Woke 2.0 me ha llevado a reflexionar sobre estos mecanismos.

Pero sería un error limitar esta reflexión al movimiento que critica.

La propia expresión que presenta una ideología como un virus constituye una forma de construir un relato: transforma un fenómeno político y cultural complejo en una amenaza frente a la cual debemos posicionarnos.

Eso no invalida automáticamente los argumentos del autor.

Simplemente nos recuerda que debemos aplicar a cualquier discurso el mismo rigor crítico que exigimos a aquellos que cuestionamos.

Y ahí reside, para mí, la cuestión esencial.

**No somos intelectualmente libres porque hayamos identificado los mecanismos de manipulación de quienes piensan de manera diferente. Somos libres cuando aprendemos a reconocer esos mismos mecanismos en las ideas que nosotros defendemos.**

Tal vez el gran desafío de nuestro tiempo no consista en sustituir unas ideologías por otras.

Tal vez consista en aprender a convivir con nuestras convicciones sin convertirlas en cárceles.

En defender valores sin renunciar a la posibilidad de revisarlos.

En participar en proyectos colectivos sin entregar nuestra conciencia.

En comprender las estructuras del poder sin perder nuestra humanidad.

Y, sobre todo, en conservar algo que ninguna organización, movimiento político o estructura social debería arrebatarnos:

**La capacidad de pensar por nosotros mismos, incluso cuando hacerlo significa cuestionar aquello en lo que siempre hemos creído.**

Porque la libertad más profunda no consiste simplemente en que nadie nos diga lo que debemos pensar.

**Consiste en que, aunque todos intenten hacerlo, conservemos la capacidad de preguntarnos si tienen razón.**''')]
def inline(s):
    s=escape(s)
    return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',s)
def paras(t):
    parts=t.strip().split('\n\n')
    result=[]
    for p in parts:
        if p.startswith('**') and p.endswith('**') and p.count('**') == 2:
            result.append('<blockquote><p>'+inline(p[2:-2])+'</p></blockquote>')
        else: result.append('<p>'+inline(p)+'</p>')
    return '\n'.join(result)
toc='\n'.join(f'<a href="#{sid}">{escape(title)}</a>' for sid,title,_ in sections[1:])
content='\n'.join(f'<section id="{sid}" aria-labelledby="heading-{sid}">'+(f'<h2 id="heading-{sid}">{escape(title)}</h2>' if sid!='introduccion' else '')+paras(body)+'</section>' for sid,title,body in sections)
# Add direct link within the body at both references to source article
content=content.replace('«Woke 2.0: El virus muta para sobrevivir», publicado en La Razón', f'<a href="{article}" target="_blank" rel="noopener noreferrer">«Woke 2.0: El virus muta para sobrevivir»</a>, publicado en <em>La Razón</em>',1)
content=content.replace('La lectura del artículo sobre el denominado Woke 2.0', f'La lectura del <a href="{article}" target="_blank" rel="noopener noreferrer">artículo sobre el denominado Woke 2.0</a>',1)
source=f'''<aside class="source-box" aria-label="Artículo que inspira esta reflexión"><span class="label">Lectura de origen · La Razón</span><p>Esta reflexión nace de la lectura de «Woke 2.0: El virus muta para sobrevivir», publicado el 8 de noviembre de 2026.</p><a href="{article}" target="_blank" rel="noopener noreferrer">Leer el artículo original ↗</a><p style="font-size:.77rem;color:var(--muted);margin:.7rem 0 0">El artículo pertenece a su medio y puede estar sujeto a sus condiciones de acceso.</p></aside>'''
content=content.replace('</section>',source+'</section>',1)
html=f'''<!doctype html>
<html lang="es" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#102b3d">
  <meta name="description" content="Una reflexión filosófica de Ángel A. Urbina Sánchez sobre la ideología, el poder, la identidad y la libertad de conciencia.">
  <meta name="author" content="Ángel A. Urbina Sánchez">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="es_ES">
  <meta property="og:title" content="Cuando las ideologías piensan por nosotros">
  <meta property="og:description" content="Sobre el poder, la identidad, la indignación y la libertad de pensamiento. Una reflexión de Ángel A. Urbina Sánchez.">
  <meta property="article:published_time" content="2026-11-08">
  <meta name="twitter:card" content="summary">
  <title>Cuando las ideologías piensan por nosotros · Ángel A. Urbina Sánchez</title>
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/style.css">
  <script defer src="assets/site.js"></script>
</head>
<body>
  <a href="#contenido" class="skip-link">Saltar al contenido</a>
  <div id="reading-progress" class="progress" aria-hidden="true"></div>
  <header class="topbar" id="arriba">
    <a class="brand" href="#arriba">Ángel A. Urbina Sánchez <span aria-hidden="true">/</span> Ensayos</a>
    <div class="toolbar">
      <button id="copy-link" type="button" aria-label="Compartir el artículo">↗ Compartir</button>
      <button id="theme-toggle" type="button" aria-pressed="false">☾ Tema oscuro</button>
    </div>
  </header>
  <div class="hero"><div class="hero-inner">
    <div class="eyebrow">Pensamiento · Sociedad · Filosofía</div>
    <h1>Cuando las ideologías<br>piensan por nosotros</h1>
    <p class="lead">Una reflexión sobre el poder, la identidad y la libertad de conciencia.</p>
    <div class="meta"><span>Ángel A. Urbina Sánchez</span><span>8 de noviembre de 2026</span><span>Ensayo</span></div>
  </div></div>
  <main id="contenido" class="main-grid">
    <aside class="toc" aria-label="Índice de contenidos"><strong>En este ensayo</strong><nav>{toc}</nav></aside>
    <article class="article" aria-label="Ensayo completo">
      {content}
      <div class="signature">Reflexión a propósito del <a href="{article}" target="_blank" rel="noopener noreferrer">artículo «Woke 2.0: El virus muta para sobrevivir»</a>, publicado en <em>La Razón</em> el 8 de noviembre de 2026.<strong>Ángel A. Urbina Sánchez</strong><a class="back-to-top" href="#arriba">↑ Volver al inicio</a></div>
    </article>
  </main>
  <footer class="footer">© 2026 Ángel A. Urbina Sánchez · Reflexión y pensamiento crítico · <a href="{article}" target="_blank" rel="noopener noreferrer">Artículo de referencia ↗</a></footer>
</body></html>'''
(root/'index.html').write_text(html,encoding='utf8')
print('Generated sections',len(sections),'word count',len(re.sub('<[^>]+>',' ',html).split()))
