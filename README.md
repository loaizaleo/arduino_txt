# arduino_txt

Lee la señal de un **sensor de pulso cardíaco** con Arduino y guarda los datos en un archivo de texto en la computadora.

## Objetivo

Capturar una señal analógica del Arduino y guardarla en un archivo para graficarla o analizarla después (por ejemplo, calcular la frecuencia cardíaca).

## Lenguaje y tecnologías

- **Arduino (C/C++)**
- **Python 3** con `pyserial`

### Componentes

- Placa Arduino (Uno o similar)
- Sensor [PulseSensor](https://pulsesensor.com/): cable morado (señal) al pin analógico **A0**

## Archivos

| Archivo | Descripción |
|---|---|
| `sketch_feb11a.ino` | Lee el sensor cada 10 ms y envía `tiempo(s)` y `señal` por serial. Enciende el LED del pin 13 cuando la señal supera el umbral (520). |
| `comm_2.py` | Lee 1200 líneas del puerto serial y las guarda en `pulsor_sensor.dat`. |

## Uso

1. Suba `sketch_feb11a.ino` al Arduino con el IDE de Arduino.
2. Instale `pyserial` y ejecute el script:

   ```bash
   pip install pyserial
   python comm_2.py
   ```

3. El archivo `pulsor_sensor.dat` queda con dos columnas separadas por tabulación:

   ```
   tiempo(s)    señal(0-1023)
   ```

También puede ver la señal en vivo con el *Serial Plotter* del IDE de Arduino.

## Notas

- `comm_2.py` usa el puerto `/dev/ttyACM0` (Linux). En Windows cámbielo por el que corresponda, por ejemplo `COM3`.
- El tiempo se calcula como `contador × 0,01` s; es aproximado, porque no incluye lo que tarda el envío por serial.
- El umbral de detección (`Threshold = 520`) puede requerir ajuste según la persona y el sensor.
