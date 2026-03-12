************
Introducción
************

Cuando necesitas escribir o codificar, tienes que elegir un editor de texto, y uno muy bueno. Hay muchos editores de texto disponibles allí afuera, pero muy pocos de ellos con mas de 40 años de edad. Es el caso de *Emacs* (http://www.gnu.org/software/emacs/), *Vi* y su sucesor mejorado |vim| (http://www.vim.org). Fueron creados en los 70's y aún son usados bastante hoy en dia. Puedes haber notado que no es gracias a la belleza de sus sitios web o la eficiencia de su comunicación. Aquí hay alguna *razones para su exito**:

**Para siempre** 
    Los aprendes una vez y los usarás para siempre. En un mundo donde los lenguajes y tecnologías estan constantemente cambiando, es una verdadera oportunidad para poder invertir a largo plazo.

**Donde sea**
    Estan disponibles para cada uno y cada posible plataforma : MacOS, Windows, GNU/Linux, BSD, y siempre ha sido el caso. 

**Eficiente** 
    Gracias a sus características (como el uso extenso del teclado), puedes editar y escribir texto tan rápido como tus pensamientos.

**Para todo** 
    Ellos te permiten editar todo y nada. Cuando. Cuando vas a usar otro lenguaje de programación u otro lenguaje de marcado, no tendrás que cambiar de editor. Por supuesto, este libro ha sido escrito usando |vim| (y el lenguaje de marcado `ReST Markup <http://sphinx-doc.org/rest.html>`)

Aun, estos editores de texto son difíciles de aprender. No es que sean mas difíciles que cualquier otra cosa, no es nada que no puedas manejar, mas bien porque no hay una forma inteligente allí afuera para aprenderlos por ahora. Entonces, aquí estamos.

El objetivo de este libro es direccionar esta brecha guiandote a través de tu descubrimiento de |vim|. Voy a poner *Emacs* a un lago por ahora y me enfocaré en |vim|. Si quieres saber mas acerca de esta **Guerra de editores**, asegurate de revisar `Wikipedia page <http://en.wikipedia.org/wiki/Editor_war>`. Este libro no pretende ser un libro de referencia acerca de |vim|. Hay muchas buenas referencias sobre el asunto como `A byte of Vim <http://swaroopch.com/notes/vim/>`. Como sea, este libro pretender reducir la barrera para acostumbrarse a |vim|. En mi opinión, la cosa mas difícil acerca de aprender |vim| es no desanimarse y encontrar una forma de usarlo mientras aprendes paso a paso. Todos tenemos que hacer cosas con nuestro editor en el dia a dia, por eso perder toda tu productividad cuando cambias a |vim| no es posible.

Estoy seguro que vas a encontrar muchas personas que te digan: "Solo hazlo", "Verás, es dificil al principio, pero el tiempo ayudará". Es cierto, pero aún tienes el problema de tratar de mantener tu productividad en el dia a dia. El enfoque de este libro es el siguiente:

- Tener un |vim| moderno: resaltado de sintaxis y colores agradables.
- Usar |vim| como cualquier otro editor: fácil edición de código y cambiar entre archivos usando el ratón.
- Aprender atajos de teclado y dejar de usar el ratón paso a paso.
- Instalar los *mejores* plugins para empezar usando |vim| en todo su potencial.

Empezando con el punto número 2, serás capaz de usar |vim| en el dia a dia sin perder mucha productividad. Es donde la mágia sucede: si puedes integrar |vim| en los hábitos de tu dia a dia, habrás ganado. Entonces tendrás el resto de tu vida para aprender todos los atajos y trucos de |vim|.

¿Estás cansado de probar un nuevo editor cada año? ¿Estás cansado de tener que volver a aprender todo de cero cada vez? ¿Estás cansado de tener que cambiar de editor cuando estas usando Mac, Windows o Linux? Entonces, solo para, y ¡únete a la comunidad de personas felices con sus editores de texto!

¿Para quién?
============

Cada persona que tiene que producir texto (código, libros, informes, diapositivas) regularmente. Desarrolladores son porsupuesto considerados, pero no es solo para ellos.

Por ejemplo, tu eres un:

**Estudiante**
    Si tu quieres impresionar a tu futuro jefe con tu currículum, es un deber. Es una prueba de seriedad ver que un estudiante tomó parte de su tiempo para aprender |vim|. Mas aún, tendrás una herramienta única para escribir todo lo que tengas que escribir (y serás capaz de usarlo para el resto de tu carrera): tus informes en LaTeX, tus diapositivas, tu código (si necesitas Word o LibreOffice para escribir tus informes, es momento de usar `LaTeX <http://en.wikipedia.org/wiki/LaTeX>`_, `Markdown <http://en.wikipedia.org/wiki/Markdown>`_ or `reStructuredText <http://en.wikipedia.org/wiki/ReStructuredText>`_).
).

    Consejo amistoso: para tus diapositivas, no vaciles en usar algo como `impress.js <http://bartaz.github.com/impress.js>`_. Usa HTML/JS/CSS y recomiendo altamente que lo uses para hacer presentaciones asombrosas basadas en tecnologías no propietarias. Puedes echarle un vistazo a `reveal.js <http://lab.hakim.se/reveal-js/>`_ también, y este editor en liniea `slide.es <http://slid.es/>`_.

**Profesor** 
    Es momento de dar un ejemplo para tus estudiantes y enseñarles una herramienta que usarán durante su vida entera. Mucho mas que cualquier lenguaje de programación.

**Coder** 
    Invertir tiempo en tu herramienta diaria es algo esencial. De todos modos tendrás que aprender atajos de teclado, así que mejor hazlo en algo útil. Si esta inversión es aún rentable dentro de 10 años, es la perfecta inversión, es |vim|.

**Administrador de sistemas y redes**
    Si usas *Emacs*, puedo perdonarte. Si usas nano/pico, no hay nada que puedo hacer por ti. de otra manera, ¡es momento de hacer algo de trabajo! Administrar sistemas Unix remotamente es el caso de uso perfecto para |vim| (un editor de texto poderoso sin la necesidad de una interfaz gráfica).

**Escritor** 
    Si eres un escritor usando Markdown/reStructuredText/WikiMarkup o LaTeX, |vim| te ahorrará mucho tiempo, No serás capaz de regresar hacia otro editor luego, o querrás *Vimificarlo* a toda costa.

Creeme, He hecho y aún hago todos estos 5 roles, y mi mejor inversión ha sido, por mucho, |vim|.

Lo que estarás aprendiendo
==========================

- Como usar |vim| como un editor "usual" al inicio (ya sabes, el tipo de editor de texto que tiene coloreado de sintaxis, que te permita abrir archivos, hacer click usando el ratón). En resumen, la demistificación de |vim| que te permitirá ir mas lejos.
- Como migrar de la clásica edición de texto hacia el proder de |vim|, paso a paso de bebé (es donde la adicción commienza).
- Como hacerlo sin usar el ratón y por que es la mejor cosa que te puede pasar cuando codificas/escribes texto.
- Como puedes facilmente deducir atajos del teclado com algunas reglas simples.

Para resumir: como te consideras a ti mismo un artesano, actua como uno. Aprende como usar tu herraminta, de una vez por todas.

Lo que no estarás aprendiendo
=============================

- Tu no estarás aprendiendo como instalar y configurar |vim| en Windows. Es realizable. pero tengo muy limitado conocimiento acerca de Windows. puede pasar pero no aún. Solo Linux/Unix será discutido (y por extensión MacOS).
- Tu no estarás aprendiendo como usar *Vi* (Date cuenta de la falta de "*m*"). Solo te enseñaré como ser productivo escribiendo texto con |vim|, No te enseñaré como impresionar a tus amigos con *Vi* (y de todos modos, |vim| es suficiente para eso). Para quienes no entienden acerca de que estoy hablando, *Vi* es el ancestro de |vim| (lo que significa *Vi* - *IMproved*) y está instalado por defecto en todos sistemas similares a Unix (incluido MacOS).
- Tu no estarás aprendiendo a conocer |vim| por dentro: este libro no es una referencia, es una forma práctiva de aprender |vim|.
- Tu no estarás aprendiendo como personalizar los colores de tu |vim|: Usaré el tema `Solarized <http://ethanschoonover.com/solarized>`, es el mejor tema para tus ojos.

La parte dificil es empezar
===========================

Entonces, ¿estas listo para la aventura? ¿listo para sacrificar una hora para empezar a usar |vim|, una semana para estar familiarizado con él, y el resto de tu vida para ser feliz con tu elección? ¡Entonces aquí vamos!, casi, solo necesitamos hablar un poco antes.

Con |vim| tendrás que luchar. No importa cuan grande sea la fuerza de voluntad, lucharás. Estar preparado. El objetivo de esta guia es disminuir esta lucha tanto como sea posible, pero estar consciente que tendrás que luchar de todos modos, Sin dolor no hay ganancia. Este es el método que recomiendo para domar a la bestia:

- Intenta hacer un hábito el uso de |vim|. Asegurate de seguir esta guia hasta el capitulo *The NERD Tree* (el explorador de archivos). Luego serás capaz de usar |vim| como lo harías con Notepad++, Textmate o Sublime Text por ejemplo. Estarás usando solo 1% de las capacidades de |vim|, pero como sea, lo que importa es usar |vim| en tu dia a dia.
- Asgurate de tener una hoja impresa con todos los atajos principales de |vim| cerca de tí. El objetivo aquí no es aprenderlos de memoria, sino para tener algún lugar a donde mirar cuando te preguntes a ti mismo: "seguramente existe una mejor forma de hacer esto".
- Manten la fé. Al principio serás escéptico respecto a la utilidad de aprender todo desde cero con |vim|. Y luego, un dia, tendrás un momento "¡ajá!". Te preguntarás a ti mismo por que todos los softwares que usas no pueden ser controlados usando los atajos de |vim|.
- Mantén en tu mente que esto es una inversión para tus siguientes 20 años. Y todos saben que una inversión es raramente rentable inmediatamente.

Suficiente charla, ¡vamos a empezar!
