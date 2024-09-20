import shared
from security import safe_requests

def handler(event, context):
  response = safe_requests.get(shared.get_url(), stream=True)

  print(response.status_code)

  return response.status_code
