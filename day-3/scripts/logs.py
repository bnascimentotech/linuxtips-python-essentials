#!/usr/bin/env python3
"""
"""

__version__ = "0.1.0" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import os
import logging # root logger
from logging import handlers

# TODO: usar função para configurações de log
# TODO: usar lib externa (Exemplo: loguru)

# BOILERPLATE
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Nossa instância
log = logging.Logger("logs.py", log_level)

# Level
# ch = logging.StreamHandler() # Console/Terminal/stderr
# ch.setLevel(log_level)

fh = handlers.RotatingFileHandler(
    "meuLog.log", 
    maxBytes=300, # Recomendado: 10**6
    backupCount=10
) # Arquivo
fh.setLevel(log_level)

# Formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# Destino
# log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem pro Dev, QA, SysAdmin.")
log.info("Mensagem geral para usuários.")
log.warning("Aviso que não causa erro.")
log.error("Erro que afeta uma única execução.")
log.critical("Erro geral. Exemplo: o banco de dados sumiu!")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro: %s.", str(e))
    # print(f"[ERROR] Deu erro: {str(e)}")
