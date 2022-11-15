import pandas as pd
from databases.databases import db
import ast


results = db.Results
Results=pd.DataFrame(results)

#ast.literal_eval(ejem:si hay un dic en forma de string lo paa a dic)

def str_to_datetype(data):#DE STRING A DATE sin espacios en extremos
   return pd.to_datetime(data.rstrip().lstrip(), format='%d/%m/%Y')
    
def str_to_literal(data):
    ##funcion para usar en booleanos
    ## EN ESTOS CASO ES MEJOR TAMPIEN PONER rstrip() ?????
    return ast.literal_eval(data)

def filter_pens(Data_Frame):
   #aux: UN DATAFRAME 
   aux= pd.DataFrame(columns=['stage','date','pens_home_score','pens_away_score','team_name_home','team_name_away'])
   for data in  Data_Frame.find("pens"):
      if ast.literal_eval(data):
         aux=Data_Frame.append({'stage':'stage'})
     

