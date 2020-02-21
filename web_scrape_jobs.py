import requests
from bs4 import BeautifulSoup
link = 'https://www.seek.com.au/data-engineer-jobs-in-information-communication-technology'
h_class = '_3MPUOLE'
l_class = '_2e4Pi2B'
base_url = 'https://www.seek.com.au'

# extracts data by parsing html class
def scrape_data(URL,cls):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_=cls)
    return results

# extact skill list
def skill_list(URL,cls):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_=cls)
    key = results.find_all('ul')
    for key in results.find_all('ul'):
        print(key.text)

# extracts job, location, company and skills from data by passing different html class

def extact_from_data(cls1,cls2,cls3):
    results = scrape_data(link,h_class)
    for result in results:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
        title_elem = result.find('a', class_=cls1)
        location_elem = result.find('strong', class_=cls2)
        company_elem = result.find('a', class_=cls3)
        job_link = base_url+title_elem['href']
        print(title_elem.text.strip())
        print(location_elem.text.strip())
        print(company_elem.text.strip())
        skill_list(job_link,l_class)
        print()

extact_from_data('_2iNL7wI','lwHBT6d','_3AMdmRg')