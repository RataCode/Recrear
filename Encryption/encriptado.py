from Encryption.encrypt_decrypt import aes_gcm_encrypt
from Encryption.Libs.vars import *
import pandas as pd
import numpy as np

def encritCU(ftps, webs):
    # Aplicar la transformación a cada diccionario dentro del array ftps
    if bool(ftps):
        for ftp in ftps:
            if str(ftp["User"]) != "nan":
                ftp["User"] = aes_gcm_encrypt(str(ftp["User"]), key)
            else:
                ftp["User"] = "No disponible"

            if str(ftp["Pass"]) != "nan":
                ftp["Pass"] = aes_gcm_encrypt(str(ftp["Pass"]), key)
            else:
                ftp["Pass"] = "No disponible"
    else:
        ftps = [{"Protocolo": "", "Servidor": "", "Puerto": "", "User": "", "Pass": "", "Tipo": ""}]
    # Aplicar la transformación a cada diccionario dentro del array webs
    if bool(webs):
        for web in webs:
            if str(web["User"]) != "nan":
                web["User"] = aes_gcm_encrypt(str(web["User"]), key)
            else:
                web["User"] = "No disponible"
            
            if str(web["Pass"]) != "nan":
                web["Pass"] = aes_gcm_encrypt(str(web["Pass"]), key)
            else:
                web["Pass"] = "No disponible"
    else:
        webs = [{"Web": "", "User": "", "Pass": "", "Tipo": ""}]
    # Devolver los arrays transformados
    return ftps, webs




