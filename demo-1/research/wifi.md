# Operación del WiFi en la ESP32

La placa opera en la banda de 2.4 GHz exclusivamente y su funcionamiento se divide en tres modos: STA, AP y dual. El dual no es relevante para el proyecto.

## Modo STA (Station)

En este modo, la ESP32 se comporta como un cliente tradicional. Escanea las redes disponibles, se autentica con una contraseña y se conecta a una red Wi-Fi existente para obtener una dirección IP y acceso a Internet o a la red local.

> [!Note]
> Es el modo en el que operaría el dispositivo receptor en el pip

## Modo AP (Access Point)

La placa crea su propia red Wi-Fi. Otros dispositivos pueden buscar esta red y conectarse directamente a la placa, sin necesidad de infraestructura externa. 

> [!Warning]
> La placa comparte la misma antena y radio de 2.4 GHz tanto para el Wi-Fi como para el Bluetooth. La ESP32 divide y alterna el tiempo de uso entre ambas tecnologías. Supuestamente para usos "normales" el uso simultaneo anda bien.

---
Fuentes:

- https://pcbsync.com/esp32-wifi/