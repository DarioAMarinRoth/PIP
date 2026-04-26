
# BLE

## BLE GAP: Topologías y roles

El protocolo BLE soporta dos diferentes formas de comunicación: broadcast y connection-oriented. 

**Connection-oriented communication:** cuando existe una conexión dedicada entre dispositivos de forma tal que hay comunicación bidireccional.
**Broadcast communication:** Cuando los dispositivos se comunican sin establecer una conexión, sino mediante la emisión de paquetes de datos que pueden recibir dispositivos dentro de un cierto rango.
### Roles

La capa GAP (General Access Profile) define roles específicos para los nodos en una red BLE. Estos roles determinan aspectos importantes sobre como los dispositivos notifican de su presencia, o como escanean y se conectan a otros nodos.

Advertising y Scanning se refieren a los procesos mediante los cuales los dispositivos BLE se vuelven consientes de la presencia de otros y de las posibilidades de conexión. En específico:

- **Advertising:** el proceso de transmitir paquetes de advertising, ya sea para broadcast o para ser descubierto por otro dispositivo.
- **Scanning:** el proceso de escuchar para recibir paquetes de advertising.

#### Central, peripheral, broadcaster y observer

Hay cuatro roles que pueden adoptar los dispositivos BLE de una red:

- **Central:** Un dispositivo que escanea y inicia conexiones con dispositivos *peripheral*.
- **Peripheral:** Un dispositivo que envía paquetes de advertising y acepta conexiones de dispositivos *central*.
- **Broadcaster:** un tipo especial de *peripheral* que emite paquetes de advertising sin aceptar ninguna solicitud de conexión.
- **Observer:** un tipo especial de *central* que escucha paquetes de advertising sin iniciar ninguna conexión.

> Estos dos últimos roles son los que usaríamos para las balizas utilizando la topología _Broadcast_.

### Topología Broadcast

En la topología broadcast, la transferencia de información ocurre sin que los dispositivos establezcan ningún tipo de conexión. Esto se logra utilizando paquetes de advertising para emitir información a cualquier dispositivo que se encuentre en rango de recibir paquetes. Un dispositivo peripheral, mas específicamente, un broadcaster, publica la información, y un central, más específicamente un observador va a escanear y leer la información desde los paquetes de advertising.

La ventaja de esta topología es que no hay límites en la cantidad de dispositivos a los que se puede transmitir. Cualquier dispositivo en rango de los paquetes puede recibir la información.

## BLE Advertising

El estándar BLE tiene dos formas de comunicarse. La primera es utilizando _advertisements_, donde un dispositivo periférico BLE transmite paquetes a cualquier otro dispositivo en el entorno (lo que necesitamos para la baliza). El receptor, en este caso, puede actuar en base a estos paquetes o establecer una conexión para recibir más información.

La otra forma sería establecer directamente una conexión. De esta manera, ambos periféricos pueden enviar y recibir paquetes.

### Proceso de Advertising

Cuando un dispositivo BLE está en un estado de advertising, envía paquetes de advertising para notificar su presencia y potencialmente conectarse a otro dispositivo. Estos paquetes de advertising se envían periódicamente en _intervalos de advertising_.

>[!Note]
>Los intervalos de advertising están en un rango de entre 20 ms a 10.24 seg, con un paso de 0.625 ms.
>

Mientras menor sea el intervalo de advertising, más frecuentemente se envían los paquetes y por lo tanto mayor es el consumo de la baliza.

Como nosotros tenemos más de una baliza, si ambas están configuradas con el mismo intervalo es posible que exista una colisión entre los paquetes de dos o más balizas. Para evitar esto, se añade un delay aleatorio de entre 0 y 10 ms antes de enviar cada paquete de advertising.

Del mismo modo que existe el intervalo de advertising existe el intervalo de scan. Esto hace referencia a que tan frecuentemente un dispositivo scanner va a escanear para recibir paquetes de advertising. Otro concepto parecido es la ventana de scan que es en esencia el duty cycle del intervalo de scan.

La relación de compromiso entre el intervalo de scan y el consumo del dispositivo es completamente análoga a la de la baliza.

#### Canales de Advertisement

Los dispositivos BLE se comunican a través de 40 canales de frecuencia diferentes. De estos 40 canales hay tres (el 37, 38 y 39) que se usan principalmente para advertisement y los otros 37 se suelen usar para transferir información y establecer conexiones. Aún así, es posible usar estos canales para para hacer advertisement.

Los paquetes se envían por los tres canales principales para asegurar cierto nivel de redundancia. Del mismo modo, los dispositivos receptores escanean los tres canales para encontrar dispositivos de advertising. Esto se hace conmutando entre los diferentes canales luego de cada intervalo de scan.

![scan interval and window](https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1024,h_576/https://academy.nordicsemi.com/wp-content/uploads/2022/12/blefund_less2_adv_process-1024x576.png)

> Dato de color: si bien los canales principales de advertising están numerados consecutivamente, no son canales vecinos. La separación que hay entre los canales es para evitar interferencia por el solapamiento de las bandas de cada canal. También están elegidos para minimizar el ruido generado por otras tecnologías: WiFi.

---
**Fuentes consultadas:**

- [GAP: Devices roles and topologies](https://academy.nordicsemi.com/courses/bluetooth-low-energy-fundamentals/lessons/lesson-1-bluetooth-low-energy-introduction/topic/gap-device-roles-and-topologies/)
- [Advertising process](https://academy.nordicsemi.com/courses/bluetooth-low-energy-fundamentals/lessons/lesson-2-bluetooth-le-advertising/topic/advertising-process/)
