# **Stealth Scan usando Python3**
**Advertencia:** El uso de técnicas de escaneo, especialmente de forma no autorizada, es ilegal y viola la privacidad y seguridad de sistemas y redes.
El conocimiento de estas técnicas debe utilizarse con responsabilidad y ética, por ejemplo, en el contexto de pruebas de penetración autorizadas.

# **Descripción**
El "Stealth Scan" es una técnica de escaneo de puertos empleada por hackers y administradores de sistemas para obtener información sobre los servicios en ejecución en una red sin ser detectados fácilmente por los sistemas de seguridad. Su objetivo principal es evitar ser registrado en los logs del sistema como un escaneo malicioso y lograr evadir firewalls.

La práctica común de escaneo de puertos implica el uso del escaneo SYN, donde se envía un paquete TCP con la bandera SYN activada al puerto de destino. Si se recibe un paquete de respuesta SYN/ACK, indica que el puerto está abierto, y si se recibe un paquete de RST/ACK, el puerto está cerrado.

El Stealth Scan utiliza técnicas más sutiles, como el "3-way handshake" (apretón de manos de tres vías):

Envío del paquete SYN: El atacante envía un paquete TCP con la bandera SYN activada al puerto de destino.

Recepción del paquete SYN/ACK: Si el puerto está abierto, la máquina objetivo responde con un paquete SYN/ACK, indicando su disposición para establecer una conexión.

Envío del paquete RST: En lugar de completar el "3-way handshake" enviando un ACK para establecer la conexión, el atacante envía un paquete RST (Reset) para interrumpir la conexión. Esto rompe el intento de conexión y evita que el sistema objetivo registre el escaneo como una conexión exitosa.

Este método permite al atacante obtener información sobre la existencia de servicios sin completar la conexión, evitando así ser detectado fácilmente. Sin embargo, algunos sistemas de seguridad pueden detectar patrones de tráfico sospechoso y tomar medidas preventivas.

# **Implementación**
![Script Python3](https://i.ibb.co/JQwZkRK/script.png)

En el script compartido, se proporciona una implementación simple con fines puramente educativos. Se recomienda su uso solo en entornos controlados y con la debida autorización.

# **Verificación con WireShark**
![WireShark](https://i.ibb.co/6gcrXrf/tcp.png)
Adicionalmente, para entender mejor el proceso, podemos utilizar la herramienta WireShark. Filtrando por la IP y puerto utilizados para el escaneo, podemos observar cómo se envía primero un paquete SYN, seguido de un SYN/ACK, y finalmente un paquete RST.

