import logging
import socket
import select


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

def create_blocking(host, ip):
    logging.info('Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Blocking - connecting')
    s.connect((host, ip))

    logging.info('Blocking - connected')
    logging.info('Blocking - sending')

    s.send(b'Hello\r\n')

    logging.info('Blocking - waiting')
    data = s.recv(1024)

    logging.info(f'Blocking - data = {len(data)}')
    logging.info('Blocking - closing')
    s.close()


def create_nonblocking(host, port):
    logging.info('Non Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Non Blocking - connecting')
    result = s.connect_ex((host, port)) #Blocking

    if result != 0:
        logging.info('Non Blocking - failed to connect')
        return

    logging.info('Non Blocking - connected')
    s.setblocking(False)

    input = [s]
    output = [s]

    while input:
        logging.info('Non Blocking - waiting')
        redable, writable, exceptional = select.select(input, output, input, 0.5)

        for s in writable:
            logging.info('Non Blocking - sending')
            data = s.send(b'hello\r\n')
            logging.info(f'Non Blocking - sent: {data}')
            output.remove(s)

        for s in redable:
            logging.info('Non Blocking - reading')
            data = s.recv(1024)
            logging.info(f'Non Blocking - data: {len(data)}')
            logging.info('Non Blocking - closing')
            s.close()
            input.remove(s)
            break

        for s in exceptional:
            logging.info('Non Blocking - error')
            input.remove(s)
            output.remove(s)
            break


# create_blocking('voidrealms.com', 80)
create_nonblocking('voidrealms.com', 80)