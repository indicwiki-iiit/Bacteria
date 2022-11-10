import csv

def val(n):
    x=n
    if n=='Jan':
        x=1
    elif n=='Feb':
        x=2
    elif n=='Mar':
        x=3
    elif n=='Apr':
        x=4
    elif n=='May':
        x=5
    elif n=='Jun':
        x=6
    elif n=='Jul':
        x=7
    elif n=='Aug':
        x=8
    elif n=='Sep':
        x=9
    elif n=='Oct':
        x=10
    elif n=='Nov':
        x=11
    elif n=='Dec':
        x=12

    return str(x)
        


def main():
    file1 = open('Scraped_db.csv',encoding="utf8")
    file2 = open("demomerge.csv",'w')
    csvreader = csv.reader(file1)
    csvwriter = csv.writer(file2)
    header = []
    header = next(csvreader)
    header = ["id","domain","phylum","class","order","family","genus","species","full_scientific_name","culture_media","culture_media_compostion","temperature",
    "kind_of_temperature","temperature_range","ph","kind_of_ph","metabolite","utilization","enzymes","isolated_from","host_species","geo_loc","country","continent","temp_def"]
    csvwriter.writerow(header)
    #print(header)
    samerow=[]
    entry=[]
    currow = next(csvreader)
    samerow.append(currow)

    for row in csvreader:
        
        #print(row[0])
        if row[0]=='':
            continue
        if currow[0]==row[0]:
            samerow.append(row)
        else:
            m=len(samerow)      #no. of rows
            n=len(samerow[0])   #no. of cols/attr
            for j in range(n):
                if j==12 or j==17 or j==15:
                    continue
                attr=[]
                for i in range(m):
                    if j==11:
                        if samerow[i][11]!='' and samerow[i][12]!='':
                            dummy=samerow[i][11]
                            dummy=dummy.split('-')
                            string=samerow[i][11]
                            if len(dummy)>1:
                                #print(dummy)
                                string=" "+val(dummy[0])+" - "+ val(dummy[1])+ " "

                            if list((string,samerow[i][12])) not in attr :                        

                                attr.append(list((string,samerow[i][12])))

                    elif j==14:
                        if samerow[i][j]!='' and  samerow[i][15]!='':
                            dummy=samerow[i][14]
                            dummy=dummy.split('-')
                            string=samerow[i][14]
                            if len(dummy)>1:              
                                string=" "+val(dummy[0])+" - "+ val(dummy[1])+ " "
                            if list((string,samerow[i][15])) not in attr:                        

                                attr.append(list((string,samerow[i][15])))

                    elif j==16:
                        if samerow[i][j]!='' and samerow[i][17]!='':
                            if list((samerow[i][16],samerow[i][17])) not in attr:
                                attr.append(list((samerow[i][16],samerow[i][17])))
                        

                    elif samerow[i][j] not in attr and samerow[i][j]!='':
                        attr.append(samerow[i][j])

                if j==11 or j==14 or j==16:
                    x=""
                    y=""
                    
                    for l in attr:
                        x+=str(l[0])+"+"
                        y+=str(l[1])+"+"
                    x=x[:-1]
                    y=y[:-1]
                    entry.append(x)
                    entry.append(y)
                    
                else:
                    entry.append('+'.join(attr))

            defi=" "
            for c in entry[13].split('+'):
                if c=="mesophilic":
                    defi+="Mesophiles are microorganisms with an optimum temperature near 37°C . Mesophiles can grow in the temperature range of 25-40°C.+"
                elif c=="thermophilic":
                    defi+="Thermophiles are “heat-loving” organisms having optimum growth between 50-60°C. Many thermophiles cannot grow below 45°C.+"
                elif c=="psychrophilic":
                    defi+="Psychrophiles are “Cold-loving” organisms, they can even grow at 0°C. They are sensitive to temperatures over 20°C. Optimum growth occurs at 15°C or below. +"
                elif c=="hyperthermophilic":
                    defi+="Hyperthermophiles have optimum growth at 80°C or higher. The permissive growth temperature for hyperthermophiles ranges from 80°C to a maximum of 110°C, with some extreme examples that survive temperatures above 121°C.+"
                #print(entry)
            entry.append(defi[:-1])
            if entry[8]=='':
                entry[8]=entry[7]
            csvwriter.writerow(entry)
            entry=[]
            if row[0]=='End':
                break
            currow=row
            samerow=[]
            samerow.append(currow)

    file1.close()
    file2.close()


if __name__ == "__main__":
    main()