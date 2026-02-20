# demo/password

import paramiko

# pip install paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

port = 22
username = 'demo'
password = 'password'
host = 'test.rebex.net'

client.connect(
    hostname=host,
    port=port,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

sftp = client.open_sftp()  # połaczenie

file_list = sftp.listdir()
print(file_list)  # ['pub', 'readme.txt'], lista plików z serwera

sftp.close()
client.close()
