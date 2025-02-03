import requests
import json
import re





# Onboarding Functions:Esign kt Brokerage
# URL:https://onboarding-web.uat.kian.digital/onboarding/kt-brokerage/applications

def get_application(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
    }

    return requests.get(base_url + "/usermgmt/api/v1/onboarding/home2",headers=headers)






def start_application(base_url, token, application_name, national_code):
    headers = {
        "Content-Type": "application/json",
        "application-name": application_name,
        "authorization": token,
        "mock": "true",
        "mockResult": "Sejami"
    }
    payload = json.dumps({
        "productGroupCode": "BROKERAGE",
        "startOnboardingFor": "MYSELF",
        "uniqueIdentifier": national_code
    })
    return requests.post(base_url + "/usermgmt/api/v1/users/start", headers=headers, data=payload)







def send_otp_fetch_sejam_data(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true"
    }
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/sjm/resendKyc/{application_id}", headers=headers)







def fetch_data_from_sejam(base_url, token, application_name, phone_number):
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true",
        "sejamiMobile": phone_number
    }
    payload = json.dumps({
        "applicationId": application_id,
        "otp": "12345"
    })
    return requests.post(base_url + "/usermgmt/api/v1/sjm/fetchDataFromSejam/", headers=headers, data=payload)








def confirm_fetch_data_from_sejam(base_url, token, application_name, phone_number):
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true",
        "sejamiMobile": phone_number,
        "ApplicationId": application_id
    }
    return requests.post(base_url + f"/usermgmt/api/v1/sjm/fetchDataFromSejam/confirm/{application_id}",headers=headers)






def send_financial_knowledge(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    payload = json.dumps({
        "tradingKnowledgeLevel": "EXCELLENT",
        "transactionLevel": "ONE"
    })
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/sjm/financial-knowledge/{application_id}",headers=headers,data=payload)






def send_bank_account(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    payload = json.dumps(
        [
            {
                "accountNumber": "3265487",
                "accountType": "LONGTERM",
                "bankId": "1",
                "branchInfo": {
                    "city": "0",
                    "code": "021365",
                    "name": "تجارت",
                    "province":"0"
                },
                "iban": "IR050550017080007139932001",
                "id": "string",
                 "isDefault": "true"
                              "",
                "submitState": "NEW"
            }
        ]
    )
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/sjm/bankAccounts/{application_id}",headers=headers,data=payload)







def get_online_exams(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
        "count": "6"
    }
    return requests.get(base_url + "/usermgmt/api/v1/onlineQuestion/get",headers=headers)






def verify_online_exams(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    payload = json.dumps(
        [
            {
                "answer": 1,
                "questionNumber": 4
            },
            {
                "answer": 1,
                "questionNumber": 2
            },
            {
                "answer": 3,
                "questionNumber": 3
            },
            {
                "answer": 4,
                "questionNumber": 1
            },
            {
                "answer": 2,
                "questionNumber": 5
            },
            {
                "answer": 4,
                "questionNumber": 6
            }
        ]
    )
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.post(base_url + f"/usermgmt/api/v1/onlineQuestion/verify/{application_id}", headers=headers, data=payload)



def oms_info(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    payload = json.dumps(
            {
              "oms": "RAYAN"
            }
    )
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.post(base_url + f"/usermgmt/api/v1/persons/oms-info/{application_id}", headers=headers, data=payload)




def send_esign_otp(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token
    }
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/esign/sendOTP/{application_id}",headers=headers)




def verify_esign_otp(base_url, token, application_name,national_code):
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    otp = national_code[-5] + national_code[-4] + national_code[-3] + national_code[-2] + national_code[-1]
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    payload = json.dumps(
        {
            "applicationId": application_id,
            "otp": otp
        }
    )
    return requests.post(base_url + "/usermgmt/api/v1/esign/verify-and-kyc", headers=headers, data=payload)






def submit_application(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    payload = json.dumps(
        {

        }
    )
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/users/submit?applicationId={application_id}", headers=headers, data=payload)







# CRM Functions:Esign kt Brokerage
def get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token, application_name):
    get_application_response = get_application(base_url, onboarding_token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "authorization": crm_token
    }
    return requests.get(base_url + f"/onboarding/api/v1/admin/opportunity/getOppByAppId/{application_id}", headers=headers)








def get_opportunity_identification(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token ,onboarding_token, application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    headers ={
        "authorization": crm_token
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}" , headers = headers)







def submit_check_identification(base_url,crm_token , onboarding_token , application_name):
    get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]

    get_opportunity_identification_response = get_opportunity_identification(base_url,crm_token , onboarding_token , application_name).json()
    get_opportunity_identification_response["bankAccountsStatus"] = "APPROVED"
    # print(get_opportunity_identification_response)
    headers = {
        "authorization": crm_token,
        "application-name": "CRM",
        "Content-Type": "application/json"
    }
    payload = json.dumps(get_opportunity_identification_response)
    return requests.put(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}" , headers = headers , data = payload)







def get_additional_info(base_url, crm_token,onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token, application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    # print(get_opportunity_id_response.json())

    headers = {
        "authorization": crm_token,
        "application-name": "CRM",
        "Content-Type": "application/json"
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/with-identification/{oppourtunity_id}", headers = headers)

#
#
#
#
#
# def submit_additional_info(base_url,crm_token , onboarding_token , application_name):
#     get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,application_name)
#     oppourtunity_id = get_opportunity_id_response.json()["id"]
#
#     get_additional_info_response = get_additional_info(base_url,crm_token , onboarding_token , application_name).json()
#
#     # if str(get_additional_info_response["nationality"]) == "None":
#     # get_additional_info_response["nationality"] = "ایرانی"
#
#
#
#     headers = {
#         "authorization": crm_token,
#         "application-name": "CRM",
#         "Content-Type": "application/json",
#         "content-length": "4052"
#     }
#     payload = json.dumps(get_additional_info_response, ensure_ascii=False)
#
#     return requests.put(base_url + f"/crm/api/v3/{application_name}/party/additional-info/{oppourtunity_id}", headers = headers , data = payload)






def confirm_by_qc(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]

    headers = {
        "Content-Type": "application/json",
        "application-name": "CRM",
        "authorization": crm_token
    }
    payload = json.dumps({})
    return requests.post(base_url + f"/crm/api/v3/{application_name}/action/opportunity/{oppourtunity_id}/confirm-by-qc", headers=headers, data=payload)







# Do Action RQ eSign
def do_action_rq(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]

    payload = {}
    headers = {
        'authorization': crm_token,
        'authority': 'uat.kian.digital',
        'accept': 'application/json',
        'application-name': 'CRM'
    }
    do_action_rq_response = requests.put(base_url + f"/crm/api/v3/KIAN_TRADE/action/opportunity/do-action/RQ/{levant_id}?productCode=BROKERAGE_ESIGN_V2",
        headers=headers, data=payload)

    if (do_action_rq_response.status_code == 200):
        get_opportunity_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                      application_name)
        action_id = get_opportunity_response.json()["actionId"]
        while action_id != 19:
            forward_action_fund(base_url, crm_token, onboarding_token, application_name)
            get_opportunity_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                          application_name)
            action_id = get_opportunity_response.json()["actionId"]
        else:
            cretae_rayan_user(base_url, crm_token, onboarding_token, application_name)
            get_opportunity_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                          application_name)
            action_id = get_opportunity_response.json()["actionId"]
            while action_id != 19:
                forward_action_fund(base_url, crm_token, onboarding_token, application_name)
                get_opportunity_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                              application_name)
                action_id = get_opportunity_response.json()["actionId"]
            return do_action_rq_response






def cretae_rayan_user(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    # print(get_opportunity_id_response.json())
    payload = {}
    headers = {
        'authority': 'uat.kian.digital',
        'accept': 'application/json, text/plain, */*',
        'application-name': 'CRM',
        'authorization': crm_token
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/action/opportunity/command/CREATE_RAYAN_USER/{oppourtunity_id}",
                        headers=headers)





# Forward Action eSign
def forward_action_fund(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Application-Name": application_name,
        "productCode": "BROKERAGE_ESIGN_V2",
        "authorization": crm_token

    }
    payload = json.dumps(
        {

        }
    )
    return requests.put(base_url + f"/crm/api/v3/{application_name}/action/opportunity/forward-action/{levant_id}",
                        headers=headers, data=payload)







# Finish Pipeline eSign
def finish_pipeline(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_id_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]

    get_additional_info_response = get_additional_info(base_url, crm_token, onboarding_token, application_name).json()

    # Extract and print the desired fields
    identifier = [
        {
            "Mobile Phone": get_additional_info_response["mobilePhone"],
            "First Name": get_additional_info_response["firstName"],
            "Last Name": get_additional_info_response["lastName"],
            "National Code": get_additional_info_response["nationalCode"]
        }
    ]


    payload = {}
    headers = {
        'application-name': 'CRM',
        "authorization": crm_token
    }
    finish_pipeline_response = requests.put(
        base_url + f"/crm/api/v3/{application_name}/action/opportunity/command/FINISH_PIPELINE/{oppourtunity_id}",
        headers=headers, data=payload)
    print(identifier)

    return finish_pipeline_response


