import pandas as pd

def create_df(df, comercio, df_combinado,i,tipoList,alta,webs,ftps,contact):
    if (not all(valor == "" for valor in webs[0].values()) or not all(valor == "" for valor in ftps[0].values())):
        df = pd.concat([df,pd.DataFrame({
        "datos_privados": comercio.replace(" ", "")
        ,"datos_privados": df_combinado["datos"].iloc[i]
        ,"datos_privados": df_combinado["datos"].iloc[i]
        ,"datos_privados": df_combinado["datos"].iloc[i]
        ,"datos_privados": df_combinado["datos"].iloc[i]
        ,"datos_privados": tipoList
        ,"datos_privados": alta
        ,"datos_privados": str(df_combinado["datos"].iloc[i]).replace(",","").replace("nan","No disponible")
        ,"datos_privados":[[{k: "" if pd.isna(v) else v for k, v in d.items()} for d in webs]]
        ,"datos_privados":[[{k: "" if pd.isna(v) else v for k, v in d.items()} for d in ftps]]
        ,"datos_privados":  [[{k: "" if pd.isna(v) else v for k, v in d.items()} for d in contact]]
        ,"datos_privados": ""
        }, index=[1])], ignore_index=True) 
    return df