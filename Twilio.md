# Python-Projects
This contains various projects on Python which i made when i was learning it.

#This project is based on Twilio, using it you can send text message to anyone free of cost.

from twilio import rest
 
# put your own credentials here 
ACCOUNT_SID = "AC872768cd87c2962f0dcd83d88cd33af2" 
AUTH_TOKEN = "469609c8093b0e4a9a9b459b4632535d" 
 
client = rest.TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
message = client.sms.messages.create(
    to="+918130723635", 
    from_="+16039523245", 
    body="Hello Subhash Tiwari from Python :)", 
)
print message.sid
