import requests

def handler(event, context):
  r = requests.get('https://aws.amazon.com', timeout=60)

  print(r.status_code)

  return r.status_code
