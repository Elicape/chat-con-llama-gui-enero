import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import threading
import re

# Colores modernos
COLOR_FONDO = "#2E3440"  # Gris oscuro
COLOR_TEXTO = "#ECEFF4"  # Blanco suave
COLOR_BOTONES = "#5E81AC"  # Azul suave
COLOR_BOTONES_ACCION = "#BF616A"  # Rojo suave
COLOR_ENTRADA = "#4C566A"  # Gris medio
COLOR_CHAT_USER = "#88C0D0"  # Azul claro
COLOR_CHAT_ASISTENTE = "#A3BE8C"  # Verde claro

# Rutas del ejecutable y modelo (pueden cambiarse)
LLAMA_EXECUTABLE = "/ruta/a/llama.cpp/build/bin/llama-run"
MODEL_PATH = "/ruta/a/tu_modelo.gguf"

# Función para eliminar secuencias de escape ANSI
def eliminar_secuencias_ansi(texto):
    return re.sub(r"\x1b\[[0-9;]*[mK]", "", texto)

# Función para enviar el mensaje y obtener la respuesta
def enviar_mensaje():
    mensaje = entrada.get("1.0", tk.END).strip()
    if mensaje:  # Verificar que no esté vacío
        # Mostrar mensaje del usuario inmediatamente
        chat.config(state="normal")
        chat.insert(tk.END, f"Tú: {mensaje}\n", "user")
        chat.config(state="disabled")
        chat.yview(tk.END)  # Hacer scroll hacia abajo
        entrada.delete("1.0", tk.END)  # Limpiar el campo de entrada

        # Llamar al modelo en un hilo separado para evitar bloquear la GUI
        threading.Thread(target=obtener_respuesta, args=(mensaje,)).start()

# Función que interactúa con el modelo
def obtener_respuesta(mensaje):
    command = [
        LLAMA_EXECUTABLE,
        MODEL_PATH,
        f"Responde en español: {mensaje}"  # Forzar respuesta en español
    ]
    try:
        proceso = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        respuesta = ""
        while True:
            output = proceso.stdout.readline()
            if output == '' and proceso.poll() is not None:
                break
            if output.strip():
                respuesta += output.strip() + "\n"
                # Eliminar secuencias de escape ANSI
                respuesta_limpia = eliminar_secuencias_ansi(respuesta)
                # Actualizar la respuesta en el chat en tiempo real
                chat.config(state="normal")
                chat.insert(tk.END, f"Asistente: {respuesta_limpia}\n", "assistant")
                chat.config(state="disabled")
                chat.yview(tk.END)
    except Exception as e:
        respuesta = f"Error al obtener respuesta: {str(e)}"
        chat.config(state="normal")
        chat.insert(tk.END, f"Asistente: {respuesta}\n", "assistant")
        chat.config(state="disabled")
        chat.yview(tk.END)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Chat con Llama")
ventana.geometry("600x700")
ventana.config(bg=COLOR_FONDO)

# Cuadro de chat con scroll
chat = scrolledtext.ScrolledText(
    ventana,
    wrap=tk.WORD,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    font=("Arial", 12),
    state="disabled"
)
chat.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Configurar tags para los diferentes tipos de mensajes
chat.tag_config("user", foreground=COLOR_CHAT_USER)
chat.tag_config("assistant", foreground=COLOR_CHAT_ASISTENTE)

# Campo de entrada
entrada = tk.Text(ventana, height=4, font=("Arial", 12), bg=COLOR_ENTRADA, fg=COLOR_TEXTO)
entrada.pack(fill=tk.X, padx=10, pady=10)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg=COLOR_FONDO)
frame_botones.pack(fill=tk.X, padx=10, pady=10)

# Botón de enviar
boton_enviar = tk.Button(
    frame_botones,
    text="Enviar",
    command=enviar_mensaje,
    bg=COLOR_BOTONES,
    fg=COLOR_TEXTO,
    relief="raised",
    font=("Arial", 12)
)
boton_enviar.pack(side=tk.LEFT, padx=5)

# Botón de cerrar
boton_cerrar = tk.Button(
    frame_botones,
    text="Cerrar",
    command=ventana.quit,
    bg=COLOR_BOTONES_ACCION,
    fg=COLOR_TEXTO,
    relief="raised",
    font=("Arial", 12)
)
boton_cerrar.pack(side=tk.RIGHT, padx=5)

# Vincular la tecla "Enter" al envío del mensaje
ventana.bind("<Return>", lambda event: enviar_mensaje())

# Iniciar bucle principal
ventana.mainloop()
