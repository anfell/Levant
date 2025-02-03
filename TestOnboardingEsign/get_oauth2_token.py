import hashlib
import base64
import random
import string
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
from requests import request
import json
from datetime import datetime





# constants
SPACE = " "
CLIENT_ID = "onboarding-web"
CLIENT_SECRET = "257d02c1-3700-49a7-ab76-6c584cbdf767"
EVENT_ID = "b3888d35-2a4b-4f67-baa8-2ae2f6bf8ec3.257d02c1-3700-49a7-ab76-6c584cbdf767.15a2d6b2-db09-4a63-a9d3-ef8cb77dec0e"





# obtain access token
url = "https://onboarding-web.uat.kian.digital/auth/callback"
data = {
    "grant_type": "authorization_code",
    "scope": "open-id"
}


response = request("POST", url, auth=(CLIENT_ID, CLIENT_SECRET), data=data)
print(json.dumps(response.json(), indent=4))
access_token = response.json()["access_token"]
token_type = response.json()["token_type"]

# make the request
now = datetime.now().isoformat()
url = "https://onboarding-web.uat.kian.digital/auth/callback"
headers = {
    "Authorization": token_type + SPACE + access_token,
    "Content-Type": "application/json"
}

response = request("GET", url, headers=headers)



print(response.text)





# #Get oAuth2 Token For CRM
# def get_oauth2_token_CRM(username, password):
#     token_endpoint = "https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/token"
#
#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'authorization': 'Bearer',
#         'content-type': 'application/x-www-form-urlencoded',
#         'origin': 'https://kd.uat.sivacrm.com',
#         'referer': 'https://kd.uat.sivacrm.com/',
#         'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#         'Cookie': 'AUTH_SESSION_ID=508a0d1a-159d-4eeb-b9e0-673a89a34248.keycloak-0; AUTH_SESSION_ID_LEGACY=508a0d1a-159d-4eeb-b9e0-673a89a34248.keycloak-0',
#     }
#
#     data = {
#         'grant_type': 'password',
#         'client_id': 'crm',
#         'client_secret': 'e07afb5d-2628-4af3-968c-4571f0d74585',
#         'username': username,
#         'password': password
#     }
#
#     response = requests.post(token_endpoint, headers=headers, data=data)
#     token_data = response.json()
#
#     access_token = token_data.get("access_token")
#     return access_token
#
# # Example usage
# username = "09125148058"
# password = "Behrud12345"
#
# access_token = get_oauth2_token_CRM(username, password)
# print("Access Token Crm:", access_token)
#
#
#
#
#
# #Get oAuth2 Token For CONBOARDING

# def get_oauth2_token_onboarding():
#     token_endpoint = "https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/token"
#
#     headers = {
#         'authority': 'uat.neshanid.com',
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
#         'authorization': 'Bearer',  # You need to provide the actual Bearer token here
#         'content-type': 'application/x-www-form-urlencoded',
#         'origin': 'https://kd.uat.sivacrm.com',
#         'referer': 'https://kd.uat.sivacrm.com/',
#         'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#         'Cookie': 'AUTH_SESSION_ID=508a0d1a-159d-4eeb-b9e0-673a89a34248.keycloak-0; AUTH_SESSION_ID_LEGACY=508a0d1a-159d-4eeb-b9e0-673a89a34248.keycloak-0',
#     }
#
#     data = {
#         'grant_type': 'password',
#         'client_id': 'onboarding',
#         'client_secret': '73a26bed-c82b-40ca-9e49-65145a2a013e',
#         'username': '09375613878',
#         'password': 'Aa123456'
#     }
#
#     response = requests.post(token_endpoint, headers=headers, data=data)
#     token_data = response.json()
#
#     access_token = token_data.get("access_token")
#     return access_token
#
# # Example usage
# access_token = get_oauth2_token_onboarding()
# print("Access Token Onboarding :", access_token)


#
#
#
# # Initialize ChromeOptions and set the --headless argument
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # To run Chrome in headless mode
# driver = webdriver.Chrome(options=chrome_options)
#
#
# def generate_code_verifier(length=64):
#     chars = string.ascii_letters + string.digits + '-._~'
#     return ''.join(random.choice(chars) for _ in range(length))
#
#
# def generate_code_challenge(code_verifier):
#     code_challenge = hashlib.sha256(code_verifier.encode()).digest()
#     code_challenge = base64.urlsafe_b64encode(code_challenge).rstrip(b'=').decode()
#     return code_challenge
#
#
# def get_access_token_with_pkce_and_selenium(client_id, redirect_uri, authorization_endpoint, username, otp):
#     code_verifier = generate_code_verifier()
#     code_challenge = generate_code_challenge(code_verifier)
#
#     driver = webdriver.Chrome(executable_path =':c\\chromedriver')
#
#     try:
#         params = {
#             'response_type': 'code',
#             'client_id': client_id,
#             'redirect_uri': redirect_uri,
#             'scope': 'openid',
#             'code_challenge': code_challenge,
#             'code_challenge_method': 'S256'
#         }
#
#         auth_url = f"{authorization_endpoint}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
#
#         driver.get(auth_url)
#
#         # Find input fields by name or any other suitable selector
#         username_input = driver.find_element(By.ID ,'username')
#         otp_input = driver.find_element(By.ID , 'otp')
#
#         username_input.send_keys(username)
#         otp_input.send_keys(otp)
#
#         # Simulate form submission
#         submit_button = driver.find_element(By.ID , 'submit-button')
#         submit_button.click()
#
#         # Wait for a while for the page to complete the redirection
#         time.sleep(5)
#
#         # Now, the driver should be on the redirect URI page with the authorization code in the URL
#         authorization_code = driver.current_url.split('code=')[1]
#
#         # Use the authorization code to obtain the access token
#         token_endpoint = 'https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/token'
#         token_data = {
#             'grant_type': 'authorization_code',
#             'client_id': client_id,
#             'redirect_uri': redirect_uri,
#             'code': authorization_code,
#             'code_verifier': code_verifier
#         }
#
#         response = requests.post(token_endpoint, data=token_data)
#         token_data = response.json()
#
#         access_token = token_data.get('access_token')
#         return access_token
#
#     finally:
#         driver.quit()
#
#
# # Provide your data
# client_id = 'onboarding-web'
# redirect_uri = 'http://localhost:3000/login'
# authorization_endpoint = 'https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/auth'
# username = '09375613878'  # Mobile number
# otp = '93878'  # Mock OTP
#
# # Get the access token using PKCE and Selenium
# access_token = get_access_token_with_pkce_and_selenium(client_id, redirect_uri, authorization_endpoint, username, otp)
#
# if access_token:
#     print("Access Token:", access_token)
# else:
#     print("Failed to obtain access token.")
#
#
#




#
#
#
#
#
#
#
#
# def get_oauth2_token_with_selenium():
#     # Start a new Chrome browser session in headless mode
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(options=chrome_options)
#
#     # Provide the authorization endpoint
#     auth_endpoint = "https://uat.neshanid.com/auth/realms/KIAN/protocol/openid-connect/auth"
#
#     # Fill in the information for user interaction
#     client_id = "onboarding-web"
#     redirect_uri = "https://onboarding-web.uat.kian.digital/auth/callback"
#     code_verifier = "K7oPLy6ULGnvE_6r3MR8ptp8VOucsDNSKE2O7VyMrdY"
#     product = "KIAN_TRADE"
#     code = "b3888d35-2a4b-4f67-baa8-2ae2f6bf8ec3.257d02c1-3700-49a7-ab76-6c584cbdf767.15a2d6b2-db09-4a63-a9d3-ef8cb77dec0e"
#     mobile_number = "09375613878"
#     otp = "93878"
#
#     # Navigate to the authorization endpoint
#     driver.get(f"{auth_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")
#
#     # Fill in the user information and submit the form
#     driver.find_element(By.ID, "username").send_keys(mobile_number)
#     driver.find_element(By.ID, "otp").send_keys(otp)
#     driver.find_element(By.ID, "code").send_keys(code)
#     driver.find_element(By.ID, "product").send_keys(product)
#     driver.find_element(By.ID, "code_verifier").send_keys(code_verifier)
#     driver.find_element(By.ID, "submit").click()
#
#     # Wait for a moment to simulate OTP validation
#     time.sleep(2)
#
#     # Extract the access token from the redirected URL
#     access_token = None
#     redirected_url = driver.current_url
#     if "access_token" in redirected_url:
#         params = redirected_url.split("#")[1].split("&")
#         for param in params:
#             if param.startswith("access_token="):
#                 access_token = param[len("access_token="):]
#                 break
#
#     # Close the browser session
#     driver.quit()
#
#     return access_token
#
#
# # Example usage
# access_token = get_oauth2_token_with_selenium()
# print("Access Token:", access_token)
