import pandas as pd
from fuzzywuzzy import process

# threshold = 1

# searchData = ['cintek', 'syntecch', 'sin tea ek', 'xintech', 'chintech', 'syntech2']
searchData = ['Oshundhara']
dbDatas = ['Bashundhara Group Ltd']


response = []
for name_to_find in searchData:
    resp_match = process.extractOne(name_to_find ,dbDatas)
    # if resp_match[1] > threshold:
    row = {'sample_name':name_to_find,'actual_name':resp_match[0], 'score':resp_match[1]}
    response.append(row)
    print(row)

results = pd.DataFrame(response)

# If you need all the 'actual_name' tp be in the datframe, continue below
# Otherwise don't include these last 2 lines of code
unmatched = pd.DataFrame([x for x in dbDatas if x not in list(results['actual_name'])], columns=['actual_name'])
results = results.append(unmatched, sort=False).reset_index(drop=True)