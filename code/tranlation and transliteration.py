from xmlrpc.client import _iso8601_format
from pyrsistent import v
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from elt import translit
import pandas as pd
from time import sleep
from random import randint
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
s=Service("C:\selenium\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()
driver.get('https://login.iiit.ac.in/cas/login?service=https%3A%2F%2Flogin.iiit.ac.in%2Fcas%2Fidp%2Fprofile%2FSAML2%2FCallback%3FentityId%3Durn%253Afederation%253AMicrosoftOnline%26SAMLRequest%3DPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c2FtbHA6QXV0aG5SZXF1ZXN0IHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiIElEPSJfZjUyOGEyMTMtNGQ4MS00Y2JmLWE1ZmQtYjMwZGM5ODM2YmU3IiBJc3N1ZUluc3RhbnQ9IjIwMjItMDctMjBUMTY6NDA6MjIuMjQ0WiIgVmVyc2lvbj0iMi4wIj48SXNzdWVyIHhtbG5zPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIj51cm46ZmVkZXJhdGlvbjpNaWNyb3NvZnRPbmxpbmU8L0lzc3Vlcj48c2FtbHA6TmFtZUlEUG9saWN5IEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6cGVyc2lzdGVudCIvPjwvc2FtbHA6QXV0aG5SZXF1ZXN0Pg%253D%253D%26RelayState%3Destsredirect%253D2%2526estsrequest%253DrQQIARAA02I21DO0UrFMTTRMTDG31E1LSTLTNUmzTNS1SEo21jVKMjdIszRLNTZJNi8S4hJwY6m_K_al3Gn1355DJgtcbq1iVMooKSkottLXLy8v10vKzEvXS87P1c8vSs9M0c9MKcnPTs3bwch4gZFxFZNKakpaUkqykZFukkWKqa5JigWQZWlmqJtkYGRqZmmSnJacmHSLid_fsbQkwwhE5BdlVqV-YuJMyy_KjS_ILy6ZxRxerVRUqmSF3dqQIEe_YB_HEP8g-5L88PJyW0O1otSUzHRbR0c3ZwNHE1NDV2MzE0dzV0dzJwNLNycTN0Njc0MjF0el2k3MbEATcvPzTjGz5Rek5mWmPGKWLUktz8zOLEg0cShKLU5NLErO0MvMzCzRS0zWy8y7wML4ioXHgNmKg4NLgEGCQYHhBwvjIlZgKCmUZXO8Pf3Jc-O3_Q_F2F0ZTrHq--kbF4e5lJakGGaYVWQ7B2YHpVa6hiU7h5UFV3nlZhlVJvn6eziGFoR7-9paWBlOYGOcwMb2gY2xg51hFycRYXyAl-EHX9erJbtenJ311gMA0')


ema=driver.find_element(By.XPATH,'//*[@id="username"]')
ema.send_keys("tewikipa4@res")
sleep(3)
ema.send_keys("earch.iiit.ac.")
sleep(3)
ema.send_keys("in")
password=driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("502d0a11")
sleep(3)
login=driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div[2]/form/input[4]')
login.click()
sleep(5)
continue1=driver.find_element(By.XPATH,'/html/body/main/div/div/section/div/form/input[3]')
continue1.click()
sleep(5)
yes=driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
yes.click()
sleep(5)

select_element = Select(driver.find_element(By.XPATH,'//*[@id="tta_tgtsl"]'))
select_element.select_by_value('hi')


df=pd.read_csv('C:/Users/Deepak Agarwal/Documents/project/template/gg/final.csv',encoding=('ISO-8859-1'))
mylist = df['domain'].tolist()
mylist1 = df['phylum'].tolist()
mylist2 = df['class'].tolist()
mylist3 = df['order'].tolist()
mylist4 = df['family'].tolist()
mylist5 = df['genus'].tolist()
mylist6 = df['species'].tolist()
mylist7 = df['full_scientific_name'].tolist()
mylist8 = df['culture_media'].tolist()
mylist9 = df['culture_media_compostion'].tolist()
mylist10 = df['temperature'].tolist()
mylist11 = df['kind_of_temperature'].tolist()
mylist12 = df['temperature_range'].tolist()
mylist13 = df['ph'].tolist()
mylist14 = df['kind_of_ph'].tolist()
mylist15 = df['metabolite'].tolist()
mylist16 = df['utilization'].tolist()
mylist17 = df['enzymes'].tolist()
mylist18 = df['isolated_from'].tolist()
mylist19 = df['host_species'].tolist()
mylist20 = df['geo_loc'].tolist()
mylist21 = df['country'].tolist()
mylist22 = df['continent'].tolist()
mylist23 = df['temp_def'].tolist()
mylist24=df['reftext'].tolist()
mylist25= df['refurl'].tolist()
domain=[]
phylum=[]
clas=[]
order=[]
family=[]
genus=[]
species=[]
full_scientific_name=[]
culture_media=[]
culture_media_compostion=[]
temperature=[]
kind_of_temperature=[]
temperature_range=[]
ph=[]
kind_of_ph=[]
metabolite=[]
utilization=[]
enzymes=[]
isolated_from=[]
host_species=[]
geo_loc=[]
country=[]
continent=[]
temp_def=[]
reftxt=[]
refurl=[]

for i in mylist11:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        kind_of_temperature.append(outPut)
    else:
        kind_of_temperature.append('nan')
for i in mylist13:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        ph.append(outPut)
    else:
        ph.append('nan')
for i in mylist14:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        kind_of_ph.append(outPut)
    else:
        kind_of_ph.append('nan')

me=[]
temp=[]
for i in range(len(mylist15)):
    metabolite=[]
    if str(mylist15[i]) =='nan':
        me.append('nan')
        continue
    else:
       temp=[]
       temp=mylist15[i].split(('+'))
       for j in range(len(temp)):
        inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
        inputBox.clear()
        inputBox.send_keys(temp[j])
        sleep(3)
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        metabolite.append(outPut)
    s=""
    for k in range(len(metabolite)):
        if k==len(metabolite)-1:
            s=s+metabolite[k]
        else:
            s=s+metabolite[k]+"+"
    me.append(s)
my=[]
temp=[]
for i in range(len(mylist16)):
    utilization=[]
    if str(mylist16[i]) =='nan':
        my.append('nan')
        continue
    else:
       temp=[]
       temp=mylist16[i].split(('+'))
       for j in range(len(temp)):
        inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
        inputBox.clear()
        inputBox.send_keys(temp[j])
        sleep(3)
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        utilization.append(outPut)
    s=""
    for k in range(len(utilization)):
        if k==len(utilization)-1:
            s=s+utilization[k]
        else:
            s=s+utilization[k]+"+"
    my.append(s)
for i in mylist17:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(5)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        enzymes.append(outPut)
    else:
        enzymes.append('nan')
for i in mylist18:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(4)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        isolated_from.append(outPut)
    else:
        isolated_from.append('nan')
for i in mylist19:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        host_species.append(outPut)
    else:
        host_species.append('nan')
for i in mylist20:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        geo_loc.append(outPut)
    else:
        geo_loc.append('nan')
for i in mylist21:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        country.append(outPut)
    else:
        country.append('nan')
for i in mylist22:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        continent.append(outPut)
    else:
        continent.append('nan')
for i in mylist23:
    inputBox = driver.find_element(By.XPATH,'//*[@id="tta_input_ta"]')
    inputBox.clear()
    inputBox.send_keys(i)
    sleep(3)
    if str(i) != 'nan':
        outPut =  driver.execute_script("return document.getElementById('tta_output_ta').value;")
        temp_def.append(outPut)
    else:
        temp_def.append('nan')
driver.close()
to_hindi = translit('hindi')

domain=to_hindi.convert(mylist)
phylum=to_hindi.convert(mylist1)
clas=to_hindi.convert(mylist2)
order=to_hindi.convert(mylist3)
family=to_hindi.convert(mylist4)
genus=to_hindi.convert(mylist5)
species=to_hindi.convert(mylist6)
culture_media=to_hindi.convert(mylist8)

temperature_range=to_hindi.convert(mylist12)
a={'domain':domain,'phylum':phylum,'class':clas,'order':order,'family':family,'genus':genus,'species':species,'full_scientific_name':mylist7,'culture_media':culture_media,'culture_media_compostion':mylist9,'temperature':mylist10,'kind_of_temperature':kind_of_temperature,'temperature_range':temperature_range,'ph':ph,'kind_of_ph':kind_of_ph,'metabolite':me,'utilization':my,'enzymes':enzymes,'isolated_from':isolated_from,'host_species':host_species,'geo_loc':geo_loc,'country':country,'continent':continent,'temp_def':temp_def,'reftet':mylist24,'refurl':mylist25}
df = pd.DataFrame.from_dict(a,orient='index')
df=df.transpose()
df.to_csv("demo.csv",index=False)

df_saved_file=pd.read_csv('demo.csv')

df_saved_file


