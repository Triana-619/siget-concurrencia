import threading
import time
import random
from collections import deque

# ==========================
# CONFIGURACIÓN DEL SISTEMA
# ==========================

BUFFER_SIZE = 5
NUM_SENSORES = 3
NUM_MODULOS = 2
SIMULATION_TIME = 20  # segundos

# ==========================
# RECURSOS COMPARTIDOS
# ==========================

buffer = deque()

# Semáforos
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

# Control de ejecución
running = True

# ==========================
# CLASE SENSOR (PRODUCTOR)
# ==========================

class Sensor(threading.Thread):
    def __init__(self, sensor_id):
        super().__init__()
        self.sensor_id = sensor_id

    def run(self):
        global running
        while running:
            dato = {
                "sensor": self.sensor_id,
                "vehiculos": random.randint(20, 120),
                "velocidad_promedio": random.randint(30, 80),
                "timestamp": time.time()
            }

            empty.acquire()
            mutex.acquire()

            buffer.append(dato)
            print(f"[SENSOR {self.sensor_id}] Produce -> {dato}")

            mutex.release()
            full.release()

            time.sleep(random.uniform(0.5, 2))


# ==========================
# CLASE MODULO (CONSUMIDOR)
# ==========================

class ModuloAnalisis(threading.Thread):
    def __init__(self, modulo_id):
        super().__init__()
        self.modulo_id = modulo_id

    def run(self):
        global running
        while running:
            full.acquire()
            mutex.acquire()

            if buffer:
                dato = buffer.popleft()
                print(f"    [MODULO {self.modulo_id}] Procesa -> {dato}")

            mutex.release()
            empty.release()

            time.sleep(random.uniform(1, 3))


# ==========================
# EJECUCIÓN PRINCIPAL
# ==========================

if __name__ == "__main__":

    sensores = [Sensor(i+1) for i in range(NUM_SENSORES)]
    modulos = [ModuloAnalisis(i+1) for i in range(NUM_MODULOS)]

    for s in sensores:
        s.start()

    for m in modulos:
        m.start()

    # Simulación durante cierto tiempo
    time.sleep(SIMULATION_TIME)
    running = False

    print("\nFinalizando simulación SIGET...\n")