import urllib, re
from BeautifulSoup import BeautifulSoup

COMMITTEES = "Committees"
ADDRESS = "Address"
ADDRESS2 = "Address2"
CITY = "City"
ZIP = "Zip"
PHONE1 = "Phone1"
PHONE2 = "Phone2"
FAX = "Fax"

phone_re = re.compile(r"(\(\d{3}\) \d{3}-\d{4})")
address_re = re.compile(r"(City Hall.+)(Philadelphia, PA) ([0-9]{5}-[0-9]{4})")
# define the order our columns are displayed in the datastore
#scraperwiki.metadata.save('data_columns', ['CouncilMember', 'address'])
base_url =  'http://www.phila.gov/citycouncil/'
# scrape_table function: gets passed an individual page to scrape
def scrape_table(soup):
    sidebar_list = soup.find("div", { "class" : "sidebarContent" })
        # Set up our data record - we'll need it later
    council_member = {}
    c_info = sidebar_list.findAll("ul")
    for ul in c_info:
        if ul:
            li = ul.findAll("li")
            for l in li:
                if l.find("a"):
                    council_member['CouncilMember'] = l.find("a")["title"]
                    council_page = scrape_council_page(l.find("a")["href"])
                    council_member[ADDRESS]= council_page[ADDRESS]
                    council_member[ZIP] = council_page[ZIP]
                    council_member[PHONE1] = council_page[PHONE1]
                    council_member[COMMITTEES] = council_page[COMMITTEES]
                    print council_member

def scrape_council_page(c_url):
    html = urllib.urlopen(base_url+c_url)
    soup = BeautifulSoup(html)
    sidebar_list = soup.find("div", {"class": "sidebarContent"})
    council_return = {}
    if sidebar_list:
        li = sidebar_list.findAll("li")
        council_return[COMMITTEES] = [l.text for l in li]
        address = parse_address(sidebar_list.findAll("p")[0].text) 
        council_return[ADDRESS] = address[ADDRESS]
        council_return[CITY] = address[CITY]
        council_return[ZIP] = address[ZIP]
    return council_return

def parse_address(addr_string):
    addr_return = {}
    addr = address_re.search(addr_string)
    try:
        addr_return[ADDRESS] = addr.group(1)
        addr_return[CITY] = addr.group(2)
        addr_return[ZIP] = addr.group(3)

        phone = phone_re.search(addr_string)
        addr_return[PHONE1] = phone.group(1)
    except:
        addr_return[ADDRESS] = ""
        addr_return[CITY] = ""
        addr_return[ZIP] = ""
        addr_return[PHONE1] = ""
    return addr_return
#scraperwiki.datastore.save(["CouncilMember"], council_member)
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(url):
    #html = scraperwiki.scrape(url)
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)
    scrape_table(soup)

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.phila.gov/citycouncil/'
starting_url = base_url + 'CouncilMembers.html'
scrape_and_look_for_next_link(starting_url)