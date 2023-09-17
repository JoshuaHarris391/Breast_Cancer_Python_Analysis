# pip install cbio_py


from cbio_py import cbio_mod as cb
all_studies = cb.getAllStudies()

import pandas as pd

# Checking type
type(all_studies)
"TCGA-BRCA" in all_studies
all_studies.dim()
dir(all_studies)
len(all_studies)
all_studies[0]

all_studies_pd = pd.DataFrame(all_studies)
type(all_studies_pd)
dir(all_studies_pd)
all_studies_pd.count

all_studies_pd.head()
all_studies_pd.shape

all_studies_pd.columns

all_studies_pd