#!/usr/bin/python

import json
import subprocess

## Downdated to run on python 2.6

# Added function implementation
def check_output(*popenargs, **kwargs):
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        error = subprocess.CalledProcessError(retcode, cmd)
        error.output = output
        raise error
    return output

if __name__ == '__main__':
    #output = subprocess.check_output("cat /proc/diskstats | awk '{print $3}' | grep -v 'ram\|loop\|sr'", shell=True)
    output = check_output("cat /proc/diskstats | awk '{print $3}' | grep -v 'ram\|loop\|sr'", shell=True)
    data = list()
    for line in output.split("\n"):
        if line:
	        data.append({"{#DEVICE}": line, "{#DEVICENAME}": line.replace("/dev/", "")})

    print(json.dumps({"data": data}, indent=4))
