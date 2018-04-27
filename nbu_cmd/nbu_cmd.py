from common.common import *

def nbu_start_or_stop(action):
    cmd = '/etc/init.d/netbackup %s'%action
    result = run_cmd(cmd)
    return result

def get_hostlongname(hostname):
    cmd = 'nslookup %s |grep -i name|cut -f 2'%hostname
    hostlongname = str(run_cmd(cmd))
    return hostlongname.strip('\n')

def get_policys():
    cmd = '/usr/openv/netbackup/bin/admincmd/bppllist'
    result = run_cmd(cmd)
    return [i for i in result.split('\n') if i!='']

if __name__ == '__main__':
    r = nbu_start_or_stop('stop')
    print(r)
