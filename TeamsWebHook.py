import subprocess
import pymsteams
myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>") #replace with Teams Webhook URL
email_address = "test@gmail.com" #Push in your test Email.
output = subprocess.check_output(['holehe','--only-used',str(email_address.replace(" ","").replace(",","."))])
my_json = output.decode('utf8').replace("'", '"')
my_json = my_json = my_json[150:-234] #.replace("\n","<br>"), if working in HTML
print(my_json)
myTeamsMessage.text(my_json)
myTeamsMessage.send()
