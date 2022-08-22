from bs4 import BeautifulSoup
import requests

"""
The purpose of this file is to hold the functions that will be responsible 
for collecting data on which countries are the best to raise a family.
"""

# URL for magazine containing a list for best places to raise a family
ceo_url = 'https://ceoworld.biz/2021/02/01/the-worlds-best-countries-for-raising-kids-2021/'

def family_friendly_data():
    """
    Function that will collect the data and send them
    in the form of a dictionary.
    """
    family_dict = {}
    data_request = requests.get(ceo_url)
    soup = BeautifulSoup(data_request.content)
    