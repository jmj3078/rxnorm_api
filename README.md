# rxnorm_api
Rxnorm Drug Interaction API module
## Requirements

  - requests
  - json
  - pandas

## drug_interaction_fromlist.py
Example : drug = Tylenol, Aricept / source = DrugBank / output = ./data.json

    python ./codes/get_drug_interaction_fromlist.py --drug Tylenol,Aricept --source DrugBank --output ./data.json

  - --drug : Drug names list, space must be comma(,)

  - --source : Must be DrugBank or ONCHigh

  - --output : Not required, if you want to save output file you have to input file path in .json format

## get_rxterm.py
Get up-to-date rxterm all concepts
