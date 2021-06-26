import socket
so=socket.socket(socket.SOCK_DGRAM)
so.bind(("0.0.0.0",8806))
so.listen()
so.accept()
so.close()

s="0.0.0.0"
test_str=".".join(s.split("."))
print(type(test_str))
