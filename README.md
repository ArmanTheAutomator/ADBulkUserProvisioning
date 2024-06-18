# ADBulkUserProvisioning
A python script that will bulk provision new users on Azure AD from an SQL database, using the Microsoft Graph API.
 

In order for this script to work, you'll need to make the following modifications to the source code. If you're going to hardcode the following variables into the source code, it is highly recommended to keep the code on an external hard drive, in a secure environment. Otherwise, please modify the variables into an input command (see below) or consider using environment variables.

These are the Azure AD specified variables that are required for this script to work: 

>>> tenant_id (Azure AD Tenant ID) : This identifies your specific Azure AD instance. It's a unique identifier for your organization's Azure Active Directory directory. You can find your tenant ID in the Azure portal under "Azure Active Directory" -> "Properties" -> "Directory ID". 
>>>
>>> client_id (Azure AD Application Client ID) : This identifies a specific application registered within your Azure AD tenant.
The script acts as an application and needs to be registered in Azure AD to access its functionalities.
You can find the client ID in the Azure portal under "Azure Active Directory" -> "App registrations" -> (your application) -> "Overview" -> "Application (client) ID".
>>>
>>> client_secret (Azure AD Application Client Secret) : This is a secret key associated with your registered application in Azure AD.
It acts like a password for your application and should be treated confidentially.
You can find (or regenerate) the client secret in the Azure portal under "Azure Active Directory" -> "App registrations" -> (your application) -> "Certificates & secrets" -> "Client secrets" -> "New client secret".

Once you have the above variables figured out, you'll need the information for the following input variables. 

Upon Running the script, you'll be prompted to provide the following information:

>>> user_principal_name : This will serve as the new user's Microsoft account and comes in the format of an email address. (i.e. newuser@example.com)
>>>
>>> user_name : This will serve as the new user's username. (i.e. New User)
>>>
>>> password : This will serve as the new user's temporary password, and will need to be changed.
>>>
>>> role_id : This will serve as the new user's role in the organization. Along with the assigned role, the new user will have predetermined permissions. You can find the role ID in the Azure portal under "Azure Active Directory" -> "Roles and Administrators" -> Click on the Desired Role -> Find "Object ID" under role details.
>>>
>>> Your SQL server info can be found through a variety of ways. If you have SQL Server Management Studio (SSMS), you can find your details there. Otherwise, you can find this info through a configuration file, a credential management portal, or an application configuration portal. 
>>>
>>> server : Your SQL server name.
>>>
>>> database : Your SQL database name.
>>>
>>> username : Your SQL database username.
>>>
>>> password : Your SQL database password.

Enjoy!

-
Arman "The Automator" Vakili
