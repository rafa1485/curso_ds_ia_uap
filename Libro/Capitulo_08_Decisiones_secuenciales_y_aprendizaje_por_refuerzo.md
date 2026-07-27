# Capitulo 8. Decisiones secuenciales y aprendizaje por refuerzo

## 8.1. Decisiones bajo incertidumbre

Una alternativa produce consecuencias inciertas. La utilidad esperada es `EU(a)=sum_s P(s|a)U(s,a)`. La aversion al riesgo se representa con una funcion concava. El valor de informacion es la mejora esperada al observar una variable antes de decidir menos su costo.

### 8.1.6. Ejemplo practico guiado

Comparar inspeccion y reparacion considerando probabilidad de fuga, costos, danos evitados y accion posterior.

## 8.2. Procesos de decision de Markov

Un MDP se define como `(S,A,T,R,gamma)`. La propiedad de Markov exige que el futuro dependa del estado actual y accion, no de toda la historia. Para una politica `pi`, `V^pi(s)=E[sum_t gamma^t R_{t+1}|S_0=s]`. Bellman:

`V^pi(s)=sum_a pi(a|s) sum_s' T(s'|s,a)[R(s,a,s')+gamma V^pi(s')]`.

### 8.2.7. Ejemplo practico guiado

Formular un control de deposito de agua con estados de nivel, acciones de bombeo, transiciones inciertas y recompensas por servicio menos costo.

## 8.3. Resolucion de procesos de decision

La iteracion de politicas evalua una politica y la mejora. La iteracion de valores aplica repetidamente el maximo de Bellman:

`V_{k+1}(s)=max_a sum_s' T(s'|s,a)[R+gamma V_k(s')]`.

La convergencia depende de descuento, representacion y precision. El costo crece con estados y acciones.

### 8.3.6. Ejemplo practico guiado

Modificar costos de energia y penalizaciones por desabastecimiento, observar cambios de politica y sensibilidad.

## 8.4. Aprendizaje por refuerzo

El agente aprende de recompensas. Exploracion busca informacion; explotacion usa la mejor accion conocida. Q-learning actualiza fuera de politica:

`Q(s,a) <- Q(s,a) + alpha[r + gamma max_a' Q(s',a') - Q(s,a)]`.

SARSA usa la accion siguiente realmente elegida. Una recompensa mal disenada puede producir atajos peligrosos; se necesitan limites, abstencion y monitoreo.

### 8.4.9. Ejemplo practico guiado

Entrenar en un entorno discreto, comparar Q-learning y SARSA, graficar recompensa por episodio y verificar que la politica no viole restricciones.

## Sintesis

La decision secuencial combina incertidumbre, estado, accion, recompensa y horizonte. Aprender una politica no elimina la necesidad de diseñar objetivos seguros.
