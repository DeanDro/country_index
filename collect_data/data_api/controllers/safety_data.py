from bs4 import BeautifulSoup
import requests

# Safety index websites
travel_safe_index = "https://www.travelsafe-abroad.com/countries/"
wiki_peace_index = "https://en.wikipedia.org/wiki/Global_Peace_Index#Global_Peace_Index_2022_ranking"

data_safe_index = requests.get(travel_safe_index)
data_peace_index = requests.get(wiki_peace_index)


def collect_travel_safe_data():
    """
    Method that returns a dictionary with the safety levels for each 
    country based on the travel safe data
    """
    safety_dict = {}
    soup = BeautifulSoup(data_safe_index.content)
    table = soup.find('tbody')

    for row in table.findAll('tr'):
        safety_dict[row.a.text] = row.span.text
    
    return safety_dict

def collect_peace_index_data():
    """
    Returns a dictionary with the data from the wikipedia on the peace index
    for every nation.
    """
    peace_data = {}
    points = 101
    soup = BeautifulSoup(data_peace_index.content)
    table = soup.find('table', {"class" : 'wikitable sortable'})

    for row in table.findAll('a'):
        peace_data[row.text] = points
        points -= 1

    return peace_data

def return_safety_data():
    """
    Method that will collect the data from the other two methods and return a 
    dictionary with the safety index by country. 
    """
    peace_data = collect_peace_index_data()
    travel_data = collect_travel_safe_data()

    data = {
        'peace_data': {},
        'travel_data': {}
    }

    dict_data1 = {}
    for key in peace_data:
        dict_data1[key] = peace_data[key]
    
    dict_data2 = {}
    for key in travel_data:
        dict_data2[key] = travel_data[key]

    data['peace_data'] = dict_data1
    data['travel_data'] = dict_data2
    return data

