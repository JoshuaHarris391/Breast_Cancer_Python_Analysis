# # pip install cbio_py


# from cbio_py import cbio_mod as cb
# all_studies = cb.getAllStudies()

# import pandas as pd

# # Checking type
# type(all_studies)
# dir(all_studies)
# len(all_studies)
# all_studies

# all_studies_pd = pd.DataFrame(all_studies)
# type(all_studies_pd)
# dir(all_studies_pd)
# all_studies_pd.count()

# all_studies_pd.head()
# all_studies_pd.shape

# all_studies_pd.columns

# all_studies_pd

# cbioportal = cb.cbioportal
# cb.cbioportal

# molecProf = cb.getAllMolecularProfiles(return_type = 'dict')
# molecProfDF = pd.DataFrame(molecProf)
# molecProfDF.loc[42, 'molecularProfileId']

# rnaSeqZscore = cb.getMolecularProfile('brca_tcga_rna_seq_v2_mrna_median_Zscores', return_type = 'dict')
# rnaSeqZscoreDF = pd.DataFrame(rnaSeqZscore)

#############################

import requests

base_url = 'https://www.cbioportal.org/api/clinical-data/fetch'

# writing the header
header = {
    'Accept': 'application/json'
}

study_id = "brca_tcga"

# Pulling all clinical data
payload = {
    "attributeIds": [
        "string"
    ],
    "identifiers": [
        {
            "entityId": "string",
            "studyId": "string"
        }
    ]
}

response = requests.post(url=base_url, json=payload, headers=header)
response.status_code
response.json()