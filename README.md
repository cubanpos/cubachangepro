# CubaChange Pro — guía, manual y vídeos

Página pública del sistema: **https://cubanpos.github.io/cubachangepro/**

Sistema para casas de cambio privadas en Cuba. El mostrador, la caja, las tasas
y el cierre del día, en la red del propio negocio y sin internet.

## Qué hay aquí

| Archivo | Qué es |
| --- | --- |
| `index.html` | La página. Es la guía visual con tres láminas de más: navegación, vídeos y descargas. |
| `descargas/Manual.de.Usuario.CubaChangePro.pdf` | El manual completo, 27 secciones. |
| `descargas/Guia.visual.CubaChangePro.html` | La guía visual en un solo archivo, para abrir sin conexión. |
| `descargas/CubaChangePro.-.recorrido.apaisado.mp4` | El recorrido en 16:9, con voz y música (5 min 50 s). |
| `descargas/CubaChangePro.-.recorrido.vertical.mp4` | El mismo recorrido en 9:16, para el móvil. |
| `armar-pagina.py` | Deriva `index.html` de la guía. |

**Aquí no hay instaladores ni código del programa**, a propósito: este repositorio
es público y sirve para enseñar el sistema, no para repartirlo. El paquete del
cliente se entrega aparte.

## Cómo se actualiza

La página **no se edita a mano**. Se deriva de la guía visual:

```bash
python armar-pagina.py
```

Si la guía cambia, se copia la nueva a `descargas/Guia.visual.CubaChangePro.html`,
se vuelve a correr eso y se sube. Editar `index.html` directamente hace que la
web y el documento que recibe el cliente empiecen a decir cosas distintas, y eso
no se nota hasta que alguien compara los dos.

El manual sale del propio programa (Ayuda → *Descargar en PDF*): no es un
documento aparte que haya que mantener al día.

## Contacto

WhatsApp **+53 5814 6895** (Yunior Reyes) · **axissoftstgo@gmail.com** ·
Santiago de Cuba
