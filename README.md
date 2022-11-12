# Bacteria

This repository contains all the work that was done as a part of enriching Hindi wikipedia. The aim is to deploy a large number of articles for different Bacteria in Hindi.

## Stages of the project

The following ordered list will give an idea as to what stage the project currently is in:

- [x] Scrape Data from Web sources
- [x] Clean and Format the data
- [x] Scrape infobox information from Wikipedia
- [x] Create a sample article
- [x] Review of the sample article
- [x] Work on feedback from review of sample article
- [x] Review of the dataset
- [x] Create template for article generation
- [x] Review of the template
- [x] Work on feedback from review of template
- [x] Create the XML dump for all the diseases to be published

## Folders

- `Database`: Contains all the dataset (csv) files that have been used for this project.
- `Code`: Contains all the code that has been used in the project.

### Database

This folder contains the final dataset as well as some other dataset that have been used in the project:

- [Scraped_db.csv](https://github.com/indicwiki-iiit/Bacteria/blob/main/Database/Scraped_db.csv): This is the dataset that has been directly scraped from [BacDive](https://bacdive.dsmz.de/taxplorer).
- [Scraped_db_added_attrib.csv](https://github.com/indicwiki-iiit/Bacteria/blob/main/Database/Scraped_db_added_attrib.csv): This file contains the English dataset that is used for article generation after merging multivalued attributes and adding some addtional data. The file contains data on 17245 bacteria and has 24 attributes.
- [reflist.csv](https://github.com/indicwiki-iiit/Bacteria/blob/main/Database/reflist.csv): This csv file contains a list of all the references from which we took out the data.
- [Fina_eng_db](https://github.com/indicwiki-iiit/Bacteria/blob/main/Database/Final_eng_db.csv) : This csv file is the final English database with the refernces added for each bacteria.
- [Fina_hindi_db](https://github.com/indicwiki-iiit/Bacteria/blob/main/Database/Final_hindi_db.csv) : This csv file is the final Hindi database after translating and transliterating the final English database.



### Code

This folder contains various files:

- [manual_ref](https://github.com/indicwiki-iiit/Bacteria/blob/main/Code/manual_ref.py): Contains code which combines the multiple refernces of each article alongwith the url and text.
- [merge](https://github.com/indicwiki-iiit/Bacteria/blob/main/Code/merge.py): Contains code which merges all the multi-valued attributes with a proper delimiter such that it can be separated out when required. Also does some conversions and addition of attributes.
- [ref_scrape](https://github.com/indicwiki-iiit/Bacteria/blob/main/Code/ref_scrape.py): Contains the code used for extraction of references.
- [transaltion and transliteration](https://github.com/indicwiki-iiit/Bacteria/blob/main/Code/tranlation%20and%20transliteration.py): Includes the code for translating and transliterating the main dataset.

### Generating articles

- [hindi_template](https://github.com/indicwiki-iiit/Bacteria/blob/main/hindi_template.txt): It contains the template for the structure of the article.
- [xmlgen](https://github.com/indicwiki-iiit/Bacteria/blob/main/xmlgen.py): It contains the backbone structure for conversion to XML.
- [generation](https://github.com/indicwiki-iiit/Bacteria/blob/main/generate.py): it contains the code for generating XML dump of articles using the template and the dataset
- [xmldump50](https://github.com/indicwiki-iiit/Bacteria/blob/main/xmldump50.xml): the XML dump file of intial 50 articles bacteria.


## Contributors
Darshana Baruah darshanabaruah185@gmail.com
<br>
Vineet Agarwal vineetagarwal540@gmail.com

