import numpy as np
import matplotlib.pyplot as plt

# --- 1. CONFIGURACIÓN DEL TIEMPO ---
dt = 0.1       # Paso del tiempo (segundos)
tiempo_total = 20.0  # Duración del experimento
pasos = int(tiempo_total / dt)

# --- 2. ESTADO INICIAL DEL ROBOT (X, Y, Theta) ---
# Empezamos en el centro (0, 0) mirando hacia la derecha (0 radianes)
x = 0.0
y = 0.0
theta = 0.0

# --- 3. CONTROLES CONSTANTES ---
# Le decimos al robot que avance a 1.0 m/s y gire a 0.3 rad/s (hará un círculo)
v = 1.0
omega = 0.3

# Listas para guardar la trayectoria y poder graficarla después
historial_x = [x]
historial_y = [y]

print("Iniciando simulación matemática del robot...")

# --- 4. BUCLE PRINCIPAL (Integración de Euler) ---
for t in range(pasos):
    # Ecuaciones diferenciales del modelo uniciclo
    x_punto = v * np.cos(theta)
    y_punto = v * np.sin(theta)
    theta_punto = omega
    
    # Actualizamos el estado multiplicando la derivada por el paso del tiempo (dt)
    x = x + x_punto * dt
    y = y + y_punto * dt
    theta = theta + theta_punto * dt
    
    # Guardamos la nueva posición
    historial_x.append(x)
    historial_y.append(y)

print("Simulación terminada con éxito. Generando gráfico...")

# --- 5. GRAFICAR RESULTADOS ---
plt.figure(figsize=(6,6))
plt.plot(historial_x, historial_y, label='Trayectoria del Robot', color='purple', linewidth=2)
plt.plot(0, 0, 'go', label='Inicio (0,0)') # Punto de inicio en verde
plt.title('Simulador Matemático 2D - Modelo Uniciclo')
plt.xlabel('Posición X (Metros)')
plt.ylabel('Posición Y (Metros)')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
