# Vanker Content Design System: contexto completo del proyecto

Fecha: 4 de septiembre de 2026. Documento de contexto para abrir un chat nuevo con toda la
información del proyecto: qué es, qué requisitos lo definen, qué se ha construido, cómo está
organizado, qué proceso se siguió y qué queda abierto.

## 1. Qué es el proyecto

Vanker es un neobanco ficticio de la zona euro. El proyecto es su **sistema de diseño de
contenido**: un repositorio de reglas (voz y tono, terminología, patrones de copy,
especificaciones de componentes y guardarraíles regulatorios) escrito para que lo usen a la
vez personas y un agente de IA, de modo que un modelo pueda redactar toda la experiencia
digital del banco on-brand y conforme al marco regulatorio europeo, y que ese resultado se
pueda medir.

Autor y dueño de las decisiones: José Luis Escuadra Valle, content designer senior. Uso:
material docente para dos cursos de Maven (IA Accelerator y Evals) y proyecto presentado en
clase; el profesor pidió tres artefactos a partir del sistema: una web app, una skill de
Claude y una integración con Figma. Los tres existen.

Vanker es ficción. Nada del sistema es asesoramiento financiero ni un producto real; la capa
de compliance traduce el marco europeo a obligaciones de contenido pero no ha sido revisada
por un profesional legal (`DISCLAIMER.md`).

## 2. Requisitos y decisiones fijadas

Estas decisiones son las que definen el proyecto y no se reabren sin motivo.

| Requisito | Decisión |
| --- | --- |
| Idioma del producto | Inglés americano («color», «canceled», «email»). Todo el sistema y todo el copy están en inglés. |
| Mercado | Zona euro. Vocabulario europeo (IBAN, SEPA transfer); nunca «checking account», «routing number», «ACH». |
| Formato de dinero | Europeo aunque el texto sea inglés: `150 €`, `2.540,75 €`, `10,10 €`. Símbolo detrás con espacio, millares con punto, decimales con coma, sin `,00` en cantidades redondas, dos decimales exactos cuando hay céntimos. Nunca redondear el dinero de una persona. |
| Cifras, fechas y horas | Dígitos («3 steps»); fechas escritas día mes año («4 September 2026»), nunca numéricas ni con ordinal ni mes primero; solo «Today» es relativo; horas de 12 h con espacio y minúsculas («2:32 pm»); plazos como rango en «working days». |
| Marca | Grafito `#111827` y fucsia `#DB2777`; Plus Jakarta Sans (producto) y Space Grotesk (solo marketing); sistema plano, esquinas de 12 px, motion calmado. |
| Voz | «Un amigo listo, moderno y bien informado que es brillante con el dinero»: claridad primero, del lado de la persona, calmado, sin hype ni jerga. Referencias: Apple y Revolut/N26. |
| Puntuación | Sentence case siempre; nunca exclamaciones, punto y coma, puntos suspensivos, rayas, abreviaturas latinas ni emoji; rangos con «to»; signo menos real (−). |
| Precedencia entre capas | `CLAUDE.md` > `compliance/` > `terminology/` > `voice-and-tone/` > `patterns/` > `components/`. Los ejemplos nunca prevalecen sobre las reglas. |
| Prohibiciones absolutas | Prometer rentabilidad o «sin riesgo»; urgencia o escasez falsas; ocultar comisiones, plazos o condiciones; garantías no autorizadas (protección de depósitos); pedir más datos de los necesarios; obstaculizar una reclamación; opiniones médicas, legales o fiscales como hechos. |
| Obligaciones | Incluir los avisos y disclosures que exige `compliance/` para cada superficie; transparencia de comisiones y plazos; expandir siglas en primera mención salvo las de uso general; ruta de reclamación accesible; términos controlados del glosario; etiqueta visible y persistente en cada campo; las llamadas a la acción van en botones, nunca en el cuerpo; un botón, una acción. |
| Regla de seguridad | Si una cadena toca dinero, riesgo, términos legales, protección de depósitos o datos personales y `compliance/` no la cubre claramente, no se inventa la redacción: se marca `[NEEDS COMPLIANCE REVIEW]` y se deja el resto usable. |
| Localización | Una cadena es una frase completa con variables nombradas (`{amount}`, `{date}`); nunca se concatena en tiempo de ejecución. Nunca se señala algo por su color ni por su posición en pantalla. |
| Estados de error de sistema | Toda pantalla que interrumpe un movimiento de dinero dice qué pasó con el dinero con una de tres frases fijas: «No money has left your account.», «Your payment is on its way and we will confirm it.», «We do not know yet whether it went through, and we will tell you as soon as we do.». Y dice de qué lado está el problema. Nunca «Something went wrong», nunca códigos de error visibles. |

## 3. Los repositorios y la documentación

Hay dos repos, ambos locales en el Mac y en GitHub, con un dueño cada uno.

| Repo | Ruta local | GitHub | Qué es | Dueño |
| --- | --- | --- | --- | --- |
| Sistema | `~/Desktop/Content_Design_System_AI` | `joseluisescuadravalle/Vanker_neobank_content_design_system` | La fuente de verdad: reglas, evals, skills | Cowork (este chat) |
| App | `~/Desktop/Vanker_content_desktop_app` | `joseluisescuadravalle/Vanker-desktop-app` | Web y comprobador de copy (Vite + React + TypeScript), cliente del sistema | Claude Code |

Lo que cruza la frontera entre repos se escribe en el handoff (`_handoff/`), nunca se hace
desde el otro lado. José Luis hace `git add/commit/push` desde Terminal con el bloque bash
que se le da; el mount de Cowork deja `index.lock`, de ahí el `rm -f .git/index.lock`.

### 3.1 Estructura del repo del sistema

```
Content_Design_System_AI/
├── CLAUDE.md              carta fundacional: precedencia, prohibiciones, obligaciones, regla de seguridad
├── README.md, DISCLAIMER.md, CONTRIBUTING.md, DESKTOP_APP_BRIEF.md
├── voice-and-tone/        voice.md, tone.md, inclusive-language.md (4 ficheros)
├── terminology/           glossary, banned-terms, capitalization-and-punctuation, numbers-and-dates, localization (6)
├── patterns/              22 patrones: ctas, links, errors, system-errors, loading, forms, search, confirmations,
│                          success, empty-states, notifications, emails, auth, cards, permissions, flow-intro,
│                          welcome-carousel, charts, currency-exchange, complaints, alt-text, accessibility
├── components/
│   ├── foundations/       color, typography, shape, spacing, elevation, iconography, motion (7), con bloque JSON de tokens
│   └── library/           22 componentes: button, text-field, textarea, date-field, dropdown, checkbox, radio-group,
│                          card, transaction-row, status-label, count-badge, chip, amount-input, code-input, tooltip,
│                          accordion, toggle, navigation, sheet-modal, banner-toast, empty-state, onboarding-step
├── compliance/            framework, principles, disclosures, risk-warnings, security-payments, identity-kyc,
│                          complaints, data-privacy, accessibility (10). Módulos condicionales: crédito, cripto, inversión
├── evals/                 la capa de evaluación (ver sección 4)
├── skill/                 las dos skills de Claude (ver sección 5)
└── _handoff/              notas de contexto entre sesiones y entre repos
```

Cada fichero de componente o patrón sigue la misma anatomía, en este orden, y
`check_structure.py` la exige: título y estado (`normative`, `normative + example`,
`tooling`); qué es en dos frases y la tesis (la única idea por la que existe el fichero);
«what this is not» cuando hay confusión probable; slots (componente) o situaciones (patrón);
reglas numeradas, cada una con su razón dentro; estados y comportamiento; accesibilidad como
sección propia; ejemplos con ✅ y ❌ y la razón de cada ❌; un bloque JSON legible por máquina;
y «Eval hooks», las reglas reescritas como cosas verificables.

La regla sobre las reglas: **cada regla lleva su razón**, porque un agente sigue la regla que
entiende e improvisa alrededor de la que no. Se escribe desde el fallo (qué sale mal si no) y
se declara la tensión cuando una regla choca con otra.

## 4. La capa de evaluación (`evals/`)

Dos capas: **aserciones deterministas** (código, `assertions.py`, 62 checks con id `A-*`,
por ejemplo `A-EURO-FORMAT`, `A-NO-BANNED`, `A-CTA`, `A-MONEY-ACCOUNTED`, `A-COLOR-ALONE`) y
**juez** (un modelo puntúa con `rubric.md` siete dimensiones de 0 a 2: voz, tono, claridad,
terminología, patrón, compliance, accesibilidad; pasa si ninguna aplicable es 0, compliance y
tono nunca 0, y el total llega al 85 % del máximo aplicable). La capa barata va primero y
nunca se envía al juez lo que el código ya rechazó.

Los checks son sensibles a la superficie: `SURFACE_CHECKS` mapea 72 ids de superficie
(`cta`, `field-error`, `push-title`, `system-error-screen`, `label-in`, `toast`...) a los
checks que aplican, y `UNIVERSAL` añade seis a todas.

El golden set (`golden-set/cases.jsonl`) tiene 319 casos: 318 con candidato aprobado (122 de
ellos negativos, que deben fallar) y `statements.none-yet`, la ranura permanente de
generación, que nunca lleva candidato para que el camino de generación no se pudra.

**Siete puertas**, todas limpias, que se ejecutan tras cada cambio desde `evals/`:

1. `python3 run_golden.py`: la capa determinista sobre el golden set.
2. `python3 run_golden.py --strict`: audita casos que declaran menos checks de los que su superficie aplica.
3. `python3 terms_sync.py`: `banned-terms.md` y `assertions.py` de acuerdo (74 términos documentados, 72 implementados).
4. `python3 check_structure.py`: cada componente y patrón lleva la anatomía.
5. `python3 check_examples.py`: los 399 ejemplos aprobados de la documentación no contradicen ninguna regla actual, más un barrido ortográfico de la prosa.
6. `python3 export_rules.py --check`: `rules.json` (todo lo que es dato: listas, mapa de superficies) está al día; la app lo lee en vez de tener copias.
7. `python3 build_skill.py --check`: la skill de Claude no ha derivado del repo.

La capa de juez: `judge.py generate | build | score`, con runs en `generation-runs/` y
`judge-runs/`. Ya hubo una tanda a ciegas (dos contextos limpios, uno genera y otro juzga):
el copy pasó la capa determinista y el juez dio 2 en todas las dimensiones aplicables. Es
ciega en contexto, no en modelo: falta una tanda con un proveedor distinto.

Trampas documentadas en `CONTRIBUTING.md` (todas ocurrieron y todas tienen ya herramienta):
un caso solo ejecuta los checks que declara; las listas de superficies se escriben a mano;
coincidencia por subcadena («ACH» en «reach»); documento y código derivan; el juez corrige su
propio examen si ve la nota `expected`; una segunda implementación con las reglas copiadas se
queda atrás (la app pasó «Oooh» y «Cancel or die» durante días); el generador lee la
respuesta en la referencia; el generador se puntúa a sí mismo; una regla nueva invalida
ejemplos antiguos; un run determinista verde se lee como «el copy es bueno».

## 5. Los tres artefactos

| Artefacto | Dónde se usa | Qué hace | Estado |
| --- | --- | --- | --- |
| Web app (repo de la app) | Navegador, `npm run dev`, `localhost:5174` | Home con seis puertas (Voice & tone, Visual identity, Components, Patterns, Accessibility, Copy checker). El checker ejecuta los 62 checks en TypeScript leyendo `rules.json` y muestra «No rule broken» (nunca PASS) con la nota «Meaning not evaluated»; el juez, llamado «revisión editorial», solo se desbloquea cuando la capa determinista pasa entera. | En uso; paridad con el sistema verde (`parity.test.ts`) |
| Skill `vanker-content-design` | Chat de Claude (Claude.ai, app, Cowork, Code) | El sistema cargado como instrucción: el agente identifica superficie y slots, lee componente, patrón y compliance, escribe, pasa `scripts/check_copy.py` (mismo código que `assertions.py`), hace la lectura de pantalla, genera el prompt de revisión editorial (`scripts/editorial_review.py`), lo entrega a un revisor de contexto limpio y cierra con `Editorial review: pass, 13 of 14, independent` (o «same run» cuando no hay subagente). Formato de entrega `slot (surface): text`, el mismo que lee el checker. | Instalada; probada: 100 % de reglas frente a 44 % sin skill |
| Figma: archivo «Vanker Design System» + skill `vanker-figma-surfaces` | Figma (conector oficial de Figma en Claude, servidor remoto) | Archivo con variables (Primitives, Color con modos Light y Dark, Spacing, Radius), 15 estilos de texto, 4 sombras y los 22 componentes con variantes y propiedades de texto, todo derivado de los JSON de `foundations/` y `library/`. La skill monta una surface desde un prompt: pide el copy a la skill de contenido, busca los componentes por nombre, lee las claves de propiedad en tiempo de ejecución, monta instancias en la página Surfaces y deja el prompt como procedencia. | Publicado como librería de equipo el 04/09/2026. Clave del archivo: `9sr6gsJLZ2eHV4XBfH8D27`, carpeta «Vanker» |

Cómo se generan y mantienen las skills: `evals/build_skill.py` copia al `skill/` los
documentos (`references/`), el checker y `rules.json` (`scripts/`), genera `INDEX.md`
(superficie → checks → ficheros que la gobiernan) y `owners.json`, y escribe `MANIFEST.json`
con el hash de cada fuente; `--check` es la séptima puerta y `--package` produce el fichero
`.skill` que se instala con «Save skill» desde un chat. Tras cualquier cambio en el sistema,
la skill instalada hay que reinstalarla. La skill de Figma se edita a mano y se empaqueta
como zip de su `SKILL.md`; cuando se cambia la librería desde el chat, José Luis tiene que
volver a pulsar Publish en Figma.

Huecos conocidos: no hay librería de iconos en Figma (los iconos son marcadores); no existe
superficie de título para notificación in-app (se usa `push-title`); Space Grotesk no tiene
peso 800, así que `marketing/display-lg` usa Bold; una propiedad de texto de Figma tiene un
solo valor por defecto para todo el set de variantes.

## 6. El proceso que se siguió

El sistema se construyó del 25 de agosto al 4 de septiembre de 2026 en 84 commits, en
sesiones numeradas por etapas.

1. **Carta y capas (25 a 27 de agosto).** `CLAUDE.md` con precedencia y reglas duras;
   voz y tono alineados a inglés americano; terminología; patrones básicos (errores, CTAs,
   confirmaciones, empty states, notificaciones); foundations con tokens JSON; primeros
   componentes; capa de compliance.
2. **Evals (28 a 30 de agosto).** Enfoque en dos capas, `assertions.py`, golden set,
   rúbrica y prompt del juez; primeras puertas (`run_golden`, `--strict`, `terms_sync`).
3. **Ampliación a 22 componentes y 22 patrones (hasta el 1 de septiembre).**
   `CONTRIBUTING.md` con la anatomía y las trampas; `check_structure.py`.
4. **Etapas 31 a 37 (1 de septiembre).** Interjecciones prohibidas, `A-REPEATED-CHARS`,
   «un botón, una acción»; `check_examples.py` (quinta puerta); paso de generación en
   `judge.py` y tanda a ciegas; `export_rules.py` y `rules.json` (sexta puerta) tras
   descubrir que la app tenía las listas copiadas; `A-ATTRIBUTION`;
   `patterns/accessibility.md` y `A-COLOR-ALONE`, que destapó 15 ficheros escribiendo
   «colour» en un sistema que lo prohíbe.
5. **Etapa 38 (3 de septiembre): skill de contenido.** `SKILL.md` a mano, `build_skill.py`
   (séptima puerta), `check_copy.py`; prueba con tres prompts, con y sin skill, calificada por
   el propio checker; el ejemplo del `SKILL.md` falló el checker por parafrasear una de las
   tres frases fijas sobre el dinero, y se corrigió.
6. **Etapa 39 (3 de septiembre): Figma, primera tanda.** Archivo creado desde el chat con el
   conector de Figma; fundamentos como variables y estilos; siete componentes; primera
   surface de demo (el modal de pago rechazado, la «demo 2» del guion de clase); skill
   `vanker-figma-surfaces`.
7. **Etapa 40 (4 de septiembre): Figma completo.** Prueba de extremo a extremo con un
   agente limpio (banner de caducidad del documento) que destapó defectos del Banner
   (altura fija, rellenos blancos, acción como texto), corregidos; los 15 componentes
   restantes; regla «un defecto se arregla en el componente, no en la instancia».
8. **Etapa 41 (4 de septiembre): revisión editorial en la skill.** `editorial_review.py`,
   rúbrica y prompt del juez dentro de la skill; prueba con la sheet de confirmación de una
   transferencia (13 de 14); alineación del glosario con la práctica en SEPA e IBAN (no se
   expanden en producto). Publicación del archivo de Figma como librería de equipo.

La presentación en clase tiene guion en inglés (unos 4 min 45) en
`~/Desktop/Vanker_presentation_script.md`, con dos demos: la que caza el código (un error
con 15 fallos: «Oooops! Error 500 — Something went wrong 😕», «kindly», «hurry», «150.00
EUR», CTAs «OK» y «Retry or Cancel!») y la que solo ve el juez (título «We could not complete
your payment» sobre un cuerpo que dice «Your payment is on its way»: cero fallos
deterministas y un fallo de sentido).

El PRD de la app está en `~/Desktop/Vanker_content_desktop_app/docs/Vanker-app-requirements.pdf`
y el brief de arranque de la app en `DESKTOP_APP_BRIEF.md` del repo del sistema
(stakeholders: content designer, product designer, ingeniero, PM, legal; funciones:
navegador de referencia, comprobador, visor y exportador de tokens, generador, panel de
evals).

## 7. Cómo se trabaja en este proyecto

Acompañamiento didáctico antes que entregables: se explica la decisión en el chat y el
documento es el acta. Cuando se pide copy, se enseña para validar antes de fijarlo en el
golden set. Cada sesión se encabeza con «Etapa N — Sección». Se etiquetan las afirmaciones
que sostienen una decisión: [Cierto], [Probable], [Suposición]. Si hay un fallo de fondo en
un planteamiento, se abre con «No estoy de acuerdo porque [razón]. Alternativa: [X]. Riesgo
de tu planteamiento: [Y]»; si no lo hay, no se fabrica desacuerdo. Nunca se usa la raya (—):
incisos entre paréntesis, en chat y en documentos. Se desarrollan las siglas entre
paréntesis. Se da el texto terminado, nunca referencias a fragmentos anteriores. Cuando se
entrega una herramienta, se enseña primero lo que produce con un ejemplo; el control de
calidad se ofrece, no se impone. Respuestas completas al primer intento, sin ofrecimientos
de mejoras posteriores. Español de España en el chat; inglés en todo lo que es sistema.

## 8. Estado y pendientes

Estado a 4 de septiembre de 2026: siete puertas limpias; skills instaladas y probadas;
librería de Figma completa y publicada; árbol de git limpio (último commit `83578bc`).

Pendiente, por orden de valor:

1. Una tanda de generación y juicio con un modelo de otro proveedor, para tener un número que
   no venga del mismo modelo que escribió el sistema.
2. En la app (Claude Code): página de referencia y galería para localización, y la puerta
   «07 Skill» si se quiere enseñar la skill desde la web.
3. Librería de iconos en Figma, y sustituir los marcadores en los componentes.
4. Añadir una superficie de título para notificación in-app en `SURFACE_CHECKS`.
