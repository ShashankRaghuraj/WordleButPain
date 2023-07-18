import socket

host = ''
port = 21567

storedValue = "Yo, what's up"

def setup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print (msg)
    return s

def setupConnection():
    s.listen(1)
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn
    
def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        dataMessage = data.split(' ',1)
        command = dataMessage[0]
        
        if command == 'EXIT':
            s.close()
            break

        conn.sendall(str.encode())
        print("Data has been sent!")
    conn.close()
s = setup()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break

