from netmiko import ConnectHandler

Destination = input('Target IP: ')


#used to define the system being accessed
cisco = {
    'device_type':'cisco_ios',
    'host': str(Destination),
    'username':'',
    'password':'',
    'secret':'',
}
#applying the information to the connection manager
connect = ConnectHandler(**cisco)
#testing to verify if the connection is live
live = connect.find_prompt()
#setting the command interface to Exec mode using the listed secret
out_command = connect.enable()
#running some simple commands and getting their output
intbrief = connect.send_command('sh int brief')
ipbrief = connect.send_command('sh ip int brief')
shrun = connect.send_command('sh run')
#displaying their output
print(intbrief) 
print(ipbrief)
print(shrun)
