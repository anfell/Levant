import sys
import os
sys.path.append(os.getcwd())
import helper_functions
from GetTokenOAuth2.get_neshan_token import *
from Tools.get_identifier import *
import inspect
import ast

BASE_URL = "https://uat.kian.digital"

APPLICATION_NAME = "KIAN_DIGITAL"

identifierPath = os.path.join(os.getcwd() + "\KianDigitalFundsV3Esign", "identifiers.txt")

f = open(identifierPath, "r")
IDENTIFIERS = ast.literal_eval(f.read())
f.close()

PHONE_NUMBER = IDENTIFIERS[0]["phoneNumber"]
NATIONAL_CODE = IDENTIFIERS[0]["nationalCode"]
ONBOARDING_TOKEN = "Bearer " + get_onboarding_token(PHONE_NUMBER, "Aa123456").json()["access_token"]
result = f"\tNational Code: {IDENTIFIERS[0]['nationalCode']}\n \tPhone Number: {IDENTIFIERS[0]['phoneNumber']}\n"
print("\n" + result)
#
# isETF = ["FIXED_INCOME", "GOLD", "DORSA", "TRADABLE_INDEX", "KIAN_TRADE", "MORVARID_BAHA", "NEGIN_SAMAN", "DARA_ALGORITHM", "FARAZ_DARIK", "ETEMAD_DARIK", "BROKERAGE"]
# isNonETF = ["AVA", "NEDA", "BUSINESS_NEDA", "NAMAD_ASHNA", "TAZMIN_KIAN", "SAKHREH", "OFOGH", "AHANG"]



def test_get_application():
    get_application_response = helper_functions.get_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    data = get_application_response.json()
    assert get_application_response.status_code == 200
    assert data["applications"] != []


def test_start_application(productName):
    start_application_response = helper_functions.start_application(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME,NATIONAL_CODE,productName)
    # print(start_application_response.json())
    assert start_application_response.status_code == 200



def test_send_esign_otp(asset):
    test_send_esign_otp_response = helper_functions.send_esign_otp(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME,int(asset))
    assert test_send_esign_otp_response.status_code == 200


def test_verify_esign_otp(asset):
    test_verify_esign_otp_response = helper_functions.verify_esign_otp(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME, NATIONAL_CODE,int(asset))
    assert test_verify_esign_otp_response.status_code == 200




def test_submit_application(asset):
    test_submit_application_response = helper_functions.submit_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME,int(asset))
    # print(test_submit_application_response.json())
    assert test_submit_application_response.status_code == 200

