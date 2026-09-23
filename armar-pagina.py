# -*- coding: utf-8 -*-
u"""
===========================================================================
ARMA LA PAGINA WEB A PARTIR DE LA GUIA VISUAL
---------------------------------------------------------------------------
La pagina NO se escribe a mano. Se deriva de `descargas/Guia.visual.CubaChangePro.html`,
que es el documento que tambien se entrega al cliente, y se le anaden tres
cosas que solo tienen sentido en la web:

  1. una barra de navegacion,
  2. los dos videos del recorrido, que en el archivo suelto no caben,
  3. una lamina de descargas.

Se hace asi por una razon concreta: si la pagina fuera una copia, a la segunda
correccion la guia y la web dirian cosas distintas, y nadie se enteraria hasta
que un cliente comparase las dos. Derivandola, una correccion en la guia llega
sola a la web con volver a correr esto.

    python armar-pagina.py
===========================================================================
"""
import io, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTE = os.path.join(AQUI, u"descargas", u"Guia.visual.CubaChangePro.html")
SALIDA = os.path.join(AQUI, u"index.html")
BASE = u"https://cubanpos.github.io/cubachangepro/"

g = io.open(FUENTE, encoding=u"utf8").read()

# ---------------------------------------------------------------- cabecera
# El titulo de la guia suelta es el nombre del documento; el de la pagina es
# el nombre del producto, que es lo que se ve en la pestana y en Google.
g = g.replace(u"<title>Pizarra Abierta</title>", u"<title>CubaChange Pro</title>", 1)

META = u"""
<link rel="canonical" href="%(base)s">
<meta property="og:type" content="website">
<meta property="og:title" content="CubaChange Pro">
<meta property="og:site_name" content="CUBANPOS">
<meta property="og:locale" content="es_CU">
<meta property="og:url" content="%(base)s">
<meta property="og:description" content="El mostrador, la caja, las tasas y el cierre de una casa de cambio privada. En tu propia red, sin internet.">
""" % {u"base": BASE}

# ---- lo unico que se anade al estilo ----------------------------------
# Todo con los tokens que ya existen; ni un color nuevo. Un tono mas en la
# paleta por tres bloques seria empezar a tener dos verdes que significan lo
# mismo.
ESTILO = u"""
<style>
/* ---- la navegacion de la barra (solo existe en la web) ---- */
.barra .nav{display:none; gap:22px; align-items:center}
.barra .nav a{color:var(--suave); text-decoration:none; font-family:var(--display);
  font-size:14px; font-weight:600; letter-spacing:.01em; padding:6px 0;
  border-bottom:2px solid transparent}
.barra .nav a:hover, .barra .nav a:focus-visible{color:var(--tinta); border-bottom-color:var(--oro)}
@media (min-width:760px){ .barra .nav{display:flex} }

/* ---- los dos videos ---- */
.cintas{display:grid; gap:28px; grid-template-columns:1fr}
@media (min-width:900px){ .cintas{grid-template-columns:1.62fr 1fr; align-items:start} }
/* El vertical mide 9:16. A la misma anchura que el apaisado saldria el doble de
   alto y se comeria la lamina entera, asi que se le pone techo y se centra: lo
   que manda es que los dos se vean a la vez, no que ocupen lo mismo. */
.cinta.movil video{max-width:min(100%, 280px); margin:0 auto}
.cinta.movil .rot, .cinta.movil .pie{text-align:center}
.cinta{display:grid; gap:12px; min-width:0}
.cinta video{display:block; width:100%; height:auto; border-radius:14px;
  border:1px solid rgba(255,255,255,.14); background:#000}
.cinta .rot{font-family:var(--dato); font-size:11.5px; font-weight:600;
  letter-spacing:.16em; text-transform:uppercase; color:#8AA1A9}
.cinta .pie{font-family:var(--cuerpo); font-size:15px; line-height:1.5; color:#A9BEC4; margin:0}

/* ---- la lamina de descargas ---- */
.bajadas{display:grid; gap:14px; grid-template-columns:1fr; margin-top:8px}
@media (min-width:720px){ .bajadas{grid-template-columns:1fr 1fr} }
.baja{display:flex; align-items:center; gap:16px; padding:18px 20px; min-width:0;
  background:var(--panel); border:1px solid var(--linea); border-radius:14px;
  text-decoration:none; color:inherit; box-shadow:var(--sombra)}
.baja:hover, .baja:focus-visible{border-color:var(--oro)}
.baja .ico{flex:0 0 auto; width:44px; height:44px; border-radius:11px;
  background:var(--realce); display:flex; align-items:center; justify-content:center}
.baja .txt{display:grid; gap:3px; min-width:0}
.baja .q{font-family:var(--display); font-size:16.5px; font-weight:700; letter-spacing:-.01em}
.baja .d{font-family:var(--dato); font-size:12px; color:var(--suave); letter-spacing:.04em}
</style>
"""
g = g.replace(u"</head>", META + ESTILO + u"</head>", 1)

# ---- la barra: el hueco de la guia pasa a ser la navegacion -----------
VIEJA = u'<span class="hueco"></span>\n    <span class="sec">Casa de cambio · Cuba</span>'
NUEVA = (u'<nav class="nav" aria-label="Secciones">\n'
         u'      <a href="#recorrido">El recorrido</a>\n'
         u'      <a href="#videos">Vídeos</a>\n'
         u'      <a href="#descargas">Descargas</a>\n'
         u'    </nav>\n'
         u'    <span class="hueco"></span>')
if VIEJA not in g:
    sys.exit(u"la barra de la guia cambio de forma: revisar el reemplazo")
g = g.replace(VIEJA, NUEVA, 1)

# ---------------------------------------------------------------- videos
VIDEOS = u"""
<!-- ========================== LOS DOS VIDEOS ============================ -->
<section class="banda" id="videos">
  <div class="env">
    <div class="cabecera">
      <span class="rotulo" style="color:#8AA1A9">El recorrido en vídeo</span>
      <h2>Seis minutos, y ya sabes si te sirve</h2>
      <p>El mismo recorrido de esta página, contado en voz alta y pantalla por pantalla:
        la pizarra, el mostrador, las tarjetas, el turno de caja, las denominaciones,
        el cierre, los informes y los controles de cada operación.</p>
    </div>
    <div class="cintas">
      <figure class="cinta">
        <div class="rot">Para el ordenador · 16:9</div>
        <video controls preload="metadata" playsinline
          poster="img/portada-apaisado.webp"
          src="descargas/CubaChangePro.-.recorrido.apaisado.mp4"></video>
        <p class="pie">5 min 50 s · 85 MB. Para verlo en pantalla grande o mandarlo por correo.</p>
      </figure>
      <figure class="cinta movil">
        <div class="rot">Para el teléfono · 9:16</div>
        <video controls preload="metadata" playsinline
          poster="img/portada-vertical.webp"
          src="descargas/CubaChangePro.-.recorrido.vertical.mp4"></video>
        <p class="pie">5 min 50 s · 74 MB. El mismo recorrido, montado para el móvil.</p>
      </figure>
    </div>
  </div>
</section>
"""

# ------------------------------------------------------------- descargas
def icono(d):
    return (u'<span class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
            u'stroke="var(--oro)" stroke-width="1.8" stroke-linecap="round" '
            u'stroke-linejoin="round" aria-hidden="true">%s</svg></span>' % d)

DOC = u'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'
PANTALLA = u'<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 20.5h8M12 17v3.5"/>'
PELICULA = u'<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M10 9.5l5 2.5-5 2.5z"/>'
TELEFONO = u'<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 5.5h3"/>'

PIEZAS = [
    (DOC, u"Manual de usuario", u"PDF · 27 secciones · 145 KB",
     u"descargas/Manual.de.Usuario.CubaChangePro.pdf"),
    (PANTALLA, u"Guía visual completa", u"HTML · un solo archivo · 1,9 MB",
     u"descargas/Guia.visual.CubaChangePro.html"),
    (PELICULA, u"Vídeo del recorrido", u"MP4 · 16:9 · 85 MB",
     u"descargas/CubaChangePro.-.recorrido.apaisado.mp4"),
    (TELEFONO, u"Vídeo para el móvil", u"MP4 · 9:16 · 74 MB",
     u"descargas/CubaChangePro.-.recorrido.vertical.mp4"),
]

DESCARGAS = u"""
<!-- ========================== DESCARGAS ================================= -->
<section id="descargas">
  <div class="env">
    <div class="cabecera">
      <span class="rotulo">Para llevarte</span>
      <h2>Llévatelo todo y míralo sin conexión</h2>
      <p>El manual y la guía se abren en cualquier ordenador o teléfono, sin instalar nada
        y sin internet. Los vídeos se pueden reenviar por WhatsApp tal cual.</p>
    </div>
    <div class="bajadas">
%(filas)s
    </div>
  </div>
</section>
""" % {u"filas": u"\n".join(
    u'      <a class="baja" href="%s" download>%s<span class="txt">'
    u'<span class="q">%s</span><span class="d">%s</span></span></a>' % (h, icono(d), q, s)
    for (d, q, s, h) in PIEZAS)}

# El cierre con los contactos es lo ultimo del documento; los dos bloques
# nuevos van justo antes, para que la llamada a la accion siga cerrando.
ANCLA = u"<!-- ========================== CIERRE"
if ANCLA not in g:
    sys.exit(u"no se encuentra el bloque de CIERRE de la guia")
g = g.replace(ANCLA, VIDEOS + DESCARGAS + u"\n" + ANCLA, 1)

io.open(SALIDA, u"w", encoding=u"utf8", newline=u"\n").write(g)
print(u"  index.html  (%.1f KB)" % (len(g.encode(u"utf8")) / 1024.0))
