import requests
import shutil
from BeautifulSoup import BeautifulSoup

def download_image(url, name):
    r = requests.get( url)
    if r.status_code == 200:
        try:
            with open("flags"+name, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)    
        except:
	    return False
    return True

countries = []
with open("listOfCountries.txt", "r+") as f:
    data = f.read()
    countries = data.strip().split("\n")


with open("temp.html", "r+") as f:
    for country in countries:
        response = requests.get("http://flagpedia.net/"+country)
	parsed_html = BeautifulSoup(response.text)
        flag_url = parsed_html.findAll('img', width="550", height="367")
	if download_image(flag_url, country):print "Downloaded " + country + " flag successfully"
	more_info = parsed_html.findAll('dl',"list clearfix")
	more_country_info = more_info[0]
	keys = more_info[0].findAll('dt')
	keys = [x.text for x in keys]
	values = more_info[0].findAll('dd')
	values = [x.text for x in values]
	dict_more_info = dict(zip(keys, values))
        print dict_more_info
	import pdb;pdb.set_trace()
