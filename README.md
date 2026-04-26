# PIP Marin/Ramirez

- [ ] TODO: Escribir el readme

---

## Instalar y utilizar MicroPython

### Flashear el Firmware

#### 1. Instalar Python y PIP

```bash
sudo pacman -S python python-pip
```

#### 2. Instalar las CLI tools

```bash
pip install esptool mpremote
```

Dar acceso al puerto serial

```bash
sudo usermod -aG uucp $USER
```

#### 3. Instalar MicroPython

Descargar la última versión de MicroPython disponible para la placa ([ESP32-C3](https://micropython.org/download/ESP32_GENERIC_C3/)).

#### 4. Flashear MicroPython

1. Conectar la placa.
2. Identificar el puerto:

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM*
    ```

    > [!Tip]
    > Si no se encuentra la placa, reiniciar la computadora.
3. Borrar el flash:

    ```bash
    esptool.py --chip esp32c3 --port /dev/<PUERTO_IDENTIFICADO> erase_flash
    ```

4. Flashear el firmware

    ```bash
    esptool.py --chip esp32c3 --port /dev/<PUERTO_IDENTIFICADO> \
    --baud 460800 write_flash -z 0x0 <RUTA_A_ESP32_GENERIC_C3-*.bin>
    ```

5. Verificar con RPLE

    ```bash
    mpremote connect /dev/<PUERTO_IDENTIFICADO>
    ```

    En caso de funcionar correctamente debería verse el prompt `>>>`. Ctrl + x para salir.

### Subir scripts a la placa

Para subir un archivo a la placa se hace uso del comando:

```bash
mpremote connect /dev/<PUERTO_IDENTIFICADO> cp <archivo_local> :<archivo_en_placa>
```

Además, es recomendable hacer un reset

```bash
mpremote connect /dev/<PUERTO_IDENTIFICADO> reset
```

#### A tener en cuenta

Según la documentación, hay dos archivos que la placa trata de manera especial al arrancar: boot.py y main.py. El script boot.py se ejecuta primero (si existe) y, una vez que finaliza, se ejecuta el script main.py. \
Se pueden cargar archivos con nombres distintos pero no se ejecutarán automáticamente al alimentar la placa. Esto se puede hacer tanto desde RPLE:

```bash
import mi_archivo
```

O con mpremote:

```bash
mpremote connect /dev/<PUERTO_IDENTIFICADO> run mi_archivo.py
```
