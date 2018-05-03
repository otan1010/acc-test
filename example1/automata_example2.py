from datetime import datetime

def main(urd):
    now = datetime.now().strftime('%Y%m%d %H:%M:%S')

    urd.begin('connlog-process', now)
    
    jid_connlog = urd.latest('connlog-raw').joblist.jobid
    
    urd.build('process_conn', datasets=dict(source=jid_connlog), name='process_conn-cust-name')
    
    urd.finish('connlog-process')
