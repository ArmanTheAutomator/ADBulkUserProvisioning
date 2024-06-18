import requests
import json
import pyodbc

# Replace with your Azure credentials (consider environment variables)
tenant_id = "your_tenant_id"
client_id = "your_client_id"
client_secret = "your_client_secret"
role_id = "your_role_id"  # Replace with the desired Azure AD role ID

# SQL Server connection details
server = input("What is your SQL server name? : ")
database = input("What is your SQL database name? : ")
username = input("What is your SQL username? : ")
password = input("What is your SQL password? : ")


def get_access_token():
  resource = "https://graph.microsoft.com"
  token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
  payload = {
      "grant_type": "client_credentials",
      "client_id": client_id,
      "client_secret": client_secret,
      "scope": f"{resource}/.default"
  }
  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  response = requests.post(token_url, data=payload, headers=headers)
  response.raise_for_status()  # Raise exception for non-200 status codes
  return response.json()["access_token"]


def create_user(user_data):
  access_token = get_access_token()
  headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

  user_principal_name = user_data["email"]
  user_name = f"{user_data['first_name']} {user_data['last_name']}"

  # Check for username conflicts and append birthdate if needed
  user_exists = check_user_exists(user_principal_name, access_token)
  if user_exists:
      user_name = f"{user_name}-{user_data['birth_date'].strftime('%y%m%d')}"

  user_data = {
      "displayName": user_name,
      "userPrincipalName": user_principal_name,
      "passwordProfile": {
          "password": "StrongPassword123!"  # Replace with a strong password generation logic
      }
  }

  try:
      response = requests.post(user_url, headers=headers, json=user_data)
      response.raise_for_status()  # Raise exception for non-200 status codes
      print(f"User created successfully: {user_principal_name}")
      assign_role(user_principal_name, access_token)
  except requests.exceptions.RequestException as e:
      print(f"Error creating user: {user_principal_name} - {e}")


def check_user_exists(user_principal_name, access_token):
  headers = {"Authorization": f"Bearer {access_token}"}
  url = f"https://graph.microsoft.com/v1.0/users?$filter=userPrincipalName eq '{user_principal_name}'"
  response = requests.get(url, headers=headers)

  if response.status_code == 200 and response.json()["value"]:
      return True
  else:
      return False


def assign_role(user_principal_name, access_token):
  headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
  url = f"https://graph.microsoft.com/v1.0/directoryRoles/{role_id}/members/$ref"
  user_object_id_url = f"https://graph.microsoft.com/v1.0/users?$filter=userPrincipalName eq '{user_principal_name}'"
  response = requests.get(user_object_id_url, headers=headers)
  response.raise_for_status()  # Raise exception for non-200 status codes
  user_object_id = response.json()["value"][0]["id"]
  data = {"@odata.id": f"{url}/{user_object_id}"}
  response = requests.post(url, headers=headers, json=data)
  response.raise_for_status()  # Raise exception for non-200 status codes
  print(f"Role assigned successfully to {user_principal_name}")
