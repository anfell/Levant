import json
import sqlite3
import requests




# Onboarding Functions:Asset Funds
# Get Application
def get_application(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
    }

    return requests.get(base_url + "/usermgmt/api/v1/onboarding/home2", headers=headers)




# Start Application
def start_application(base_url, token, application_name, national_code, product_name):
    headers = {
        "Content-Type": "application/json",
        "application-name": application_name,
        "authorization": token,
        "mock": "true",
        "mockResult": "Sejami"
    }
    payload = json.dumps({
        "productGroupCode": product_name,
        "startOnboardingFor": "MYSELF",
        "uniqueIdentifier": national_code,
        "birthDate": 493425000000,
        "extraDataSet": [
            {
                "key": "VERSION",
                "value": "V3"
            },
            {
                "key": "KDFUNDS",
                "value": "ESIGN"
            }

        ]

    })
    return requests.post(base_url + "/usermgmt/api/v1/users/start", headers=headers, data=payload)





# Send Esign OTP
def send_esign_otp(base_url, token, application_name,asset):
    headers = {
        "Application-Name": application_name,
        "authorization": token
    }
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][asset]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/esign/sendOTP/{application_id}", headers=headers)





# Verify Esign OTP
def verify_esign_otp(base_url, token, application_name, national_code,asset):
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][asset]["applicationID"]
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






# Submit Application
def submit_application(base_url, token, application_name,asset):
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
    application_id = get_application_response.json()["applications"][asset]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/users/submit?applicationId={application_id}", headers=headers,
                        data=payload)







# CRM Functions
# Get Opportunity By Application Id
def get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token, application_name,asset):
    get_application_response = get_application(base_url, onboarding_token, application_name)
    application_id = get_application_response.json()["applications"][asset]["applicationID"]
    headers = {
        "authorization": crm_token
    }
    return requests.get(base_url + f"/onboarding/api/v1/admin/opportunity/getOppByAppId/{application_id}",
                        headers=headers)






# Forward Action Fund
def forward_action_fund(base_url, crm_token, onboarding_token, application_name,asset):
    get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name,asset)
    levant_id = get_levant_id_response.json()["levantId"]

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Application-Name": application_name,
        "productCode": "KIAN_DIGITAL_FUNDS_ASSET",
        "authorization": crm_token

    }
    payload = json.dumps(
        {

        }
    )
    return requests.put(base_url + f"/crm/api/v3/{application_name}/action/opportunity/forward-action/{levant_id}",
                        headers=headers, data=payload)





# Do Action RQ
def do_action_rq(base_url, crm_token, onboarding_token, application_name,asset):
    get_oppourtunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name,asset)
    levant_id = get_oppourtunity_id_response.json()["levantId"]

    payload = {}
    headers = {
        'authorization': crm_token,
        'authority': 'uat.kian.digital',
        'accept': 'application/json',
        'application-name': 'CRM'
    }
    if get_oppourtunity_id_response.json()["opportunityStatus"] != "WON":
        do_action_rq_response = requests.put(
            base_url + f"/crm/api/v3/KIAN_DIGITAL/action/opportunity/do-action/RQ/{levant_id}?productCode=KIAN_DIGITAL_FUNDS_ASSET",
            headers=headers, data=payload)
        if (do_action_rq_response.status_code == 200):
            get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                          application_name,asset)
            action_id = get_opportunity_response.json()["actionId"]
            while (action_id != 19) and (action_id != None):
                forward_action_fund(base_url, crm_token, onboarding_token, application_name,asset)
                get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                              application_name,asset)
                action_id = get_opportunity_response.json()["actionId"]
            return do_action_rq_response
        else:
            return do_action_rq_response
    else:
        class res:
            status_code = 200
        return res


# Finish Pipeline
def finish_pipeline(base_url, crm_token, onboarding_token, application_name,asset):
    get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name,asset)
    oppourtunity_id = get_opportunity_id_response.json()["id"]

    payload = {}
    headers = {
        'application-name': 'CRM',
        "authorization": crm_token
    }
    return requests.put(
        base_url + f"/crm/api/v3/{application_name}/action/opportunity/command/FINISH_PIPELINE/{oppourtunity_id}",
        headers=headers, data=payload)


