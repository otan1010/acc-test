from extras import job_params
from collections import Counter

datasets = {'source',}

def synthesis():
    print()
    c = Counter(datasets.source.iterate(None, 'id.resp_h'))
    print(c.most_common(10))
    print()
