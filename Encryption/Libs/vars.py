from Encryption.Libs.lib import *
#####   MONGODB CONNECTIONS ####
# --- Clients ---
client = connect_db('base de datos')
client_local = connect_db('')
# PARA GENERAR RANDOM KEYS 
# Random_key = get_random_bytes(16) # UNA VEZ SE GENERA UN KEY GUARDARLA PARA EL DESENCRIPTADO
key = client.gdc.JSONtables.find_one({'Documento': 'documento'})['values']