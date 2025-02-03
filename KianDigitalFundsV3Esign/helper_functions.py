import requests
import json





# Onboarding Functions:Onboarding Esign for Create Funds on Kian Digital
# Get Application
def get_application(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
    }

    return requests.get(base_url + "/usermgmt/api/v1/onboarding/home2", headers=headers)




# Start Application
def start_application(base_url, token, application_name, national_code,product_name):
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





# Send OTP Fetch Sejam Data
def send_otp_fetch_sejam_data(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true"
    }
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/sjm/resendKyc/{application_id}", headers=headers)




# Fetch Data From Sejam
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





# Confirm Fetch data From Sejam
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
    return requests.post(base_url + f"/usermgmt/api/v1/sjm/fetchDataFromSejam/confirm/{application_id}",
                         headers=headers)





# Send Esign OTP
def send_esign_otp(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token
    }
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/esign/sendOTP/{application_id}", headers=headers)





# Verify Esign OTP
def verify_esign_otp(base_url, token, application_name, national_code):
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




# Submit Application
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
    return requests.put(base_url + f"/usermgmt/api/v1/users/submit?applicationId={application_id}", headers=headers,
                        data=payload)








# CRM Functions:Esign
# Get Opportunity Id By Application Id
def get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token, application_name):
    get_application_response = get_application(base_url, onboarding_token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "authorization": crm_token
    }
    return requests.get(base_url + f"/onboarding/api/v1/admin/opportunity/getOppByAppId/{application_id}",
                        headers=headers)




# Do Action RQ
def do_action_rq(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]

    payload = {}
    headers = {
        'authorization': crm_token,
        'authority': 'uat.kian.digital',
        'accept': 'application/json',
        'application-name': 'CRM'
    }
    return requests.put(
        base_url + f"/crm/api/v3/KIAN_DIGITAL/action/opportunity/do-action/RQ/{levant_id}?productCode=KIAN_DIGITAL_FUNDS_ESIGN",
        headers=headers, data=payload)





# Get Opportunity Identification
def get_opportunity_identification(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    headers = {
        "authorization": crm_token
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}",
                        headers=headers)





# Submit Check Identification
def submit_check_identification(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]

    get_opportunity_identification_response = get_opportunity_identification(base_url, crm_token, onboarding_token,
                                                                             application_name).json()
    get_opportunity_identification_response["bankAccountsStatus"] = "APPROVED"
    # print(get_opportunity_identification_response)
    headers = {
        "authorization": crm_token,
        "application-name": "CRM",
        "Content-Type": "application/json"
    }
    payload = json.dumps(get_opportunity_identification_response)
    return requests.put(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}",
                        headers=headers, data=payload)





# Get Additional Info
def get_additional_info(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    # print(get_opportunity_id_response.json())
    headers = {
        "authorization": crm_token,
        "application-name": "CRM",
        "Content-Type": "application/json"
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/with-identification/{oppourtunity_id}",
                        headers=headers)






# Submit Additional Info
def submit_additional_info(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_response.json()["id"]

    headers = {
        "authorization": crm_token,
        "application-name": "CRM",
        "Content-Type": "application/json"
    }
    payload = json.dumps(get_additional_info(base_url, crm_token, onboarding_token, application_name).json())
    submit_additional_info_response = requests.put(base_url + f"/crm/api/v3/{application_name}/party/additional-info/{oppourtunity_id}",
                        headers=headers, data=payload)

    # get_additional_info_response = get_additional_info(base_url, crm_token, onboarding_token, application_name).json()

    # # Extract and print the desired fields
    # identifier = [
    #     {
    #         "Mobile Phone": get_additional_info_response["mobilePhone"],
    #         "First Name": get_additional_info_response["firstName"],
    #         "Last Name": get_additional_info_response["lastName"],
    #         "National Code": get_additional_info_response["nationalCode"]
    #     }
    # ]
    if (submit_additional_info_response.status_code == 200):
        get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                      application_name)
        action_id = get_opportunity_response.json()["actionId"]
        while (action_id != 19 and (action_id != None)):
            forward_action_fund(base_url, crm_token, onboarding_token, application_name)
            get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                          application_name)
            action_id = get_opportunity_response.json()["actionId"]
        # identifier.insert(1,action_id)
        return submit_additional_info_response
    else:
        # visiting_user(base_url, crm_token, onboarding_token, application_name)
        # get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
        #                                                               application_name)
        # action_id = get_opportunity_response.json()["actionId"]
        # while action_id != 19:
        #     forward_action_fund(base_url, crm_token, onboarding_token, application_name)
        #     get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
        #                                                                   application_name)
        #     action_id = get_opportunity_response.json()["actionId"]
        # # identifier.insert(1, action_id)
        return submit_additional_info_response



# در واقع این سرویس submit_additional_info همان تکمیل اطلاعات بوده است که در حال حاضر کار تایید نهایی راهم متاسفانه انحام میدهد

# این را گذاشتم اینحا تا یادم بماند که سرویس submit_additional_info متاسفانه فرآیند را جلو میبرد با توجه به هبه دیتایی که از انبوردینک میگیرد
# و ممکن است درست نباشد
#  درست ترین راه این است که این سرویس زیر فراخوانی شود برای تایید نهایی




# confirm_by_qc
def confirm_by_qc(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_response.json()["id"]

    headers = {
        "authorization": crm_token,
        "application-name": "CRM",
        "Content-Type": "application/json"
    }
    payload = json.dumps({})
    confirm_by_qc_response = requests.post(base_url + f"/crm/api/v3/{application_name}/action/opportunity/{oppourtunity_id}/confirm-by-qc",
                        headers=headers, data=payload)

    # get_additional_info_response = get_additional_info(base_url, crm_token, onboarding_token, application_name).json()

    # # Extract and print the desired fields
    # identifier = [
    #     {
    #         "Mobile Phone": get_additional_info_response["mobilePhone"],
    #         "First Name": get_additional_info_response["firstName"],
    #         "Last Name": get_additional_info_response["lastName"],
    #         "National Code": get_additional_info_response["nationalCode"]
    #     }
    # ]
    if (confirm_by_qc_response.status_code == 200):
        get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                      application_name)
        action_id = get_opportunity_response.json()["actionId"]
        while (action_id != 19 and (action_id != None)):
            forward_action_fund(base_url, crm_token, onboarding_token, application_name)
            get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                          application_name)
            action_id = get_opportunity_response.json()["actionId"]
        # identifier.insert(1,action_id)
        return confirm_by_qc_response
    else:
        # visiting_user(base_url, crm_token, onboarding_token, application_name)
        # get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
        #                                                               application_name)
        # action_id = get_opportunity_response.json()["actionId"]
        # while action_id != 19:
        #     forward_action_fund(base_url, crm_token, onboarding_token, application_name)
        #     get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
        #                                                                   application_name)
        #     action_id = get_opportunity_response.json()["actionId"]
        # identifier.insert(1, action_id)
        return confirm_by_qc_response











# Visiting User
def visiting_user(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]

    payload = {}
    headers = {
        'authorization': crm_token,
        'authority': 'uat.kian.digital',
        'accept': 'application/json',
        'application-name': 'CRM'
    }
    return requests.put(
        base_url + f"/crm/api/v3/KIAN_DIGITAL/action/opportunity/do-action/VISITING_USER/{levant_id}?productCode=KIAN_DIGITAL_FUNDS_ESIGN",
        headers=headers, data=payload)




# Forward Action Fund
def forward_action_fund(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Application-Name": application_name,
        "productCode": "KIAN_DIGITAL_FUNDS_ESIGN",
        "authorization": crm_token

    }
    payload = json.dumps(
        {

        }
    )
    return requests.put(base_url + f"/crm/api/v3/{application_name}/action/opportunity/forward-action/{levant_id}",
                        headers=headers, data=payload)







# Finish Pipeline
def finish_pipeline(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]

    payload = {}
    headers = {
        'application-name': 'CRM',
        "authorization": crm_token
    }
    return requests.put(
        base_url + f"/crm/api/v3/{application_name}/action/opportunity/command/FINISH_PIPELINE/{oppourtunity_id}",
        headers=headers, data=payload)


