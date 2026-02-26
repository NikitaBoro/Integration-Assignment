import requests

def create_ticket(username,password,title, description=None,depends_on=None):
  
  json = {"title": title}
  if description is not None:
      json["description"] = description
  if depends_on is not None:              
      json["dependsOn"] = depends_on
        
  try:
    response = requests.post(
        "https://integrations-assignment-ticketforge.vercel.app/api/tforge/workitem/publish",
        json=json,
        auth = (username,password)
    )
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    return response.json()
  
def list_tickets(username,password,limit=5):      
  try:
    response = requests.get(
        f"https://integrations-assignment-ticketforge.vercel.app/api/tforge/workitems/mine?limit={limit}",
        auth = (username,password)
    )
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    return response.json()
  

def get_ticket(username,password,ref):
  response = requests.get(
    f"https://integrations-assignment-ticketforge.vercel.app/api/tforge/workitem/{ref}",
    auth=(username, password)
  )
  response.raise_for_status()
  return response.json()

def edit_ticket(username,password,ref,title=None, description=None,depends_on=None):
  
  if title is None and description is None and depends_on is None:
    return {"success": True, "message": "Nothing to update"}
  
  try:
    current_ticket = get_ticket(username, password, ref)
  except requests.exceptions.HTTPError as e:
    return {
        "success": False,
        "error": f"Ticket {ref} not found or unauthorized"
    }
  except requests.exceptions.RequestException as e:
    return {
        "success": False,
        "error": str(e)
    }

  workitem = current_ticket["workitem"]
  
  json = {
    "title": workitem["title"],
    "description": workitem.get("description"),
    "dependsOn": workitem.get("dependsOn"),
    "stage": workitem["stage"],
  }
  
  if title is not None:
    json["title"] = title
  if description is not None:
    json["description"] = description
  if depends_on is not None:              
    json["dependsOn"] = depends_on
  
  try:
    response = requests.put(
        f"https://integrations-assignment-ticketforge.vercel.app/api/tforge/workitem/{ref}",
        json=json,
        auth = (username,password)
    )
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    return response.json()