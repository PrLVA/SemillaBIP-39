# Generador de Billetera de Bitcoin Cash (BIP-39)

Este proyecto es una aplicación con interfaz gráfica (GUI) desarrollada en Python que genera frases mnemotécnicas de 12 palabras compatibles con el estándar BIP-39, utilizando simulaciones de lanzamientos de dados. Está diseñada específicamente para crear frases de recuperación para billeteras de Bitcoin Cash, con una interfaz moderna y fácil de usar.

## Características
- Genera 12 palabras mnemotécnicas en español basadas en el estándar BIP-39.
- Simula lanzamientos de un dado de 6 caras (11 lanzamientos por palabra) para generar números aleatorios seguros.
- Interfaz gráfica elegante con tema oscuro y botones interactivos.
- Muestra las palabras enumeradas en un cuadro de texto con barra de desplazamiento.
- Permite copiar las palabras al portapapeles con un solo clic.
- Retroalimentación visual al copiar (el botón cambia a "¡Copiado!" temporalmente).

## Requisitos
Para ejecutar este programa, necesitas tener instalado lo siguiente:
- **Python 3.x** (recomendado: 3.8 o superior).
- Bibliotecas de Python:
  - `tkinter` (generalmente viene con Python).
  - `pyperclip` (para copiar al portapapeles).
  - `mnemonic` (para generar las palabras BIP-39).

Puedes instalar las dependencias con el siguiente comando:
```bash
pip install pyperclip mnemonic
