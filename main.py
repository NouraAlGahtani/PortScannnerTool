import socket



target =  input("Enter the Target IP Adresss")
min_port = int(input("enter the minimum port number you want to scan:"))
max_port = int(input("enter the maximum port number you want to scan"))

print("Scanning target", target, "From port", min_port, "to port", max_port)


for port in range (min_port, max_port + 1) :
    s = socket.socket(socket.AF_INET)
