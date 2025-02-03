import requests
import json



# Onboarding Functions:LV- Card Onboarding- MiddleEast
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




# Send Bank OTP
def send_bank_otp(base_url, token):
    headers = {
        "authorization": token,
    }
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.get(base_url + f"/usermgmt/api/v1/KIAN_DIGITAL/card/bank/send-otp/{application_id}", headers=headers)




# Verify Bank OTP
def verify_bank_otp(base_url, token,national_code):
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    otp = national_code[-5] + national_code[-4] + national_code[-3] + national_code[-2] + national_code[-1]
    headers = {
        "Content-Type": "application/json",
        "authorization": token,
        "mock": "true",
    }
    payload = json.dumps({
        "otp": otp
    })
    return requests.post(base_url + f"/usermgmt/api/v1/KIAN_DIGITAL/card/bank/verify-otp/{application_id}", headers=headers, data=payload)




# Fetch Sabt Ahval Data
def fetch_sabt_ahval_data(base_url, token):
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "authorization": token,
    }
    return requests.put(base_url + f"/usermgmt/api/v1/KIAN_DIGITAL/card/sabt-ahval/{application_id}", headers=headers, data=payload)




# Submit Sabt Ahval Data
def submit_sabt_ahval_data(base_url, token):
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "authorization": token,
        "ApplicationId": application_id
    }
    return requests.put(base_url + f"/usermgmt/api/v1/KIAN_DIGITAL/card/sabt-ahval/submit/{application_id}",
                         headers=headers)




# Send Additional Info
def send_additional_info(base_url, token):
    headers = {
        "Content-Type": "application/json",
        "authorization": token
    }
    payload = json.dumps({
        "businessActivityCode": "2",
        "educationCode": "54",
        "email": "test@test.com",
        "enFatherName": "ahmad",
        "enFirstName": "reza",
        "enLastName": "rezayi",
        "occupationCode": "25",
        "placeOfBirthCode": "5",
        "placeOfIssueCode": "5",
        "submitState": "NEW"
    })
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/KIAN_DIGITAL/card/additional-info/{application_id}", headers=headers, data=payload)




# Address
def address(base_url, token):
    headers = {
        "Content-Type": "application/json",
        "authorization": token
    }
    payload = json.dumps({
        "city": "41",
        "fullAddress": "آرژانتین الوند پلاک 19",
        "postalCode": "1654682123",
        "province": "52",
        "submitState": "NEW"
    })
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.put(base_url + f"/usermgmt/api/v1/KIAN_DIGITAL/card/location/{application_id}", headers=headers, data=payload)




# Upload File
def upload_file(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "authorization": token
    }
    files = [
        ("files", ("1.JPG", open("/C:/Users/Afsaneh/Desktop/1.JPG", "rb"), "application/octet-stream"))
    ]
    return requests.post(base_url + "/glusterproxy/api/v1/file/upload", headers=headers, files=files)




# Documents
def documents(base_url, token, application_name):
    upload_file_response = upload_file(base_url, token)
    documentToken = upload_file_response.json()["token"][0]
    documentName = upload_file_response.json()["name"][0]
    headers = {
        "Content-Type": "application/json",
        "authorization": token
    }
    payload = json.dumps({
        "documents": [
            {
                "documentId": documentName,
                "documentToken": documentToken,
                "documentType": "NATIONAL_CARD_FRONT",
                "submitState": "NEW"
            },
            {
                "documentId": documentName,
                "documentToken": documentToken,
                "documentType": "NATIONAL_CARD_BACK",
                "submitState": "NEW"
            },
            {
                "documentId": documentName,
                "documentToken": documentToken,
                "documentType": "SIGNATURE_IMAGE",
                "submitState": "NEW"
            }
        ],
        "nationalCardExpireDate": 1795442298000,
        "nationalCardSerial": "123465897",
        "newNationalCard": True,
        "submitState": "EDIT"
    })
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.post(base_url + f"/usermgmt/api/v1/{application_name}/card/documents/confirm/={application_id}", headers=headers,
                        data=payload)




# Contract
def contract(base_url, token, application_name):
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "authorization": token,
        "Application-Name": application_name
    }
    payload = json.dumps({
        "accepted": True,
        "acceptedDate": 0,
        "applicationId": application_id,
        "submitState": "NEW"
    })
    return requests.put(base_url + "/usermgmt/api/v1/persons/contract", headers=headers, data=payload)




# Video Caption
def video_caption(base_url, token, application_name):
    get_application_response = get_application(base_url, token)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "authorization": token,
    }
    return requests.get(base_url + f"/usermgmt/api/v1/{application_name}/card/video-caption/{application_id}", headers=headers)




# Upload Video
def upload_video(base_url, token, application_name):
    headers = {
        "Content-Type": "application/json",
        "Application-Name": application_name,
        "File-Type": "VIDEO",
        "authorization": token
    }
    files = [
        ("files", ("1.JPG", open("/C:/Users/Afsaneh/Desktop/1.JPG", "rb"), "application/octet-stream"))
    ]
    return requests.post(base_url + "/glusterproxy/api/v1/file/upload", headers=headers, files=files)




# Confirm Video
def confirm_video(base_url, token, application_name):
    upload_video_response = upload_video(base_url, token)
    videoName = upload_video_response.json()["name"][0]
    videoToken = upload_video_response.json()["token"][0]
    headers = {
        "Content-Type": "application/json",
        "authorization": token
    }
    payload = json.dumps({
        "documentId": videoName ,
        "documentToken": videoToken,
        "documentType": "CARD_VIDEO",
        "submitState": "NEW"
    })
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    return requests.post(base_url + f"/usermgmt/api/v1/{application_name}/card/upload-video/={application_id}", headers=headers,
                        data=payload)




# Submit Application
def submit_application(base_url, token, application_name):
    get_application_response = get_application(base_url, token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "Content-Type": "application/json",
        "authorization": token,
        "Application-Name": application_name
    }
    return requests.put(base_url + f"/usermgmt/api/v1/users/submit?applicationId={application_id}", headers=headers)






# Card Crm Middle east
# Get Opportunity Id By Application Id
def get_oppourtunities(base_url, crm_token, onboarding_token, application_name):
    get_application_response = get_application(base_url, onboarding_token, application_name)
    application_id = get_application_response.json()["applications"][0]["applicationID"]
    headers = {
        "accept-language": "fa",
        "authorization": crm_token,
        "application-name": "CRM"

    }
    return requests.get(base_url + f"/onboarding/api/v1/admin/opportunity/getOppByAppId/{application_id}",
                        headers=headers)





# Get Opportunity Identification
def get_opportunity_identification(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    headers = {
        "authorization": crm_token,
        "accept-language": "fa"
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}",
                        headers=headers)





# Get Additional Info(with-identification)
def get_additional_info(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    # print(get_opportunity_id_response.json())
    headers = {
        "authorization": crm_token,
        "Content-Type": "application/json",
        "accept-language": "fa"
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/with-identification/{oppourtunity_id}",
                        headers=headers)




# Download Document
def download_document(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    documentToken = get_opportunity_id_response.json()["token"]
    documentPath = get_opportunity_id_response.json()["path"]
    # print(get_opportunity_id_response.json())
    headers = {
        "authorization": crm_token,
        'X-Objects-Token': documentToken
    }
    return requests.get(base_url + f"/glusterproxy/api/v1/file/download?filename= {documentPath}",
                        headers=headers)





# Download Video
def download_video(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                     application_name)
    documentToken = get_opportunity_id_response.json()["token"]
    documentPath = get_opportunity_id_response.json()["path"]
    headers = {
        "authorization": crm_token,
        'X-Objects-Token': documentToken,
        'File-Type': 'VIDEO'
    }
    return requests.get(base_url + f"/glusterproxy/api/v1/file/download?filename={documentPath}",
                        headers=headers)





# CRM Front Static Data
def static_data(base_url, crm_token, application_name):
    headers = {
        "authorization": crm_token,
        "Content-Type": "application/json"
    }
    return requests.get(base_url + f"/crm/api/v3/{application_name}/opportunity/card/static-data/CITY",
                        headers=headers)



#Modify opp crm operator
def modify_opp_crm_operator(base_url, crm_token, onboarding_token, application_name):
    get_levant_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                   application_name)
    levant_id = get_levant_id_response.json()["levantId"]
    get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                     application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "authorization": crm_token

    }
    payload = json.dumps({
            "cardAdditionalInfoDTO": {
            "businessActivityCode": "54",
            "educationCode": "5",
            "email": "testemail@gmail.com"
        }
    })
    return requests.patch(base_url + f"/crm/api/v3/{application_name}/opportunity/modify/card/{levant_id}/{oppourtunity_id}",
                        headers=headers, data=payload)





# Put Identification
def put_identification(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_id_response.json()["id"]
    # print(get_opportunity_id_response.json())
    headers = {
        "authorization": crm_token,
        "Content-Type": "application/json",
    }
    payload = json.dumps({
        "id": "",
        "levantId": "",
        "opportunityId": "",
        "rejectTypes": [],
        "rejectDesc": None,
        "appUpdate": True,
        "nationalCardFrontStatus": "APPROVED",
        "nationalCardBackStatus": "APPROVED",
        "signatureImageStatus": "APPROVED",
        "depositaryLetterStatus": "EMPTY",
        "certificateStatus": "SUBMITTED",
        "cvStatus": "EMPTY",
        "educationCertificateStatus": "EMPTY",
        "certificateDescriptionStatus": "SUBMITTED",
        "logoStatus": "EMPTY",
        "licenseStatus": "EMPTY",
        "agentSentenceStatus": "EMPTY",
        "officialNewspaperStatus": "EMPTY",
        "statuteStatus": "EMPTY",
        "establishmentAnnouncementStatus": "EMPTY",
        "businessPermitStatus": "EMPTY",
        "signOfficersStatus": "EMPTY",
        "ownershipStatus": "EMPTY",
        "documentsStatus": "EMPTY",
        "businessDocumentsStatus": "EMPTY",
        "personalInfoStatus": "EMPTY",
        "businessInfoStatus": "EMPTY",
        "financialInfoStatus": "EMPTY",
        "facilityDetailStatus": "EMPTY",
        "guarantorsStatus": "EMPTY",
        "sanaConfirmationStatus": "EMPTY",
        "paycheckScanStatus": "EMPTY",
        "bankDraftStatus": "EMPTY",
        "leaseContractStatus": "EMPTY",
        "bankAccountPrintStatus": "EMPTY",
        "wageAssignmentStatus": "EMPTY",
        "signatureVerificationStatus": "EMPTY",
        "creditScoreStatus": "EMPTY",
        "personScoreStatus": "EMPTY",
        "contactStatus": "APPROVED",
        "businessContactStatus": "EMPTY",
        "shebaNoStatus": "EMPTY",
        "brokerageAccountStatus": "EMPTY",
        "emailStatus": "EMPTY",
        "sejamStatus": "EMPTY",
        "fetchSejamDataStatus": "EMPTY",
        "stakeHoldersStatus": "EMPTY",
        "companyStatus": "EMPTY",
        "editDocuments": False,
        "editBusinessDocuments": False,
        "editPersonalInfo": False,
        "editFinancialInfo": False,
        "editBusinessInfo": False,
        "editContact": False,
        "editBusinessContact": False,
        "editShebaNo": False,
        "editBrokerageAccount": False,
        "editEmail": False,
        "editSejam": False,
        "editable": False,
        "bourseCodesStatus": "EMPTY",
        "financialKnowledgeStatus": "EMPTY",
        "workInfoStatus": "EMPTY",
        "bankAccountsStatus": "EMPTY",
        "sejamOTPStatus": "EMPTY",
        "educationInfoStatus": "EMPTY",
        "chequeStatus": "EMPTY",
        "payrollStatus": "EMPTY",
        "accountTurnoverStatus": "EMPTY",
        "collateralOrganizationCodeStatus": "EMPTY",
        "contractStatus": "SUBMITTED",
        "kycSelfieImageStatus": "EMPTY",
        "kycVideoCaptchaStatus": "EMPTY",
        "kycSignatureImageStatus": "EMPTY",
        "cardBankOtpStatus": "APPROVED",
        "sabtAhvalStatus": "APPROVED",
        "cardAdditionalInfoStatus": "APPROVED",
        "videoStatus": "APPROVED",
        "cardDocumentDataStatus": "APPROVED",
        "stages": [
            "cardBankOtp",
            "cardSabtAhval",
            "cardAdditionalInfo",
            "cardContact",
            "cardDocuments",
            "contract",
            "cardUploadVideo"
        ],
        "documents": [
            "NATIONAL_CARD_FRONT",
            "NATIONAL_CARD_BACK",
            "BIRTH_CERTIFICATE",
            "BIRTH_CERTIFICATE_DESCRIPTION",
            "SIGNATURE_IMAGE"
        ]
    })
    return requests.put(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}",
                        headers=headers, data=payload)





# confirm_by_qc
def confirm_by_qc(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_response.json()["id"]

    headers = {
        "authorization": crm_token,
        "Content-Type": "application/json"
    }
    payload = json.dumps({})
    return requests.post(base_url + f"/crm/api/v3/{application_name}/action/opportunity/{oppourtunity_id}/confirm-by-qc",
                        headers=headers, data=payload)





# Reject By QC
def reject_by_qc(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_response.json()["id"]

    headers = {
        "authorization": crm_token,
        "Content-Type": "application/json"
    }
    payload = json.dumps(None)
    return requests.post(base_url + f"/crm/api/v3/{application_name}/action/opportunity/{oppourtunity_id}/reject-by-qcc",
                        headers=headers, data=payload)






# Check Status Action
def check_status_action(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_response.json()["id"]

    headers = {
        "authorization": crm_token,
        "application-name": application_name,
        "mockResult": "retry",
        "Content-Type": "application/json"
    }
    return requests.put(base_url + f"onboarding/api/v1/admin/actions/CARD_CHECK_STATUS/{oppourtunity_id}",
                        headers=headers)






# General Finish
def general_finish(base_url, crm_token, onboarding_token, application_name):
    get_opportunity_response = get_oppourtunities(base_url, crm_token, onboarding_token,
                                                                        application_name)
    oppourtunity_id = get_opportunity_response.json()["id"]

    headers = {
        "authorization": crm_token,
        "application-name": application_name,
        "Content-Type": "application/json"
    }
    return requests.post(
        base_url + f"/crm/api/v3/{application_name}/action/opportunity/command/GENERAL_FINISH/{oppourtunity_id}",
        headers=headers)








#
# # Submit Check Identification
# def submit_check_identification(base_url, crm_token, onboarding_token, application_name):
#     get_opportunity_id_response = get_oppourtunities(base_url, crm_token, onboarding_token,
#                                                                         application_name)
#     oppourtunity_id = get_opportunity_id_response.json()["id"]
#
#     get_opportunity_identification_response = get_opportunity_identification(base_url, crm_token, onboarding_token,
#                                                                              application_name).json()
#     get_opportunity_identification_response["bankAccountsStatus"] = "APPROVED"
#     # print(get_opportunity_identification_response)
#     headers = {
#         "authorization": crm_token,
#         "application-name": "CRM",
#         "Content-Type": "application/json"
#     }
#     payload = json.dumps(get_opportunity_identification_response)
#     return requests.put(base_url + f"/crm/api/v3/{application_name}/opportunity/identification/{oppourtunity_id}",
#                         headers=headers, data=payload)
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
#
#
# # در واقع این سرویس submit_additional_info همان تکمیل اطلاعات بوده است که در حال حاضر کار تایید نهایی راهم متاسفانه انحام میدهد
#
# # این را گذاشتم اینحا تا یادم بماند که سرویس submit_additional_info متاسفانه فرآیند را جلو میبرد با توجه به هبه دیتایی که از انبوردینک میگیرد
# # و ممکن است درست نباشد
# #  درست ترین راه این است که این سرویس زیر فراخوانی شود برای تایید نهایی
#
#
#
#
# # confirm_by_qc
# def confirm_by_qc(base_url, crm_token, onboarding_token, application_name):
#     get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                         application_name)
#     oppourtunity_id = get_opportunity_response.json()["id"]
#
#     headers = {
#         "authorization": crm_token,
#         "application-name": "CRM",
#         "Content-Type": "application/json"
#     }
#     payload = json.dumps({})
#     confirm_by_qc_response = requests.post(base_url + f"/crm/api/v3/{application_name}/action/opportunity/{oppourtunity_id}/confirm-by-qc",
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
#     if (confirm_by_qc_response.status_code == 200):
#         get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                       application_name)
#         action_id = get_opportunity_response.json()["actionId"]
#         while (action_id != 19 and (action_id != None)):
#             forward_action_fund(base_url, crm_token, onboarding_token, application_name)
#             get_opportunity_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                           application_name)
#             action_id = get_opportunity_response.json()["actionId"]
#         # identifier.insert(1,action_id)
#         return confirm_by_qc_response
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
#         # identifier.insert(1, action_id)
#         return confirm_by_qc_response
#
#
#
#
#
#
#
#
#
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
#         base_url + f"/crm/api/v3/KIAN_DIGITAL/action/opportunity/do-action/VISITING_USER/{levant_id}?productCode=KIAN_DIGITAL_FUNDS_ESIGN",
#         headers=headers, data=payload)
#
#
#
#
# # Forward Action Fund
# def forward_action_fund(base_url, crm_token, onboarding_token, application_name):
#     get_levant_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                    application_name)
#     levant_id = get_levant_id_response.json()["levantId"]
#
#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Application-Name": application_name,
#         "productCode": "KIAN_DIGITAL_FUNDS_ESIGN",
#         "authorization": crm_token
#
#     }
#     payload = json.dumps(
#         {
#
#         }
#     )
#     return requests.put(base_url + f"/crm/api/v3/{application_name}/action/opportunity/forward-action/{levant_id}",
#                         headers=headers, data=payload)
#
#
#
#
#
#
#
# # Finish Pipeline
# def finish_pipeline(base_url, crm_token, onboarding_token, application_name):
#     get_opportunity_id_response = get_oppourtunity_by_application_id(base_url, crm_token, onboarding_token,
#                                                                         application_name)
#     oppourtunity_id = get_opportunity_id_response.json()["id"]
#
#     payload = {}
#     headers = {
#         'application-name': 'CRM',
#         "authorization": crm_token
#     }
#     return requests.put(
#         base_url + f"/crm/api/v3/{application_name}/action/opportunity/command/FINISH_PIPELINE/{oppourtunity_id}",
#         headers=headers, data=payload)
#
#
