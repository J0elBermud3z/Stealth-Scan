from scapy.all import *

# Definir una función llamada escanear_puerto que toma una dirección IP y un número de puerto como argumentos.
def escanear_puerto(ip, puerto):
    # Generar un número de puerto fuente aleatorio para el escaneo sigiloso.
    srcport = RandShort()

    # Crear un paquete TCP SYN (Stealth scan) utilizando la librería Scapy.
    paquete = IP(dst=ip) / TCP(sport=srcport, dport=puerto, flags="S")

    # Enviar el paquete y esperar una respuesta, con un tiempo de espera de 1 segundo y sin imprimir mensajes de verbose.
    respuesta = sr1(paquete, timeout=1, verbose=0)
    
    # Analizar la respuesta recibida.
    if respuesta and respuesta.haslayer(TCP):
        # Verificar si el paquete recibido es un TCP SYN/ACK (indicativo de puerto abierto).
        if respuesta.getlayer(TCP).flags == 0x12:
            print(f"El puerto {puerto} está abierto!")
    else:
        print(f"El puerto {puerto} está cerrado!")

# Llamar a la función escanear_puerto con la dirección IP "192.168.1.1" y el número de puerto 443.
escanear_puerto("192.168.1.1", 443)