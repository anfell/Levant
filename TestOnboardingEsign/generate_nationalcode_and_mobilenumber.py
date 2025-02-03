import requests
import json
from bs4 import BeautifulSoup
import random
from faker import Faker



# Generate Fake National Code

def generate_random_national_code():
    fake = Faker()
    random_number = fake.random_int(min=10**9, max=(10**10)-1)  # Generates a 10-digit number
    return str(random_number)

random_national_code = generate_random_national_code()
print("Random National Code:", random_national_code)





# # Generate Fake Mobile Number
def generate_random_mobile_number():
    while True:
        mobile_number = "09" + ''.join(random.choice("0123456789") for _ in range(9))
        if len(mobile_number) == 11:
            return mobile_number

random_mobile_number = generate_random_mobile_number()
print("Random Mobile Number:", random_mobile_number)






# # Generate National Code and Mobile Number
# url = "https://eliagroup.ir/acreate-code"
# # url = "https://majidh1.github.io/iranianNationalCode/"
#
#
#
# payload = {}
# headers = {
#   'authority': 'eliagroup.ir',
#   'accept': '*/*',
#   'accept-language': 'en-US,en;q=0.9',
#   'content-length': '0',
#   'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=bd4d8a0b-fa65-0405-bbbf-105233f009bf; yektanet_session_last_activity=8/5/2023; _yngt_iframe=1; _yngt=12368875-5cb9e-e9958-847a0-0c51a64d185f1; XSRF-TOKEN=eyJpdiI6ImpaMVFyYTVRam8vaHh1dTdNTU1BelE9PSIsInZhbHVlIjoiczhubk1tYjNwZk50RHc1QTI3VGFvUldGNUpiT1cvR29WaUpucTJmby9PdmMzNjFtQ2FCQTA2Mk5NR2Y2M2Mxb2ZzcWhUVzdpN3RFb0NRU3M4eXo4NUc2TW9WdmhJODI1WkprNG00eE1xak9haFVvREd5VjZDOExUcDc4SlhPMGUiLCJtYWMiOiI2N2M0NTkzYTViODMwY2NjM2U0ODk5ZTM0MWY1NTk5OGJkMzhlMTFlYTIyNjQ2Mzk2NmNkOWI5NTAyNDYzZDI1IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImhZUlpod0Q1YzNrWTNPeFVWYXdOeEE9PSIsInZhbHVlIjoidlVmN2hGbE55VFBSendCeFhIVWhkdFliTnJYMlBobkM0RHdCdEFzaWVudjVQR1NnZklyTHk1bFdjVG4yZ3FsODkzUFJ1WjNjVmtBRnRnM1p2RjZheEFKcEczaU1rM29JL25qeFdHV1IwOWRzTy92b2gydUNvbnVIQWNhWTY0bTQiLCJtYWMiOiI3MThiYzQzNWJmNGIzMDE4MjFiNmViMmM0YjM4ZGNhMzZiMDQxM2Q1Mzc5N2E4NDFjMTViMTZkMWEyZTE3NTU3IiwidGFnIjoiIn0%3D; content-view-yn-notification-75014=4; content-view-yn-footer-sticky-75015=4; XSRF-TOKEN=eyJpdiI6IlIyVmQ0eHZuNVpCWWd0TU1vSjBsMXc9PSIsInZhbHVlIjoibFJEOUZFdnhiL25Fbkw0cHcwbHBQSXk3Mk12TkZhS21CZXBjaXNPOEtmQmg0TmJGbm9MOU52eHU0cXdIdjhtVStPOUlKcXN3VnBLZ1RGek5nbk5hSmFudFJPbmVEY0RnbnIvU0pYOFlWZFNOVW9hejRvT2pGNVFEOTNiZEhpK0MiLCJtYWMiOiJkMzJhYWRmZGUyODI5YTA5ZTQ1NTUwN2MzNTE5ZmJhYmE3YzRhN2JhY2Y2NzRkZmI5MTYyZGVkYzBlOWIyMThlIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImZRMHdHZEVsQVZWdjdXSEhTUVR0bkE9PSIsInZhbHVlIjoiSDlBYU5pbE5KU28zMXZkVWIwL3p6cGZMU1puVkMxak5NbS9DZXlyRnBTcThzdktDSEVCWTJRSnVzUXY0ZVdRZmRVMHRRWGZkcEZ6ZFNXaHdDN2pTMmZRZWNxZzFjR1MzeDAxTVk1MTRFM0o4Y2I2S05LRDdKVGpqeWJQdE9FSUIiLCJtYWMiOiIzY2RhOTc0ZDI0YTZjNTcxY2I0YTgyN2JiNTUxNDlkN2M5Yjk4N2I4NzMyNDlmODVhNGQ0OTQwMjliNWJjYjg3IiwidGFnIjoiIn0%3D',
#   'dnt': '1',
#   'origin': 'https://eliagroup.ir',
#   'referer': 'https://eliagroup.ir/tutorials/article/21/code-meli',
#   'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#   'x-requested-with': 'XMLHttpRequest',
#   'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrcmJNbXE5b2tqN0pTVHB5MzJmTUV1dXFlazZfdUF4Y1pRMVNEZmRMa2I0In0.eyJleHAiOjE2OTEyNDI0NzYsImlhdCI6MTY5MTIxMzY3NywiYXV0aF90aW1lIjoxNjkxMjEzNjc2LCJqdGkiOiI4Mzc2NGZmMi1mYzQyLTRiZmQtYTljZi05Y2NmYjI1ODc5ZmMiLCJpc3MiOiJodHRwczovL3VhdC5uZXNoYW5pZC5jb20vYXV0aC9yZWFsbXMvS0lBTiIsImF1ZCI6WyJvYXV0aDItcmVzb3VyY2UiLCJraWFuLWF1ZCIsImFjY291bnQiXSwic3ViIjoiMjhiMTM4NzYtMjhkMi00ZjZiLTk0YTQtNTRlNmUxYTM2MTNiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoib25ib2FyZGluZy13ZWIiLCJzZXNzaW9uX3N0YXRlIjoiZWI2OTY3M2EtMTU2NS00NTljLWE2NmYtMzYzN2E1ZjdhYzJlIiwic2NvcGUiOiJvcGVuaWQgTEVWQU5UX0NSRURJVF9HUkFERV9FUVVBTElaQVRJT05fREVGIExFVkFOVF9DUkVESVRfRklOQU5DSUFMX1NUQVRFTUVOVCBMRVZBTlRfQ1JFRElUX1NDT1JFX01BUFBJTkcgb2F1dGgyLXJlc291cmNlIHJvbGVzIExFVkFOVF9DUkVESVRfQlVTSU5FU1NfSU5GTyBjcm0gTEVWQU5UX0NSRURJVF9HUkFERV9FUVVBTElaQVRJT04gb25ib2FyZGluZyBMRVZBTlRfQ1JFRElUX0ZJTkFOQ0lBTF9TVEFURU1FTlRfV0VJR0hUIExFVkFOVF9DUkVESVRfUEFSQU1FVEVSIiwic2lkIjoiZWI2OTY3M2EtMTU2NS00NTljLWE2NmYtMzYzN2E1ZjdhYzJlIiwidXNlcl9uYW1lIjoiMDkxMjQxNjk3NjIiLCJ1dWlkIjoiMjhiMTM4NzYtMjhkMi00ZjZiLTk0YTQtNTRlNmUxYTM2MTNiIiwiY2xpZW50X2lkIjoiVU5LTk9XTiIsImF1dGhvcml0aWVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiLCJkZWZhdWx0LXJvbGVzLWtpYW4iLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiVVNFUiJdLCJsZXZhbnRJZCI6IjEwMDAwMDQyMDU4In0.g2WQrQ6BAVlwQJFRzDYChjrdC2Kf6q_LdhAJ3kzjk9jLsuHavjEhJ_3H9q-cZLkvhOr8GDgNOYPMjpdTLvLajWVqyWtFEP3O4zngKUGXPRzIyLCypS5ooueah7W4uSJ4-KJ7ctvJQBR2wYLfkhfpHyBj-0ImLHL80tII6H9xkEo'
#
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
#
#
#
#
# # Number of national codes you want to generate
# num_codes = 6
#
#
# # Store the generated codes and corresponding mobile numbers
# generated_national_codes = []
# generated_mobiles = []
#
# # Calculate the number of requests needed
# num_requests = (num_codes + 1) // 1  # Integer division rounded up
#
#
#
# # Send multiple POST requests to the service
# for _ in range(num_requests):
#     response = requests.post(url, headers=headers, data=payload)
#     if response.status_code == 200:
#         codes = response.text.strip().split('\n')
#         generated_national_codes.extend(codes)
#         generated_mobiles.extend([f"09{random.randint(10000000, 99999999)}" for _ in range(len(codes))])
#
#
#
# # Take the first `num_codes` generated codes and mobile numbers, or fewer if there are not enough available
# filtered_codes = generated_national_codes[:num_codes]
# filtered_mobiles = generated_mobiles[:num_codes]
#
# # Print the generated codes and mobile numbers
# for i, (code, mobile) in enumerate(zip(filtered_codes, filtered_mobiles)):
#     print(f"Generated Code {i+1}: {code}")
#     print(f"Generated Mobile {i+1}: {mobile}")
#
#