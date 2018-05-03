from datetime import datetime

def main(urd):
    now = datetime.now().strftime('%Y%m%d %H:%M:%S')

    urd.begin('connlog-raw', now)

    jid_prev = urd.latest('connlog-raw').joblist.jobid

    urd.build('csvimport',
            #options=dict(filename='test1.csv'),
            options=dict(filename='conn.log.gz', separator='\t'),
            datasets=dict(previous=jid_prev),
            name='connlog-cust-name')

    urd.finish('connlog-raw')
