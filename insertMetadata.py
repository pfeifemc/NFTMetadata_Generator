import os
import io
import csv
import sys
import math
import json

# This tool takes Mickey Degods Combo NFT data and inserts it into
# JSON files corresponding to the NFT (name of file, file attributes)

# pseudo:
#1: Fox delivers a folder of numbered images 0 thru n
#2: The metadata on our spreadsheet has every piece of data needed as well as a matching ID to the image
#3: For each image number in the list...
  # Grab trait info for this image:
    # Combo name
    # Royalty address
    # Attributes: 
      # Items 1 thru 5 (none is valid entry)
      # Skin
      # Chain
      # Neck tat
      # Arm tat
      # Special
    # Calculated royalty (number out of 100, i.e. 5% = 5)
  # Insert into an array (list)
  # Dump into JSON named after this image number

#### Generate Metadata for each Image    

f = open('./combos_batch8.json',) 

if not os.path.exists('./metadata'):
    os.makedirs('./metadata')

data = json.load(f)

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for i in data:
    token_id = i['tokenId']
    share = int(i['share']) * 10
    addy = i['address']
    token = {
        "name": str(i['name']).strip(),
        "symbol": "COMBOS",
        "image": str(token_id) + '.png', #IMAGES_BASE_URL + 
        "description": "A delicious combo of Mickey's finest menu items - Stake this for $DUST or you're probably NGMI.  Visit us at http://www.mickeydegods.com/ and follow us @mickeydegods on Twitter.",
        "tokenId": token_id,
        "external_url": "http://www.mickeydegods.com/",
        "seller_fee_basis_points": 1000,
        "properties": {
          "files": [
            {
              "uri": str(token_id) + '.png',
              "type": "image/png"
            }
          ],
          "category": "image",
          "creators": [
            {
              "address": "J7T25FgKxrHqL7CpX8r6kSMcSRgST21mgkf5jCtw1z6j", # DAO addy
              "share": 70 - share
            },
            {
              "address": "13JRnpvnSXqjUMAn1RbJjurMVpJHcwZYfdTNaNM4Pegm", # Fox addy
              "share": 30
            },
            {
              "address": str(addy).strip(), #royalty addy
              "share": share
            }
          ]
        },
        "collection": {"name": "Mickeys Combos", "family": "Mickey Degods"},
        "attributes": []
    }
    token["attributes"].append(getAttribute("Item 1", i["Item 1"]))
    token["attributes"].append(getAttribute("Item 2", i["Item 2"]))
    token["attributes"].append(getAttribute("Item 3", i["Item 3"]))
    token["attributes"].append(getAttribute("Item 4", i["Item 4"]))
    token["attributes"].append(getAttribute("Item 5", i["Item 5"]))
    token["attributes"].append(getAttribute("Skin", i["Skin"]))
    token["attributes"].append(getAttribute("Chain", i["Chain"]))
    token["attributes"].append(getAttribute("Neck Tat", i["Neck Tat"]))
    token["attributes"].append(getAttribute("Special Arm Tat", i["Special Arm Tat"]))
    token["attributes"].append(getAttribute("One of One Item", i["One of One Item"]))
    token["attributes"].append(getAttribute("Extra Item", i["Extra Item"]))
    token["attributes"].append(getAttribute("Special Combo", i["Special Combo"]))
    token["attributes"].append(getAttribute("Number of Items", i["Number of Items"]))

    with open('./metadata/' + str(token_id) + ".json", 'w', newline='') as outfile:
        json.dump(token, outfile, indent=4)

f.close()
