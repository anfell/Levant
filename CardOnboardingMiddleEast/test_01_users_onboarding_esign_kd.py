import json
import sys
import os
sys.path.append(os.getcwd())
import helper_functions
from GetTokenOAuth2.get_neshan_token import *
from Tools.get_identifier import *
import inspect
import read_test_file


BASE_URL = "https://uat.kian.digital"

APPLICATION_NAME = "KIAN_DIGITAL"
IDENTIFIERS = read_test_file.read_file_from_folder_a()
print(IDENTIFIERS[0])
PHONE_NUMBER = IDENTIFIERS[0]["phoneNumber"]
NATIONAL_CODE = IDENTIFIERS[1]["nationalCode"]




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
PRODUCTNAME = "KIAN_CARD_MIDDLE_EAST"


def test_get_application():
    get_application_response = helper_functions.get_application(BASE_URL, ONBOARDING_TOKEN, APPLICATION_NAME)
    data = get_application_response.json()
    assert get_application_response.status_code == 200
    assert data["applications"] == []


def test_start_application(PRODUCTNAME):
    start_application_response = helper_functions.start_application(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME,NATIONAL_CODE,PRODUCTNAME)
    print(start_application_response)
    assert start_application_response.status_code == 200


def test_send_bank_otp():
    test_send_bank_otp_response = helper_functions.send_bank_otp(BASE_URL, ONBOARDING_TOKEN)
    assert test_send_bank_otp_response.status_code == 200


def test_verify_bank_otp():
    test_verify_bank_otp_response = helper_functions.verify_bank_otp(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME)
    # email = test_verify_bank_otp_response["privatePerson"]["email"]
    # print("Email:", email)
    assert test_verify_bank_otp_response.status_code == 200


def test_fetch_sabt_ahval_data():
    test_fetch_sabt_ahval_data_response = helper_functions.fetch_sabt_ahval_data(BASE_URL, ONBOARDING_TOKEN)
    assert test_fetch_sabt_ahval_data_response.status_code == 200


def test_submit_sabt_ahval_data():
    test_submit_sabt_ahval_data_response = helper_functions.submit_sabt_ahval_data(BASE_URL, ONBOARDING_TOKEN)
    assert test_submit_sabt_ahval_data_response.status_code == 200


def test_send_additional_info():
    test_send_additional_info_response = helper_functions.send_additional_info(BASE_URL, ONBOARDING_TOKEN)
    assert test_send_additional_info_response.status_code == 200


def test_address():
    test_address_response = helper_functions.address(BASE_URL, ONBOARDING_TOKEN)
    # print(test_address_response.json())
    assert test_address_response.status_code == 200


def test_upload_fileo():
    test_upload_file_response = helper_functions.upload_file(BASE_URL, ONBOARDING_TOKEN)
    assert test_upload_file_response.status_code == 200


def test_documents():
    test_documents_response = helper_functions.documents(BASE_URL, ONBOARDING_TOKEN)
    assert test_documents_response.status_code == 200


def test_contract():
    test_contract_response = helper_functions.contract(BASE_URL, ONBOARDING_TOKEN)
    assert test_contract_response.status_code == 200


def test_video_caption():
    test_video_caption = helper_functions.video_captio(BASE_URL, ONBOARDING_TOKEN)
    assert test_video_caption.status_code == 200


def test_upload_video():
    test_upload_video = helper_functions.upload_video(BASE_URL, ONBOARDING_TOKEN)
    assert test_upload_video.status_code == 200


def test_confirm_video():
    test_confirm_video = helper_functions.confirm_video(BASE_URL, ONBOARDING_TOKEN)
    assert test_confirm_video.status_code == 200


def test_submit_applicationo():
    test_submit_application = helper_functions.submit_application(BASE_URL, ONBOARDING_TOKEN)
    assert test_submit_application.status_code == 200


