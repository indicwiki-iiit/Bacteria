import pandas as pd

#temperature,ph,reftext,refurl.
#domain
df=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/domain.csv',encoding=('utf-8'))

#phylum,class,order,genus,famliy,species
df1=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/fine1.csv',encoding=('utf-8'))

df16=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/full_scientific.csv',encoding=('utf-8'))
#culture_media
df2=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/template/merge2.csv',encoding=('utf-8'))

#culture_media_compositon
df3=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/culture_media_composition.csv',encoding=('utf-8'))
#print(df3['culture_media_compostion'])
#kind_of_temperature
df4=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/kind_of_temperature.csv',encoding=('utf-8'))

#temperature_range
df5=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/temperature_range.csv',encoding=('utf-8'))

#kind_of_ph
df6=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/kind_of_ph.csv',encoding=('utf-8'))

#metabolite
df14=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/metabolite.csv',encoding=('utf-8'))

#uutilization
df7=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/utilization.csv',encoding=('utf-8'))

#enzymes
df15=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/enzymes1.csv',encoding=('utf-8'))

#isolated_from
df8=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/isolated_from.csv',encoding=('utf-8'))

#host_species
df9=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/host_species.csv',encoding=('utf-8'))

#geo_loc
df10=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/geo_loc.csv',encoding=('utf-8'))

#country
df11=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/country.csv',encoding=('utf-8'))

#continent
df12=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/continent.csv',encoding=('utf-8'))

#temp_def
df13=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/temp_def.csv',encoding=('utf-8'))


mylis= df['id'].tolist()
mylist = df['domain'].tolist()
mylist1 = df1['phylum'].tolist()
mylist2 = df1['class'].tolist()
mylist3 = df1['order'].tolist()
mylist4 = df1['family'].tolist()
mylist5 = df1['genus'].tolist()
mylist6 = df1['species'].tolist()
mylist7 = df16['authority'].tolist()
mylist8 = df2['culture_media'].tolist()
mylist9 = df3['culture_media_compostion'].tolist()
mylist10 = df10['temperature'].tolist()
mylist11 = df4['kind_of_temperature'].tolist()
mylist12 = df5['temperature_range'].tolist()
mylist13 = df5['ph'].tolist()
mylist14 = df6['kind_of_ph'].tolist()
mylist15 = df2['metabolite'].tolist()
mylist16 = df7['utilization'].tolist()
mylist17 = df15['enzymes'].tolist()
mylist18 = df8['isolated_from'].tolist()
mylist19 = df9['host_species'].tolist()
mylist20 = df10['geo_loc'].tolist()
mylist21 = df11['country'].tolist()
mylist22 = df12['continent'].tolist()
mylist23 = df13['temp_def'].tolist()
mylist24=df10['reftext'].tolist()
mylist25= df10['refurl'].tolist()


a={'id':mylis,'domain':mylist,'phylum':mylist1,'class':mylist2,'order':mylist3,'family':mylist4,'genus':mylist5,'species':mylist6,'authority':mylist7,'culture_media':mylist8,'culture_media_compostion':mylist9,'temperature':mylist10,'kind_of_temperature':mylist11,'temperature_range':mylist12,'ph':mylist13,'kind_of_ph':mylist14,'metabolite':mylist15,'utilization':mylist16,'enzymes':mylist17,'isolated_from':mylist18,'host_species':mylist19,'geo_loc':mylist20,'country':mylist21,'continent':mylist22,'temp_def':mylist23,'reftext':mylist24,'refurl':mylist25}
df = pd.DataFrame.from_dict(a,orient='index')
df=df.transpose()
df.to_csv("ultimate.csv",encoding='utf-8',index=False)
df_saved_file=pd.read_csv('ultimate.csv')
df_saved_file