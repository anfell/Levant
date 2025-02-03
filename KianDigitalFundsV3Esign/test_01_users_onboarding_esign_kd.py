import json
import sys
import os
sys.path.append(os.getcwd())
import helper_functions
from GetTokenOAuth2.get_neshan_token import *
from Tools.get_identifier import *
import inspect

BASE_URL = "https://uat.kian.digital"

APPLICATION_NAME = "KIAN_DIGITAL"
IDENTIFIERS = generate_identifiers(1)
PHONE_NUMBER = IDENTIFIERS[0]["phoneNumber"]
NATIONAL_CODE = IDENTIFIERS[0]["nationalCode"]
CURRENT_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
create_lead_response = create_lead(PHONE_NUMBER,"Aa123456",APPLICATION_NAME)
if create_lead_response.status_code == 200:
    ONBOARDING_TOKEN = "Bearer " + get_onboarding_token(PHONE_NUMBER, "Aa123456").json()["access_token"]
else:
    exit(1)
filepath = os.path.join(CURRENT_PATH, "identifiers.txt")
f = open(filepath, "w")
f.write(str(IDENTIFIERS))
f.close()
result = f"\tNational Code: {IDENTIFIERS[0]['nationalCode']}\n \tPhone Number: {IDENTIFIERS[0]['phoneNumber']}\n"
print("\n" + result)

isETF = ["FIXED_INCOME", "GOLD", "DORSA", "TRADABLE_INDEX", "KIAN_TRADE", "MORVARID_BAHA", "NEGIN_SAMAN", "DARA_ALGORITHM", "FARAZ_DARIK", "ETEMAD_DARIK", "BROKERAGE"]
isNonETF = ["AVA_ETF", "NEDA", "BUSINESS_NEDA", "NAMAD_ASHNA", "TAZMIN_KIAN", "SAKHREH", "OFOGH", "AHANG"]


def test_get_application():
    get_application_response = helper_functions.get_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    data = get_application_response.json()
    assert get_application_response.status_code == 200
    assert data["applications"] == []


def test_start_application(productName):
    start_application_response = helper_functions.start_application(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME,NATIONAL_CODE,productName)
    print(start_application_response)
    assert start_application_response.status_code == 200



def test_send_otp_fetch_sejam_data():
    test_send_otp_fetch_sejam_data_response = helper_functions.send_otp_fetch_sejam_data(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_send_otp_fetch_sejam_data_response.status_code == 200



def test_fetch_data_from_sejam():
    test_fetch_data_from_sejam_response = helper_functions.fetch_data_from_sejam(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME,PHONE_NUMBER)
    # email = test_fetch_data_from_sejam_response["privatePerson"]["email"]
    # print("Email:", email)
    assert test_fetch_data_from_sejam_response.status_code == 200


def test_confirm_fetch_data_from_sejam():
    test_confirm_fetch_data_from_sejam_response = helper_functions.confirm_fetch_data_from_sejam(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME, PHONE_NUMBER)
    assert test_confirm_fetch_data_from_sejam_response.status_code == 200





def test_send_esign_otp():
    test_send_esign_otp_response = helper_functions.send_esign_otp(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_send_esign_otp_response.status_code == 200



def test_verify_esign_otp():
    test_verify_esign_otp_response = helper_functions.verify_esign_otp(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME, NATIONAL_CODE)
    assert test_verify_esign_otp_response.status_code == 200




def test_submit_application():
    test_submit_application_response = helper_functions.submit_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(test_submit_application_response.json())
    assert test_submit_application_response.status_code == 200