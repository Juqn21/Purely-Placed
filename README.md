# 🧩 Enfócate | Purely Placed

**Enfócate** es un juego de acertijos minimalista basado en la satisfacción visual y el orden. Inspirado en la estética *cozy*, el objetivo es organizar objetos cotidianos de manera armónica, lógica o simétrica.

---

## 📐 Concepto: Purely Placed
El diseño del juego se rige por la filosofía **Purely Placed**, donde cada píxel cuenta:
* **Orden Táctil:** Mecánicas de "Drag & Drop" suaves y precisas.
* **Satisfacción Visual:** Alineaciones perfectas y paletas de colores coherentes.
* **Minimalismo Cognitivo:** Sin interfaces saturadas. El puzzle es el centro de atención.

---

## 🕹️ Mecánicas de Juego
* **Grid Alignment:** Los objetos deben encajar en una rejilla invisible o seguir un patrón lógico (tamaño, color, forma).
* **Interacción Intuitiva:** Arrastra, rota y coloca elementos hasta que "se sientan" en el lugar correcto.
* **Feedback Auditivo:** Sonidos sutiles y relajantes que confirman cuando un objeto está bien colocado.

---

## 🛠️ Especificaciones Técnicas
* **Motor:** Pygame 2.x
* **Lógica de Colisiones:** Máscaras de colisión precisas para detectar el encaje exacto de piezas.
* **Arquitectura:** Basada en estados (Menú, Selección de Nivel, Puzzle, Éxito).

---

## 📁 Estructura del Proyecto
```text
root/
├── assets/
│   ├── fuentes/       # Fuentes
│   ├── images/ # Imagenes a usar
│   
├── src/
│   ├── engine/      # Lógica de arrastrar y soltar (Drag & Drop)
│   ├── states/      # Control del flujo del juego
│   └── puzzles/     # Configuración de cada nivel de orden
└── main.py # Ejecutable principal
