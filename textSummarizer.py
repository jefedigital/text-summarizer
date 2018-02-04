# https://market.mashape.com/textanalysis/text-summarization

# init
import config
import requests
import pandas as pd
import json

# settings
apiKey = 'your-mashape-key'
apiLimit = 90
requestHeader = {"X-Mashape-Key": apiKey,
                 "Content-Type": "application/x-www-form-urlencoded",
                 "Accept": "application/json"}
sentenceLimit = 1
source = 'data/pages.xlsx'
sourceColumn = 'description'
target = 'data/results.xlsx'
targetColumn = 'descriptionNew'

# functions
def summarize(description):
    payload = {"sentnum": sentenceLimit,"text": description}
    response = requests.post('https://textanalysis-text-summarization.p.mashape.com/text-summarizer-text',
                     headers=requestHeader,
                     data=payload)
    summary = json.loads(response.text)['sentences'][0]
    return summary

# load data
pages = pd.read_excel(source)

# summarize
pages[targetColumn] = pages[sourceColumn].apply(lambda x: summarize(x))

# write
pages.to_excel(target)
