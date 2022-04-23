#! /usr/bin/python

# Imports
import requests

# def send_simple_message():
#     print("I am sending an email.")
#     return requests.post(
#         "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
#         auth=("api", "YOUR_API_KEY"),
#         data={"from": 'hello@example.com',
#             "subject": "Visitor Alert",
#             "html": "<html> Your Raspberry Pi recognizes someone. </html>"})
    
def send_simple_message():
    	return requests.post(
		"https://api.mailgun.net/v3/sandbox5799b990c7c54e1184f6c669b90ad5c5.mailgun.org/messages",
		auth=("api", "6e92ee7d15a9deb0cb03d1eb24604ce7-02fa25a3-7bf7ebba"),
		data={"from": "Queens Home mailgun@sandbox5799b990c7c54e1184f6c669b90ad5c5.mailgun.org",
			"to": ["zinwotatimothy@gmail.com"],
		   "subject": "Visitor Alert",
            "html": "<html> <h1>Visitor Alert!!</h1></br>Your Raspberry Pi recognizes someone. </html>"})
                      
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
