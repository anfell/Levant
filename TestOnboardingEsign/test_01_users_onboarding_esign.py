import helper_functions
from GetTokenOAuth2.get_neshan_token import *
from Tools.get_identifier import *
import os
import inspect

BASE_URL = "https://uat.kian.digital"
APPLICATION_NAME = "KIAN_TRADE"
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

def test_get_application():
    get_application_response = helper_functions.get_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    data = get_application_response.json()
    assert get_application_response.status_code == 200
    assert data["applications"] == []


def test_start_application():
    start_application_response = helper_functions.start_application(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME,NATIONAL_CODE)
    assert start_application_response.status_code == 200


def test_send_otp_fetch_sejam_data():
    test_send_otp_fetch_sejam_data_response = helper_functions.send_otp_fetch_sejam_data(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_send_otp_fetch_sejam_data_response.status_code == 200



def test_fetch_data_from_sejam():
    test_fetch_data_from_sejam_response = helper_functions.fetch_data_from_sejam(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME,PHONE_NUMBER)
    assert test_fetch_data_from_sejam_response.status_code == 200


def test_confirm_fetch_data_from_sejam():
    test_confirm_fetch_data_from_sejam_response = helper_functions.confirm_fetch_data_from_sejam(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME, PHONE_NUMBER)
    assert test_confirm_fetch_data_from_sejam_response.status_code == 200


def test_send_financial_knowledge():
    test_send_financial_knowledge_response = helper_functions.send_financial_knowledge(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_send_financial_knowledge_response.status_code == 200


def test_send_bank_account():
    test_send_bank_account_response = helper_functions.send_bank_account(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_send_bank_account_response.status_code == 200


def test_get_online_exams():
    test_get_online_exams_response = helper_functions.get_online_exams(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_get_online_exams_response.status_code == 200

def test_verify_online_exams():
    test_verify_online_exams_response = helper_functions.verify_online_exams(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_verify_online_exams_response.status_code == 200

def test_oms_info():
    test_oms_info_response = helper_functions.oms_info(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_oms_info_response.status_code == 200

def test_send_esign_otp():
    test_send_esign_otp_response = helper_functions.send_esign_otp(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_send_esign_otp_response.status_code == 200



def test_verify_esign_otp():
    test_verify_esign_otp_response = helper_functions.verify_esign_otp(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME, NATIONAL_CODE)
    assert test_verify_esign_otp_response.status_code == 200




def test_submit_application():
    test_submit_application_response = helper_functions.submit_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    assert test_submit_application_response.status_code == 200