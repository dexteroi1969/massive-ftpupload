#!/usr/bin/env python
import subprocess
import ftplib

server = 'x.x.x.x' # set IPv4 address
username = '*****' # set Username for FTP
password = '*****' # set Password for FTP
remote_path = '/var/tmp/'  # set Path on FTP
local_path = '/var/log/mail/' # set Local Path with files
filename_template = 'test*' # set filename template, for example 'smtp-example-log*'
def bulkupload(a):
    ftp_connection = ftplib.FTP(server, username, password)
    ftp_connection.cwd(remote_path)
    fh = open(a, 'rb')
    file = a.split(local_path)
    ftp_connection.storbinary('STOR ' + file[1], fh)
    fh.close()
    ftp_connection.quit()
#Get files list
command = 'find '+local_path+filename_template+' -type f -mtime -1' # in this case it find all files older 1 day
p=subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)

out = p.stdout.read()
result = out.split('\n')
b=len(result)
print('Total files: '+str(b))

#Upload files to FTP
h=0
while (h<b):
    try:
        bulkupload(result[h])
    except:
        print('Procedure was failed!')
    h = h + 1
print('Files were successfully upload')

