import requests
import json


# get up-to-date rxterm all concepts
base_url = "https://rxnav.nlm.nih.gov/REST/RxTerms/allconcepts.json"
response = requests.get(base_url)
data = response.json()
df = pd.DataFrame(data['minConceptGroup']['minConcept'])
df.to_csv("rxterm_allconcepts.csv")

