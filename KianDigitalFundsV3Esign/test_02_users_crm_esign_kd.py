import sys
import os
sys.path.append(os.getcwd())
import helper_functions
from GetTokenOAuth2.get_neshan_token import *
import ast
import inspect


CURRENT_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
identifierPath = os.path.join(CURRENT_PATH, "identifiers.txt")
print(identifierPath + "\n")
resultPath = os.path.join(CURRENT_PATH, "result1.txt")
# print(resultPath)
f = open(identifierPath, "r")
fResult = open(resultPath, "a")
IDENTIFIERS = ast.literal_eval(f.read())
result = f"eSign KD Funds opportunity has been activated for:\n \tNational Code: {IDENTIFIERS[0]['nationalCode']}\n \tPhone Number: {IDENTIFIERS[0]['phoneNumber']}\n"
f.close()
PHONE_NUMBER = IDENTIFIERS[0]["phoneNumber"]
NATIONAL_CODE = IDENTIFIERS[0]["nationalCode"]

BASE_URL = "https://uat.kian.digital"

APPLICATION_NAME = "KIAN_DIGITAL"
CRM_TOKEN = "Bearer " + get_crm_token("09125148058", "Behrud12345").json()["access_token"]
ONBOARDING_TOKEN = "Bearer " + get_onboarding_token(PHONE_NUMBER, "Aa123456").json()["access_token"]



def test_get_oppourtunity_by_application_id():
    get_opportunity_id_response = helper_functions.get_oppourtunity_by_application_id(BASE_URL, CRM_TOKEN,ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(get_opportunity_id_response.json())
    assert get_opportunity_id_response.status_code == 200




def test_do_action_rq():

    get_do_action_rq_response = helper_functions.do_action_rq(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(get_do_action_rq_response.json())
    assert get_do_action_rq_response.status_code == 200



def test_get_opportunity_identification():
    get_opportunity_identification_response = helper_functions.get_opportunity_identification(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(get_opportunity_identification_response.json())
    assert get_opportunity_identification_response.status_code == 200




def test_submit_check_identification():
    submit_check_identification_response = helper_functions.submit_check_identification(BASE_URL,CRM_TOKEN,  ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(submit_check_identification_response.json())
    assert  submit_check_identification_response.status_code == 200




def test_get_additional_info():
    get_additional_info_response = helper_functions.get_additional_info(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(get_additional_info_response.json())
    assert get_additional_info_response.status_code == 200




#
# def test_submit_additional_info():
#     submit_additional_info_response = helper_functions.submit_additional_info(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME)
#     print(submit_additional_info_response.json())
#     # assert submit_additional_info_response.status_code == 200
#
#


def test_confirm_by_qc():
    confirm_by_qc_response = helper_functions.confirm_by_qc(BASE_URL,CRM_TOKEN,ONBOARDING_TOKEN,APPLICATION_NAME)
    # print(confirm_by_qc_response.json())
    assert confirm_by_qc_response.status_code == 200


def test_finish_pipeline():
    finish_pipeline_response = helper_functions.finish_pipeline(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME)
    # print(finish_pipeline_response.json())
    assert finish_pipeline_response.status_code == 200
    fResult.write(str(result))
    fResult.close()