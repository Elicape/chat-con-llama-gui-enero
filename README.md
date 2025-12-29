# Chat con LLaMA – v0.5

Versión funcional temprana de una interfaz gráfica local para ejecutar
modelos LLM mediante `llama.cpp`.

---

## ¿Qué es esto?

Esta aplicación es una versión **anterior** a la primera publicación
formal del proyecto, conservada porque ya era funcional y usable.

Permite interactuar con un modelo de lenguaje local desde una GUI simple,
sin depender de servicios online.

---

## ¿Por qué existe?

En el momento en que se desarrolló esta versión:

- Mi hardware no podía ejecutar aplicaciones modernas y pesadas.
- Las alternativas existentes eran complejas de configurar.
- `llama.cpp` ofrecía una forma ligera y directa de ejecutar modelos locales.

Esta app nace como una solución práctica a ese contexto.

---

## ¿Qué hace?

- Ejecuta un modelo local GGUF mediante `llama.cpp` (`llama-run`)
- Permite enviar mensajes desde una interfaz gráfica
- Muestra la respuesta del modelo en tiempo real
- Limpia secuencias de escape ANSI propias del terminal
- Mantiene la interfaz responsiva mediante hilos

---

## ¿Qué no hace (a propósito)?

- No gestiona múltiples modelos
- No guarda historial
- No resume contexto
- No es plug & play
- No abstrae rutas ni configuraciones

Esta simplicidad es intencional.

---

## Uso básico

### Requisitos

- Python 3
- `llama.cpp` compilado localmente
- Un modelo GGUF compatible

### Preparación

Antes de ejecutar, es necesario editar manualmente las rutas en el archivo
`gui-enero.py`:

```python
LLAMA_EXECUTABLE = "/ruta/a/llama.cpp/build/bin/llama-run"
MODEL_PATH = "/ruta/a/tu_modelo.gguf"
Estas rutas dependen del sistema y de dónde se haya compilado llama.cpp.

Ejecución
python3 gui-enero.py

Sobre esta versión

Aunque se publica como v0.5, esta aplicación corresponde a una etapa
preliminar del proyecto.

Se conserva y publica como referencia histórica funcional, no como versión
final ni estable.

Estado del proyecto

🔒 Versión cerrada
📦 Publicada como referencia
🛠️ No se prevén mejoras sobre este código

Agradecimientos

Proyecto llama.cpp

Autores de los modelos GGUF utilizados

Herramientas de software libre que hicieron posible la experimentación local