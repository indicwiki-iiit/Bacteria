import csv

def main():
    file1 = open('reflist.csv',encoding="utf8")
    csvreader = csv.reader(file1)
    header = next(csvreader)
    ref={}
    for row in csvreader:
        if row[0] in ref.keys():
            pass
        else:
            ref[row[0]]=list((str(row[2]+row[3]+row[4]+row[5]),row[1]))
    
    file1.close()

    file1 = open('Final_eng_db.csv')
    csvreader = csv.reader(file1)
    header = next(csvreader)
    idlist=[]
    for row in csvreader:
        #print(row)        
        if len(row)==0 or row[0]=='':
            continue
        idlist.append(row[0])
    file1.close()
    print(len(idlist))
    file1 = open('ids.csv',encoding="utf8")
    csvreader = csv.reader(file1)
    header = next(csvreader)
    print(header)
    ids={}
    l=[]
    id=0
    for row in csvreader:
        
        if id==0:
            if row[0] in idlist:
                id=row[0]
                l.append(row[5])
        elif row[0]=='':
            if id!=0:
                l.append(row[5])
        else:
            ids[id]=l
            if row[0] in idlist:
                id=row[0]
                l=[]
                l.append(row[5])
            else:
                id=0
                l=[]
    if id!=0:
        ids[id]=l

    file1.close()
    file1 = open('Final_eng_db.csv')
    csvreader = csv.reader(file1)
    header = next(csvreader)
    file2 = open("Final_hindi_db.csv",'w')
    csvwriter = csv.writer(file2)   
    header = ["id","domain","phylum","class","order","family","genus","species","full_scientific_name","culture_media","culture_media_compostion","temperature",
    "kind_of_temperature","temperature_range","ph","kind_of_ph","metabolite","utilization","enzymes","isolated_from","host_species","geo_loc","country","continent","temp_def","reftext","refurl"]
    csvwriter.writerow(header)  

    for row in csvreader:

        if len(row)==0 or row[0]=='':
            continue
        txt=""
        url=""
        if row[0] in ids.keys():
            for nos in ids[row[0]]:
                if nos in ref.keys():
                    txt+=ref[nos][0]+"+"
                    url+=ref[nos][1]+"+"
            txt=txt[:-1]
            url=url[:-1]
            row.append(txt)
            row.append(url)
        csvwriter.writerow(row)

    file2.close()
    file1.close()
        

        

        


if __name__ == "__main__":
    main()