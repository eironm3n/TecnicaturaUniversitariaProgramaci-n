
import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',  #datefmt es el formato de la fecha
                handlers=[log.FileHandler('capa_datos.log'),log.StreamHandler()])

# Llamamos una configuracion basica
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel Warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')

"""
La terminal arrojaria =
DEBUG:root:Mensaje a nivel debug
INFO:root:Mensaje a nivel info
WARNING:root:Mensaje a nivel Warning
ERROR:root:Mensaje a nivel error
CRITICAL:root:Mensaje a nivel critical
"""