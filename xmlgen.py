import string
from hashlib import sha1
from datetime import datetime

hiwiki = '''<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.11/ http://www.mediawiki.org/xml/export-0.11.xsd" version="0.11" xml:lang="hi">
  <siteinfo>
    <sitename>Hindiwiki</sitename>
    <dbname>hiwikidb</dbname>
    <base>https://hiwiki.iiit.ac.in/index.php/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0</base>
    <generator>MediaWiki 1.37.2</generator>
    <case>first-letter</case>
    <namespaces>
      <namespace key="-2" case="first-letter">मीडिया</namespace>
      <namespace key="-1" case="first-letter">विशेष</namespace>
      <namespace key="0" case="first-letter" />
      <namespace key="1" case="first-letter">वार्ता</namespace>
      <namespace key="2" case="first-letter">सदस्य</namespace>
      <namespace key="3" case="first-letter">सदस्य वार्ता</namespace>
      <namespace key="4" case="first-letter">Hindiwiki</namespace>
      <namespace key="5" case="first-letter">Hindiwiki वार्ता</namespace>
      <namespace key="6" case="first-letter">चित्र</namespace>
      <namespace key="7" case="first-letter">चित्र वार्ता</namespace>
      <namespace key="8" case="first-letter">मीडियाविकि</namespace>
      <namespace key="9" case="first-letter">मीडियाविकि वार्ता</namespace>
      <namespace key="10" case="first-letter">साँचा</namespace>
      <namespace key="11" case="first-letter">साँचा वार्ता</namespace>
      <namespace key="12" case="first-letter">सहायता</namespace>
      <namespace key="13" case="first-letter">सहायता वार्ता</namespace>
      <namespace key="14" case="first-letter">श्रेणी</namespace>
      <namespace key="15" case="first-letter">श्रेणी वार्ता</namespace>
      <namespace key="710" case="first-letter">TimedText</namespace>
      <namespace key="711" case="first-letter">TimedText talk</namespace>
      <namespace key="828" case="first-letter">Module</namespace>
      <namespace key="829" case="first-letter">Module talk</namespace>
      <namespace key="2300" case="first-letter">Gadget</namespace>
      <namespace key="2301" case="first-letter">Gadget talk</namespace>
      <namespace key="2302" case="case-sensitive">Gadget definition</namespace>
      <namespace key="2303" case="case-sensitive">Gadget definition talk</namespace>
    </namespaces>
  </siteinfo>'''

username = "Darshana baruah"
user_id = "16"

def sha36(page_id):
    page_id = str(page_id).encode('utf-8')
    sha16 = sha1(page_id).hexdigest()
    sha10 = int(sha16, 16)

    chars = []
    alphabets = string.digits + string.ascii_lowercase
    while sha10 > 0:
        sha10, r = divmod(sha10, 36)
        chars.append(alphabets[r])

    return ''.join(reversed(chars))

# Function to replace possible Entity references


def clean(text):
    text = text.replace('&', "&amp;")
    text = text.replace('<', "&lt;")
    text = text.replace('>', "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&apos;")

    return text

def writePage(page_id, title, wikiText, fobj):
    global user_id, username

    pglen = len(wikiText)
    time = datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")

    curPage = '''\n\n
	<page>
		<title>''' + clean(title) + '''</title>
		<ns>0</ns>
		<id>''' + str(page_id) + '''</id>
		<revision>
			<id>''' + str(page_id) + '''</id>
			<!-- <timestamp>'''+time+'''</timestamp> -->
			<contributor>
				<username>''' + username + '''</username>
				<id>''' + str(user_id) + '''</id>
			</contributor>
			<comment>xmlpage created</comment>
			<model>wikitext</model>
			<format>text/x-wiki</format>
			<text xml:space="preserve" bytes="''' + str(pglen) + '''">
			\n''' + wikiText + '''
			</text>
			<sha1>''' + sha36(page_id) + '''</sha1>
		</revision>
	</page>
	\n\n'''

    fobj.write(curPage)
    return