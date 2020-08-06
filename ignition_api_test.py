import requests
import json
import base64

from datetime import datetime 

resp = requests.get('http://23a5b8abd730.ngrok.io/ignition_data')
img = json.loads(resp.text)['img']
img = base64.b64decode(img)

with open('/Users/raymondfeng/Desktop/TrickyWays/cropped/chubert.jpeg', 'wb') as f:
	f.write(img)

# date_string = str(datetime.now()).replace('-','_').replace(' ', '_').replace(':','_').replace('.', '')