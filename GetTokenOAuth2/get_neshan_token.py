import requests
import json
def create_lead(username, password, product):
    payload = {}
    headers = {}
    return requests.post(f"https://uat.neshanid.com/auth/realms/KIAN/api/test-users/user/onboarding-web/{username}?password={password}&product={product}",headers=headers, data=payload)




def get_onboarding_token(username, password):
    payload = f"grant_type=password&client_id=onboarding-web&username={username}&password={password}"
    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }
    return requests.post("https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/token", headers=headers, data=payload)



def get_crm_token(username, password):
    payload = f"grant_type=password&client_id=crm-web&username={username}&password={password}"
    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }
    return requests.post("https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/token", headers=headers, data=payload)



def get_onboarding_token_credential():
    payload = 'client_id=kd-office&client_secret=WMLEI1fDqRw6LpHKF7zgM8MBBZJhHzt9&grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post("https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/token", headers=headers, data=payload)


#
# # Call the function
# response = get_onboarding_token("09375619887", "Aa123456")
# print(response.json())