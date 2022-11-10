from bs4 import BeautifulSoup
import lxml
import csv
import requests
import time


def scrape(HOME_PAGE,headers):
    s = requests.Session()
    content = s.get(HOME_PAGE).content
    soup = BeautifulSoup(content, 'lxml')
    table_rows = soup.find_all('td',{"class": "resultdetail_reference_refdata"})
    url_list=[]
    ref_text_list=[]
    for row in table_rows:
        s=row.text.replace("\t","")
        s=s.replace("\n"," ")
        s=s.replace("\r","")
        if row.a and row.a.has_attr('href'):
            u=row.a['href']        
            url_list.append(u)
            ref_text_list.append(s)
    # print(url_list)
    # print(ref_text_list)
    return '+'.join(url_list),'+'.join(ref_text_list)
    

def main():
    HOME_PAGE = "https://bacdive.dsmz.de/strain/"
    file1 = open('demomerge.csv')
    file2 = open("demodemo.csv",'w')
    
    csvreader = csv.reader(file1)
    csvwriter = csv.writer(file2)
    header = next(csvreader)
    header = ["id","domain","phylum","class","order","family","genus","species","full_scientific_name","culture_media","culture_media_compostion","temperature",
    "kind_of_temperature","temperature_range","ph","kind_of_ph","metabolite","utilization","enzymes","isolated_from","host_species","geo_loc","country","continent","temp_def","reftext","refurl"]
    csvwriter.writerow(header)
    
    #x=0
    headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "https://google.com"}

    for row in csvreader:
        #print(row)
        
        if len(row)==0:
            continue
        urls,reftext  = scrape(HOME_PAGE+row[0],headers)
        row.append(reftext)
        row.append(urls)
        csvwriter.writerow(row)
    file1.close()
    file2.close()

if __name__ == "__main__":
    main()