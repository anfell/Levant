
import sys
import os
sys.path.append(os.getcwd())
import helper_functions
from GetTokenOAuth2.get_neshan_token import *
import ast
import inspect


CURRENT_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
identifierPath = os.path.join(os.getcwd() + "\KianDigitalFundsV3Esign", "identifiers.txt")
print(identifierPath + "\n")
resultPath = os.path.join(CURRENT_PATH, "result.txt")
# print(resultPath)
f = open(identifierPath, "r")
fResult = open(resultPath, "a")
IDENTIFIERS = ast.literal_eval(f.read())
result = f"\tNational Code: {IDENTIFIERS[0]['nationalCode']}\n \tPhone Number: {IDENTIFIERS[0]['phoneNumber']}\n"
f.close()
PHONE_NUMBER = IDENTIFIERS[0]["phoneNumber"]
NATIONAL_CODE = IDENTIFIERS[0]["nationalCode"]

BASE_URL = "https://uat.kian.digital"

APPLICATION_NAME = "KIAN_DIGITAL"
CRM_TOKEN = "Bearer " + get_crm_token("09125148058", "Behrud12345").json()["access_token"]
ONBOARDING_TOKEN = "Bearer " + get_onboarding_token(PHONE_NUMBER, "Aa123456").json()["access_token"]


# def test_is_application_won(asset):
#     get_application_response = helper_functions.get_application(BASE_URL,ONBOARDING_TOKEN,APPLICATION_NAME)
#     application_final_status = get_application_response.json()["applications"][int(asset)]["applicationFinalStatus"]
#     if application_final_status == "WON":
#         print(application_final_status)
#         exit()

# def test_get_oppourtunity_by_application_id(asset):
#     get_opportunity_id_response = helper_functions.get_oppourtunity_by_application_id(BASE_URL, CRM_TOKEN,ONBOARDING_TOKEN, APPLICATION_NAME,int(asset))
#     # print(get_opportunity_id_response.json()["id"])
#     assert get_opportunity_id_response.status_code == 200






def test_do_action_rq(asset):
    get_do_action_rq_response = helper_functions.do_action_rq(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME,int(asset))
    # print(get_do_action_rq_response.json())
    assert get_do_action_rq_response.status_code == 200





def test_finish_pipeline(asset):
    finish_pipeline_response = helper_functions.finish_pipeline(BASE_URL, CRM_TOKEN, ONBOARDING_TOKEN, APPLICATION_NAME,int(asset))
    # print(finish_pipeline_response.json())
    assert finish_pipeline_response.status_code == 200
