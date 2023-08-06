import requests
import json
import argparse


# command line argument parsing
parser = argparse.ArgumentParser(description="Drug names list, source")
parser.add_argument('--drug', type=str, help="Drug name list, space must be comma(,)")
parser.add_argument('--source', type=str, help="DrugBank or ONCHigh")
parser.add_argument('--output', type=str, help="Output file, .json format", required=False)

args = parser.parse_args()
drug_list_str = args.drug 
source = args.source

# Get rxnorm code from drug name list
def get_rxnorm_code(drug_name):
    base_url = "https://rxnav.nlm.nih.gov/REST/rxcui.json"
    params = {
        "name": drug_name
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "idGroup" in data:
            if "rxnormId" in data["idGroup"]:
                rxnorm_code = data["idGroup"]["rxnormId"][0]
                return rxnorm_code
    else:
        print("Error: Failed to retrieve RxNORM code.")

    return None



# Get Interaction data from get_interactions_from_list API, NIH
def get_interactions_fromlist(source : str, rxnorm_code_list : list):
    if not isinstance(rxnorm_code_list, list) :
        print("Instance is not a list.")
        return 0

    else : 
        rxnorm_code = "%20".join(rxnorm_code_list)
        API_HOST = "https://rxnav.nlm.nih.gov"
        path = f"/REST/interaction/list.json?rxcuis={rxnorm_code}&sources={source}"
        
        url = API_HOST + path
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
        
        try:
            response = requests.get(url, headers=headers)
            print("response status %r" % response.status_code)
            print("response text %r" % response.text)
            data = response.json()
            return data

        except Exception as ex:
            print(ex)



drug_list = drug_list_str.replace(" ","").split(",")
rxnorm_code_list = []

for drug_name in drug_list:
    rxnorm_code_list.append(get_rxnorm_code(drug_name))
data = get_interactions_fromlist(source, rxnorm_code_list)

print(data)
print("Severity : ",data['fullInteractionTypeGroup'][0]['fullInteractionType'][0]['interactionPair'][0]['severity'])
print("Description : ",data['fullInteractionTypeGroup'][0]['fullInteractionType'][0]['interactionPair'][0]['description'])

if args.output :
    with open(args.output, 'w') as json_file:
        json.dump(data, json_file, indent='\t')

    print("Output file path : ", args.output)
