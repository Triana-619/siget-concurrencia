# SIGET - Simulación de Concurrencia con Semáforos

## 📌 Descripción del Proyecto

Este proyecto implementa una simulación del problema clásico **Productor-Consumidor**, adaptado a un **Sistema Inteligente de Gestión de Tráfico (SIGET)**.

El objetivo es demostrar el control y sincronización de procesos concurrentes utilizando **semáforos**, evitando condiciones de carrera, desbordamiento del buffer y bloqueos.

---

## 🏙️ Escenario Simulado

En el sistema SIGET:

-  **Sensores de tráfico (Productores)** generan datos sobre:
  - Cantidad de vehículos
  - Velocidad promedio
  - Marca de tiempo

-  **Módulos de análisis (Consumidores)** procesan los datos generados por los sensores.

-  **Buffer compartido** almacena temporalmente los datos antes de ser procesados.

El buffer tiene capacidad limitada, simulando restricciones reales en sistemas críticos.

---

## ⚙️ Arquitectura de Concurrencia

El sistema utiliza:

- 3 sensores (hilos productores)
- 2 módulos de análisis (hilos consumidores)
- 1 buffer compartido de tamaño limitado
- 3 semáforos para sincronización

---

## 🔐 Mecanismos de Sincronización

### 1️⃣ `empty`
Controla los espacios disponibles en el buffer.  
Evita que los sensores escriban cuando el buffer está lleno.

### 2️⃣ `full`
Controla la cantidad de datos disponibles.  
Evita que los módulos intenten consumir cuando el buffer está vacío.

### 3️⃣ `mutex`
Garantiza exclusión mutua.  
Asegura que solo un hilo acceda al buffer a la vez.

---

## 🚫 Problemas de Concurrencia Prevenidos

El sistema evita:

- ❌ Condiciones de carrera
- ❌ Corrupción de datos
- ❌ Desbordamiento del buffer
- ❌ Consumo de datos inexistentes
- ❌ Interbloqueo (deadlock)

