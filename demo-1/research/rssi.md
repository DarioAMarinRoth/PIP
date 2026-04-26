# RSSI

En las aplicaciones de RF hay dos indicadores que se utilizan para medir el nivel de potencia de la señal que se está recibiendo: RX y RSSI.

El RX es una medida física de la fuerza de la señal recibida que se expresa en unidades estandarizadas de potencia, específicamente en mW o en dBm.

El RSSI (por sus siglas en inglés, _Received Signal Strength Indication_ o Indicador de Fuerza de Señal Recibida) también indica la fuerza con la que un receptor percibe la señal de un emisor. A diferencia del RX, el RSSI es una medición relativa y no tiene una relación estandarizada con un parámetro físico particular sino que su valor numérico suele ser definido por cada fabricante.

En el hardware Bluetooth, el RSSI a menudo se traduce y representa como un número negativo en unidades de dBm. Cuanto más negativo sea el número, más lejos estará el dispositivo.

> Como referencia, según un artículo en BeaconZone, un dispositivo muy cercano registrará valores entre -10 dBm y -30 dBm, mientras que uno en el límite de alcance mostrará valores por debajo de -90 dBm.

Dado que diferentes dispositivos usan distintos circuitos de radio, el valor absoluto del RSSI varía de un teléfono a otro. Por ejemplo, el mismo valor de RSSI en dos celulares con procesadores diferentes podría representar dos fuerzas de señal distintas.

---

**Fuentes:**

- [Distance and RSSI](https://www.bluetooth.com/blog/proximity-and-rssi/)
- [Bluetooth LE Distance Determination Using RSSI](https://www.beaconzone.co.uk/blog/bluetooth-le-distance-determination-using-rssi/)
