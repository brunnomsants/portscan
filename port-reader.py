import socket
import sys


host = input("Host: \n")
load = "[------------------]"
backtrack = '\b' * len(load)

i = int(65535/20)
    
open_ports = []
print(load)
for port in range(0, 65535):
    
    if(port%i == 0 and port!=0):
        sys.stdout.write(backtrack + load)
        sys.stdout.flush()
        load = load.replace("-", "=", 1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    if(s.connect_ex((host, port)) == 0 ):
        open_ports.append(port)
        
    s.close()
    
    sys.stdout.write(backtrack)
print("\n\n")
print(f"Open ports:\n")
print(f"HOST    |   PORT")
for ports in open_ports:
    print(f"{host}  :   {port}")