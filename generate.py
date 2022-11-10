import sys
import csv
from jinja2 import Environment, FileSystemLoader
import re
from xmlgen import *

file_loader = FileSystemLoader('.') 
env = Environment(loader=file_loader)
xmlDump = open('xmldumpfinal.xml', 'w',encoding='utf-8')
xmlDump.write(hiwiki+'\n')
template = env.get_template("hindi_template.txt") 
context = {}
file1 = open('Final_hindi_db.csv',encoding='utf8')
initial_page_id = 1000000
csvreader = csv.reader(file1)
header = next(csvreader)
header = ["id","domain","phylum","class","order","family","genus","species","authority","culture_media","culture_media_composition","temperature",
    "kind_of_temperature","temperature_range","ph","kind_of_ph","metabolite","utilization","enzymes","isolated_from","host_species","geo_loc","country","continent","temp_def","reftext","refurl"]
lala=1
for row in csvreader:
    if len(row)==0 or row[0]=='':
        continue
    for i in range(len(row)):   
           
        if i==13 or (i>=19 and i<=23):
            dump=row[i].split('+')
            context[header[i]]=','.join(dump)
        elif i==10:
            parts=row[i].split('+')
            final=[]
            
            for part in parts:
                f=""
                x=part.split(' ')
                for y in x:
                    if(bool(re.match('^[a-zA-Z0-9]*$', y)) == True and y!=''):
                        f+=("<chem>"+y+"</chem> ")
                    else:
                        f+=y+" "
                f=f.replace("मध्यम", "माध्यम")
                final.append(f+" |")

            context[header[i]]=final                   


        elif '+' in row[i] or i==9 or i==11 or i==12  or i==14 or i==15 or i==16 or i==17 or i==18:
            if i==9:
                dump=row[i].replace("मध्यम", "माध्यम")
                context[header[i]]=dump.split('+')
            elif i==16:
                dump=row[16].replace('+','!')
                dump=dump.replace('(#)','(+)')
                context[header[i]]=dump.split('!')
            else:
                context[header[i]]=row[i].split('+')
        else:
            context[header[i]]=row[i]
    
    text = template.render(context)
    text = text.replace('&', "&amp;")
    text = text.replace('<', "&lt;")
    text = text.replace('>', "&gt;")
    writePage(initial_page_id, context["species"], text, xmlDump)
    initial_page_id += 1
    lala+=1
    



file1.close()   
xmlDump.write('</mediawiki>')
xmlDump.close()


# f = open("final.txt", "w",encoding='utf8')

# f.write(output)
# f.close()