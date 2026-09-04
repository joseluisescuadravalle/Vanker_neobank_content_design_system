# Contexto para continuar en un chat nuevo (01/09/2026)

Pega esto al abrir la sesión nueva. Es el estado real, no un resumen optimista.

## Qué es el proyecto

Sistema de diseño de contenido de **Vanker**, un neobanco ficticio de la zona euro, escrito
para que lo usen a la vez personas y un agente de IA. Material docente para los cursos de
Maven de José Luis (IA Accelerator, Evals).

Dos repos, los dos locales en el Mac y en GitHub:

- `~/Desktop/Content_Design_System_AI` → `joseluisescuadravalle/Vanker_neobank_content_design_system`.
  El sistema. **Fuente de verdad.**
- `~/Desktop/Vanker_content_desktop_app` → `joseluisescuadravalle/Vanker-desktop-app`.
  La web y el comprobador de copy (Vite + React + TypeScript). **Cliente del sistema.**
  Se levanta con `npm run dev`, en `localhost:5174`. La home y el checker son un solo sitio.

## Cómo trabajamos (importante)

- Cowork edita los ficheros directamente por el puente al Mac. **José Luis hace
  `git add/commit/push` desde Terminal.** Hay que darle el bloque bash de CADA cosa,
  empezando siempre por `rm -f .git/index.lock` (el mount deja locks).
- Hay DOS sesiones trabajando: esta (el sistema) y una de Claude Code (la app). Regla
  acordada: **un dueño por repo**, y lo que cruza la frontera se escribe en el handoff.
  Ya hubo un choque: Code portó `A-COLOR-ALONE` a la app mientras yo lo hacía aquí.
- Acompañamiento didáctico antes que entregables. Explicar decisiones.
- Cuando él pide copy, **enseñársela para validar antes** de fijarla en casos golden.

## Preferencias suyas (literales)

- Respuestas completas al primer intento, sin postámbulos ni ofrecimientos de mejoras.
  Estilo amable, conciso y senior.
- Si su idea tiene un fallo: primera frase con la estructura
  "No estoy de acuerdo porque [razón]. Alternativa: [X]. Riesgo de tu planteamiento: [Y]."
- Etiquetar afirmaciones: [Cierto] / [Probable] / [Suposición].
- **Nunca usar raya larga (—)** en chat ni en documentos; paréntesis en su lugar.
- Expandir acrónimos entre paréntesis. Encabezar sesión con "Etapa X — Sección".
- Dar el texto terminado, nunca referencias a fragmentos anteriores.
- Ojo con la jerga: pide simplificar cuando se acumula (le pasó con "slots / JSON spec /
  eval hooks / generator").

## Estado del sistema (repo 1)

- 22 componentes, 22 patrones, terminología, voz y tono, compliance.
- **62 checks deterministas** en `evals/assertions.py`, **318 casos golden**, 1 caso sin
  candidato a propósito (`statements.none-yet`, ranura permanente de generación).
- **Seis puertas**, todas limpias, hay que ejecutarlas tras cada cambio (desde `evals/`):
  `run_golden.py`, `run_golden.py --strict`, `terms_sync.py`, `check_structure.py`,
  `check_examples.py`, `export_rules.py --check`.
- `evals/rules.json` es el export de todo lo que es DATO (listas, mapa de superficies,
  patrones). La app lo lee; su `parity.test.ts` se pone rojo si se queda atrás.
- Capa de juez: `judge.py generate|build|score`, `rubric.md`, runs en `judge-runs/`.
  Hecha ya una tanda a ciegas (dos subagentes con contexto limpio).
- Marca: grafito `#111827` + fucsia `#DB2777`. Dinero europeo (`150 €`, `2.540,75 €`, sin
  `,00`, dos decimales cuando hay céntimos). 12h am/pm. "working days". Inglés americano.

## Estado de la app (repo 2)

- Home con seis puertas: 01 Voice & tone, 02 Visual identity, 03 Components, 04 Patterns,
  **05 Accessibility** (nueva), 06 Copy checker.
- Páginas de referencia en `public/mockups/*.html`. El checker en `src/`.
- 62 checks, paridad con el sistema verde. La insignia dice **"No rule broken"**, no PASS,
  y en verde añade "Meaning not evaluated. Ask for a second opinion below."
- El juez solo se desbloquea cuando la capa determinista pasa entera.

## Lo último que se hizo (etapas 31 a 37)

1. Interjecciones prohibidas, `A-REPEATED-CHARS` (letra repetida 3+ veces) y "un botón, una
   acción" en `A-CTA`. Salió de una captura suya donde "Oooh", "Yeah", "Retryyyy" y
   "Cancel or die" daban PASS.
2. `check_examples.py`: quinta puerta, barre los ~399 ejemplos aprobados de la
   documentación. Distingue una CITA de la regla de un USO de ella por estructura.
3. Paso de generación en `judge.py` + tanda a ciegas. Hallazgo: tres de los cuatro casos de
   generación tenían la respuesta escrita en la referencia (medían recuperar, no escribir).
4. `export_rules.py` + `rules.json`: sexta puerta. Nació porque la app tenía las listas
   copiadas y llevaba días pasando "Oooh".
5. `A-ATTRIBUTION` (nivel pantalla): un fallo dice de qué lado está. Lo encontró el juez.
6. **`patterns/accessibility.md`**, sección nueva, y `A-COLOR-ALONE` (WCAG 1.4.1).
   Al escribirla se descubrió que 15 ficheros escribían "colour" en su propia prosa, en un
   sistema que prohíbe esa palabra. Corregidos, y `check_examples.py` gana un barrido de
   ortografía sobre la prosa de los documentos.

## Pendiente

- **La skill de Claude** (fase 2 del proyecto): las mismas reglas cargadas como
  instrucciones del agente, para escribir con el sistema en vez de ser juzgado después.
- En la app: página de referencia y superficie de galería para **localización** (se lo pidió
  a Claude Code).
- Una tanda de generación y juicio con un modelo distinto, para tener un número que no sea
  del mismo modelo que escribió el sistema.

## Presentación en clase

El profesor le pidió presentar el proyecto. Hay guión terminado en inglés, unos 4 min 45, en
`~/Desktop/Vanker_presentation_script.md`. Incluye los dos textos de demo:

- **Demo 1** (lo que caza el código, 15 fallos): título `Oooops! Error 500 — Something went
  wrong 😕`, cuerpo con "technical difficulties / kindly / hurry / the button below / retry
  or cancel / 150.00 EUR / didn't", CTAs `OK` y `Retry or Cancel!`.
- **Demo 2** (lo que solo ve el juez, cero fallos deterministas): título `We could not
  complete your payment`, cuerpo `Your payment is on its way and we will confirm it.` +
  `The transaction was rejected by the acquirer on our side. Check your details and try
  again in a few minutes.`, CTAs `Retry` y `Close`.
  La gracia: el título dice que falló y el cuerpo dice que va en camino. La misma frase que
  hace pasar el check es la que hace fallar el juicio.

## Añadido 03/09/2026 (etapa 38): la skill de Claude existe

- `skill/vanker-content-design/`: SKILL.md escrito a mano; `references/` y `scripts/` los
  genera `evals/build_skill.py` desde el repo (séptima puerta: `build_skill.py --check`).
  `--package` produce `skill/vanker-content-design.skill`, que se instala desde un chat.
- Cualquier cambio en documentos o en `assertions.py` obliga a `python build_skill.py --package`
  y a reinstalar la skill; si no, la instalada enseña las reglas del mes pasado.
- Hueco detectado en la prueba: no hay surface de título para notificación in-app; el agente
  usó `push-title`. Pendiente decidir si se añade a `SURFACE_CHECKS`.
- Regla del repo de la app: sin cambios. Si la app quiere una puerta "07 Skill", va al handoff.

## Añadido 03/09/2026 (etapa 39): Figma

- Archivo Figma «Vanker Design System» (clave `9sr6gsJLZ2eHV4XBfH8D27`, borradores de José Luis),
  creado por el conector de Figma desde este chat. Variables (Primitives, Color con modos
  Light/Dark, Spacing, Radius), 15 estilos de texto, 4 sombras, todo desde `components/foundations/`.
- Componentes construidos: Button (30 variantes), Text field (5), Status label (10), Banner (4),
  Toast, Sheet / Modal (2), Empty state (3). Cada uno en su página, con propiedades de texto.
  Pendientes: los otros 15 de `components/library/` y una librería de iconos (los iconos actuales
  son marcadores de posición).
- `skill/vanker-figma-surfaces/`: la skill que monta una surface en Figma desde un prompt, pidiendo
  el copy a `vanker-content-design`. Busca los componentes por nombre, nunca por id.
- Primera surface de demo en la página Surfaces: el modal de pago rechazado (demo 2 del guion).

## Añadido 04/09/2026 (etapa 40): librería Figma completa

- Los 22 componentes de `components/library/` existen en Figma, cada uno en su página con
  variantes, propiedades de texto y descripción que cita su fichero fuente. Iconos: siguen
  siendo marcadores; la librería de iconos es lo único que falta.
- Prueba de extremo a extremo de `vanker-figma-surfaces` con un subagente limpio (banner de
  caducidad del documento): funcionó y destapó tres defectos del Banner (altura fija, rellenos
  blancos sueltos, acción como texto). Corregidos en la librería; la acción del banner es ahora
  un Button anidado. Regla nueva en la skill: un defecto se arregla en el componente, no en la
  instancia.
- Limitación conocida de Figma: una propiedad de texto tiene un solo valor por defecto para
  todo el set, así que las variantes muestran el mismo texto de ejemplo; las instancias lo
  cambian. Las claves de propiedad se leen en tiempo de ejecución, nunca se recuerdan.
