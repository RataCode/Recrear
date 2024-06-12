import pandas as pd 
from Encryption.encriptado import encritCU
from createsDataframe import create_df
def ismPropio(df,SW,SWf1, CCH, tipoList,df_combinado,i, comercio, alta,contact,contactos):
    ftps = []
    webs = []
    if SW['code'].isin([df_combinado['code'][i]]).any():
        cchN = CCH[CCH['code'].isin([df_combinado['code'][i]])].empty
        if not pd.isna(SWf1['Web'].iloc[0]) and not pd.isna(SWf1['Servidor'].iloc[0]):
            SW[SW['code'].isin([df_combinado['code'][i]])].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
            ,"Servidor":row['Servidor']
            ,"Puerto":row['Puerto ']
            ,"User": row['Usuario']
            ,"Pass": row['Contraseña'],
            "Tipo":"TODAS"}), axis=1)

            SWf1.apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "TODAS"} ), axis=1)

            #web = {"Web":SWf1['Web'], "User": SWf1['Usuario'], "Pass":SWf1['Contraseña'],"Tipo": "TODAS"} 

        elif pd.isna(SW[SW['code'].isin([df_combinado['code'][i]])]['Servidor'].iloc[0]) and not pd.isna(CCH[CCH['code'].isin([df_combinado['code'][i]])]['Servidor']).any() and not cchN:
            SWf1.apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "SW"} ), axis=1)
            #web = {"Web":SWf1['Web'].iloc[0], "User": SWf1['Usuario'].iloc[0], "Pass":SWf1['Contraseña'].iloc[0],"Tipo": "SW"} 
            CCH[CCH['code'].isin([df_combinado['code'][i]])].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
            ,"Servidor":row['Servidor']
            ,"Puerto":row['Puerto']
            ,"User": row['Usuario']
            ,"Pass": row['Contraseña'],
            "Tipo":"SW"}), axis=1)

        elif not pd.isna(CCH[CCH['code'].isin([df_combinado['code'][i]])]["Servidor"]).any() and not cchN :

            CCH[CCH['code'].isin([df_combinado['code'][i]])].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
            ,"Servidor":row['Servidor']
            ,"Puerto":row['Puerto']
            ,"User": row['Usuario']
            ,"Pass": row['Contraseña'],
            "Tipo":"SW"}), axis=1)

        elif (pd.isna(CCH[CCH['code'].isin([df_combinado['code'][i]])]["Servidor"]).any() or cchN) and not pd.isna(SW[SW['code'].isin([df_combinado['code'][i]])]['Web'].iloc[0]) :

            SWf1.apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "SW"} ), axis=1)
        
        elif not pd.isna(SW[SW['code'].isin([df_combinado['code'][i]])]['Servidor'].iloc[0]) and pd.isna(SW[SW['code'].isin([df_combinado['code'][i]])]['Web']).any() and cchN:
            SW[SW['code'].isin([df_combinado['code'][i]])].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
            ,"Servidor":row['Servidor']
            ,"Puerto":row['Puerto ']
            ,"User": row['Usuario']
            ,"Pass": row['Contraseña'],
            "Tipo":"SW"}), axis=1)
    
    ftps, webs = encritCU(ftps, webs)
        
    return create_df(df, comercio, df_combinado, i, tipoList, alta, webs, ftps, contacto_SW(contactos, df_combinado, contact, i))
    #return create_df(df, comercio, df_combinado, i, tipoList, alta, web, ftp, contact) 



def ism_NotPropio(df,SW, CCH, tipoList,df_combinado,i, comercio, alta,contact,contactos):
    SWTPL = SW['Empresas'].isin([tipoList])
    ftps=[]
    webs=[]
    if not SW[SWTPL].empty:
        if not pd.isna(SW[SWTPL]['Web'].iloc[0]) and not pd.isna(SW[SWTPL]['Servidor'].iloc[0]):
            SW[SWTPL].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
            ,"Servidor":row['Servidor']
            ,"Puerto":row['Puerto ']
            ,"User": row['Usuario']
            ,"Pass": row['Contraseña'],
            "Tipo":"SW"}), axis=1)

            SW[SWTPL].apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "SW"} ), axis=1)
        
        #elif not pd.isna(SW[SWTPL]['Web'].iloc[0]) and pd.isna(SW[SWTPL]['Servidor'].iloc[0]):
        #    CCH[SWTPL].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
        #    ,"Servidor":row['Servidor']
        #    ,"Puerto":row['Puerto ']
        #    ,"User": row['Usuario']
        #    ,"Pass": row['Contraseña'],
        #    "Tipo":"SW"}), axis=1)
        #    SW[SWTPL].apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "CCH"} ), axis=1)


        elif pd.isna(SW[SWTPL]['Servidor'].iloc[0]) and not pd.isna(CCH[CCH['Empresas'].isin(SW[SWTPL]["Empresas"])]["Servidor"]).any():
            SW[SWTPL].apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "SW"} ), axis=1)
        
        elif  not pd.isna(CCH[CCH['Empresas'].isin(SW[SWTPL]["Empresas"])]["Servidor"]).any() and not CCH[CCH['Empresas'].isin(SW[SWTPL]["Empresas"])]["Servidor"].empty:
            CCH[CCH['Empresas'].isin(SW[SWTPL]["Empresas"])].apply(lambda row: ftps.append({"Protocolo":row['Protocolo']
            ,"Servidor":row['Servidor']
            ,"Puerto":row['Puerto']
            ,"User": row['Usuario']
            ,"Pass": row['Contraseña'],
            "Tipo":"SW"}), axis=1)
            
        elif pd.isna(CCH[CCH['Empresas'].isin(SW[SWTPL]["Empresas"])]["Servidor"]).any() and not pd.isna(SW[SWTPL]['Web'].iloc[0]):
            SW[SWTPL].apply(lambda row: webs.append({"Web":row['Web'], "User": row['Usuario'], "Pass":row['Contraseña'],"Tipo": "SW"} ), axis=1)        
    
    ftps, webs = encritCU(ftps, webs)

    return create_df(df, comercio, df_combinado, i, tipoList, alta, webs, ftps, contacto_SW(contactos, df_combinado, contact, i))


def contacto_SW(contactos, df_combinado, contact, i):
    codigo_f1 = df_combinado['code'][i]
    if contactos['code'].isin([codigo_f1]).any():
        contis = contactos[contactos['code'].isin([codigo_f1])]
        # Verificar si cada contacto ya está en la lista `contact`
        for _, row in contis.iterrows():
            nuevo_contacto = {"Nombre": row['Nombre'], "Uso": row['Uso'], "Correo": row['Correo'], "Telefono": row['Telefono']}
            if nuevo_contacto not in contact:
                contact.append(nuevo_contacto)
    return contact