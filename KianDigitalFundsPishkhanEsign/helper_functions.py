import requests
import json





# Onboarding Functions: Onboarding Kian Digital Office_Pishkhan



# User Applications
def user_applications(base_url, token, application_name, national_code):
    headers = {
        "Application_Name": application_name,
        "authorization": token
    }
    return  requests.get(base_url + f"/usermgmt/api/v1/office/user-applications/{national_code}", headers=headers)





#Sign up Send otp
def sign_up_send_otp(base_url, token, application_name, mobile_number):
    headers = {
        "Application_Name": application_name,
        "authorization": token
    }
    return requests.put(base_url + f"/usermgmt//api/v1/office/signup/{mobile_number}/send-otp", headers=headers)





#Validate Otp
def validate_otp(base_url, token, application_name, otp, mobile_number):
    otp = 9 + mobile_number[-4] + mobile_number[-3] + mobile_number[-2] + mobile_number[-1]
    headers = {
        "Application_Name": application_name,
        "authorization": token
    }
    payload = json.dumps(
        {

        }
    )
    return requests.put(base_url + f"/usermgmt/api/v1/office/signup/{mobile_number}/{otp}/validate-otp", headers=headers, data=payload)






# Start Application
def start_application(base_url, token, application_name, national_code, product_name, mobile_number):
    headers = {
        "Content-Type": "application/json",
        "application-name": application_name,
        "authorization": token,
        "mock": "true",
        "mockResult": "Sejami"
    }
    payload = json.dumps({
        "productGroupCode": product_name,
        "uniqueIdentifier": national_code,
        "mobileNumber": mobile_number,
        "extraDataSet": [
            {
                "key": "VERSION",
                "value": "V3"
            },
            {
                "key": "AGENT",
                "value": "KD_PISHKHAN"
            }
        ]
    })

    return requests.post(base_url + "/usermgmt/api/v1/office/onboarding/start", headers=headers, data=payload)







# Send OTP Fetch Sejam Data
def send_profiling_otp(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true"
    }
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/office/sjm/profiling-otp/{application_id}", headers=headers)








# Fetch Data From Sejam
def fetch_data_from_sejam(base_url, token, application_name, phone_number):
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
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
    return requests.post(base_url + "/usermgmt/api/v1/office/sjm/fetchDataFromSejam", headers=headers, data=payload)






#Preview Fetch Data From Sejam
def test_fetch_data_from_sejam_preview(base_url, token, application_name):
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Applicstion_Name": application_name,
        "authorization": token
    }
    return requests.get(base_url + f"/usermgmt/api/v1/office/sjm/fetchDataFromSejam/preview/{application_id}", headers=headers)







# Confirm Fetch data From Sejam
def confirm_fetch_data_from_sejam(base_url, token, application_name, phone_number):
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true",
        "sejamiMobile": phone_number,
        "ApplicationId": application_id
    }
    return requests.post(base_url + f"/usermgmt/api/v1/office/sjm/fetchDataFromSejam/confirm/{application_id}", headers=headers)




#Get My Forms
def get_my_forms(base_url, token, application_name):
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Application_Name": application_name,
        "authorization": token
    }
    return requests.get(base_url + f"/usermgmt/api/v1/office/form/KIAN_DIGITAL_FUNDS_ASSET/getMyForms/{application_id}", headers= headers)







#Get My Forms
def form_preview(base_url, token, application_name):
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    get_my_forms_response = get_my_forms(base_url, token, application_name)
    form_id = get_my_forms_response.json()[0]["id"]

    headers = {
        "Application_Name": application_name,
        "authorization": token
    }
    return requests.get(base_url + f"/usermgmt/api/v1/office/form/{form_id}/{application_id}/pdf", headers= headers)






# Send Esign OTP
def send_esign_otp(base_url, token, application_name):
    headers = {
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true"
    }
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/office/esign/sendOTP/{application_id}", headers=headers)







# Verify Esign OTP
def verify_esign_otp(base_url, token, application_name, national_code):
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    otp = national_code[-5] + national_code[-4] + national_code[-3] + national_code[-2] + national_code[-1]
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token,
        "mock": "true"
    }
    payload = json.dumps(
        {
            "applicationId": application_id,
            "otp": otp
        }
    )
    return requests.post(base_url + "/usermgmt/api/v1/office/esign/verify-and-kyc", headers=headers, data=payload)







# Submit Application
def submit_application(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    start_application_response = start_application(base_url, token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/office/onboarding/submit?applicationId={application_id}", headers=headers,)













# CRM Functions:Esign
# Get Opportunity Id By Application Id
def get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token, application_name):
    start_application_response = start_application(base_url, onboarding_token, application_name)
    application_id = start_application_response.json()["applications"][0]["applicationID"]

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
        base_url + f"/crm/api/v3/KIAN_DIGITAL/action/opportunity/do-action/RQ/{levant_id}?productCode=KD_PISHKHAN_ESIGN",
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




#
# # Get Additional Info
# def get_additional_info(base_url, crm_token, onboarding_token, application_name):
#     get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                         application_name)
#     oppourtunity_id = get_opportunity_id_response.json()["id"]
#     # print(get_opportunity_id_response.json())
#     headers = {
#         "authorization": crm_token,
#         "application-name": "CRM",
#         "Content-Type": "application/json"
#     }
#     return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/with-identification/{oppourtunity_id}",
#                         headers=headers)
#
#
#
#
#
#
# # Submit Additional Info
# def submit_additional_info(base_url, crm_token, onboarding_token, application_name):
#     get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                         application_name)
#     oppourtunity_id = get_opportunity_response.json()["id"]
#
#     headers = {
#         "authorization": crm_token,
#         "application-name": "CRM",
#         "Content-Type": "application/json"
#     }
#     payload = json.dumps(get_additional_info(base_url, crm_token, onboarding_token, application_name).json())
#     submit_additional_info_response = requests.put(base_url + f"/crm/api/v3/{application_name}/party/additional-info/{oppourtunity_id}",
#                         headers=headers, data=payload)
#
#     # get_additional_info_response = get_additional_info(base_url, crm_token, onboarding_token, application_name).json()
#
#     # # Extract and print the desired fields
#     # identifier = [
#     #     {
#     #         "Mobile Phone": get_additional_info_response["mobilePhone"],
#     #         "First Name": get_additional_info_response["firstName"],
#     #         "Last Name": get_additional_info_response["lastName"],
#     #         "National Code": get_additional_info_response["nationalCode"]
#     #     }
#     # ]
#     if (submit_additional_info_response.status_code == 200):
#         get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                       application_name)
#         action_id = get_opportunity_response.json()["actionId"]
#         while (action_id != 19 and (action_id != None)):
#             forward_action_fund(base_url, crm_token, onboarding_token, application_name)
#             get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                           application_name)
#             action_id = get_opportunity_response.json()["actionId"]
#         # identifier.insert(1,action_id)
#         return submit_additional_info_response
#     else:
#         # visiting_user(base_url, crm_token, onboarding_token, application_name)
#         # get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#         #                                                               application_name)
#         # action_id = get_opportunity_response.json()["actionId"]
#         # while action_id != 19:
#         #     forward_action_fund(base_url, crm_token, onboarding_token, application_name)
#         #     get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#         #                                                                   application_name)
#         #     action_id = get_opportunity_response.json()["actionId"]
#         # # identifier.insert(1, action_id)
#         return submit_additional_info_response
#


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









#
#
# # Visiting User
# def visiting_user(base_url, crm_token, onboarding_token, application_name):
#     get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                    application_name)
#     levant_id = get_levant_id_response.json()["levantId"]
#
#     payload = {}
#     headers = {
#         'authorization': crm_token,
#         'authority': 'uat.kian.digital',
#         'accept': 'application/json',
#         'application-name': 'CRM'
#     }
#     return requests.put(
#         base_url + f"/crm/api/v3/KIAN_DIGITAL/action/opportunity/do-action/VISITING_USER/{levant_id}?productCode=KD_PISHKHAN_ESIGN",
#         headers=headers, data=payload)
#





# Forward Action Funds
def forward_action_fund(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Application-Name": application_name,
        "productCode": "KD_PISHKHAN_ESIGN",
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


