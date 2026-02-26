import requests

def register(username, password):
  try:
    response = requests.post(
        "https://integrations-assignment-ticketforge.vercel.app/api/tforge/user/register",
        json={"username": username, "password": password}
    )
    response.raise_for_status()
    return "User registered successfully "
  except requests.exceptions.RequestException as e:
    return f"Failed to register user : {response.json()['message']}"
  
  
def login (username,password):
  try:
    response = requests.get(
        "https://integrations-assignment-ticketforge.vercel.app/api/tforge/workitems/mine",auth=(username,password)
    )
    response.raise_for_status()
    return "Login successful"
  except requests.exceptions.RequestException as e:
    return f"Failed to login user : {response.json()['message']}"