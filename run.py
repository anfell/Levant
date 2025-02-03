import sys
import os



sys.path.append(os.getcwd())
from pipeline import run_pipeline
from purchase import purchase
from all_assets_scenario import *

CURRENT_PATH = os.getcwd()
# resultPath = os.path.join(CURRENT_PATH + "\Kian_Digital_Funds_Asset", "result.txt")
# identifierPath = os.path.join(CURRENT_PATH + "\KianDigitalFundsV3Esign", "identifiers.txt")
# f = open(identifierPath, "r")
# IDENTIFIERS = ast.literal_eval(f.read())
# f.close()
# result = f"\tNational Code: {IDENTIFIERS[0]['nationalCode']}\n \tPhone Number: {IDENTIFIERS[0]['phoneNumber']}\n"




KIAN_ETF_ASSETS = ["FIXED_INCOME","GOLD","AVA_ETF", "TRADABLE_INDEX", "FARMA", "AHANG", " GANJINEH", "SAM", "MAH_AFARID"]
PRODUCTS = {
    "1": "FIXED_INCOME",
    "2": "GOLD",
    "3": "AVA_ETF",
    "4": "TRADABLE_INDEX",
    "5": "FARMA",
    "6": "AHANG",
    "7": "GANJINEH",
    "8": "SAM",
    "9": "MAH_AFARID",
    "10": "NEDA"
}

print("\nSelect Workflow:\n")
print("\t1: One step")
print("\t2: Two step")
print("\t3: Three step")
print("\t4: Four step")



wf_index = input("\nPlease enter index: ")
while True:
        if wf_index not in ["1","2","3","4"]:
            print("Wrong index, please enter index from options")
            wf_index = input("\nPlease enter index: ")
        else:
            break

if wf_index == "1":
    print("\nSelect product:\n")
    #### Products
    print("\t1: Kian Fixed Income")
    print("\t2: Gold")
    print("\t3: Ava Etf")
    print("\t4: Tradable Index")
    print("\t5: Farma")
    print("\t6: Ahang")
    print("\t7: Ganjineh")
    print("\t8: Sam")
    print("\t9: Mah Afarid")
    print("\t10: NEDA")



    product_index = input("\nPlease enter index: ")
    while True:
        if product_index not in ["1","2","3","4","5","6","7","8","9", "10"]:
            print("Wrong index, please enter index from options")
            product_index = input("\nPlease enter index: ")
        else:
            break
    match product_index:
        case "1":
            productName = "FIXED_INCOME"
        case "2":
            productName = "GOLD"
        case "3":
            productName = "AVA_ETF"
        case "4":
            productName = "TRADABLE_INDEX"
        case "5":
            productName = "FARMA"
        case "6":
            productName = "AHANG"
        case "7":
            productName = "GANJINEH"
        case "8":
            productName = "SAM"
        case "9":
            productName = "MAH_AFARID"
        case "10":
            productName = "NEDA"



    print("Select the end of pipeline:")
    #### 01-onboarding with new identifiers
    print("\t1:  Onboarading - Complete")

    #### 02-onboarding with new identifiers
    print("\t2:  Onboarading - Confirm Fetch Sejam")

    #### 03-onlyCRM with existing identifiers
    print("\t3: \t Only CRM - Complete")

    #### 04-onboarding + crm with new identifiers
    print("\t4:  Onboarding -> CRM - Complete")

    #### 05-onboarding + crm::test_get_opportunity_identification with existing identifiers
    print("\t5:  Onboarding -> CRM - Barresi Ettelaat")

    #### 06-onlyCRM ::test_do_action_rq to barresi ettelaat with existing identifiers
    print("\t6: \t Only CRM - Barresi Ettelaat ")

    #### 07-onlyCRM::test_submit_check_identification with existing identifiers
    print("\t7: \t Only CRM - Taeid-Nahaei")

    #### 08-onlyCRM::test_submit_additional_info with existing identifiers
    print("\t8: \t Only CRM - Payan")

    #### 09-onlyCRM::test_finish_pipeline with existing identifiers
    print("\t9: \t Only CRM - Purched")

    #### 10-onboarding + crm::test_submit_check_identification with new identifiers
    print("\t10:  Onboarding -> CRM - Taeid-Nahaei")

    #### 11-onboarding + crm::test_submit_additional_info with new identifiers
    print("\t11: Onboarding -> CRM - Payan")






    pipeline_index = input("\nPlease enter index: ")
    while True:
        if pipeline_index not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            print("Wrong index, please enter index from options")
            pipeline_index = input("\nPlease enter index: ")
        else:
            break
    index = wf_index + pipeline_index
    run_pipeline(index,CURRENT_PATH,productName)
elif wf_index in ["2","3","4"]:
    user_input_products_index = []
    print("Products List:")
    print("\n\t0:  All Assets:")
    print("\n\t1:  Kian Fixed Income")
    print("\n\t2:  Gold")
    print("\n\t3:  Ava Etf")
    print("\n\t4:  Tradable Index")
    print("\n\t5:  Frama")
    print("\n\t6:  Ahang")
    print("\n\t7:  Ganjineh")
    print("\n\t8:  Sam")
    print("\n\t9:  Mah Afarid")



    #### get input
    for i in range(int(wf_index)):
        user_input_products_index.append(input(f"\nSelect product number {i + 1}: "))
        if user_input_products_index[0] == "0":
            break
        while True:
            if user_input_products_index[-1] not in list(PRODUCTS.keys()):
                user_input_products_index.pop(-1)
                print("Wrong index, please enter index from options")
                user_input_products_index.append(input(f"\nSelect product number {i + 1}: "))
            else:
                break

    while True:
        if user_input_products_index[0] == "0":
            if wf_index == "2":
                scenario = two_steps_scenario
            elif wf_index == "3":
                scenario = three_steps_scenario
            elif wf_index == "4":
                scenario = four_steps_scenario
            for user_input_products_index in scenario:
                # print(user_input_products_index[0])
                # exit(0)
                for i in range(len(user_input_products_index)):
                    print(PRODUCTS[user_input_products_index[i]])
                ETF_flag = False
                asset_number = 0
                for i in range(int(wf_index)):
                    if (ETF_flag and (PRODUCTS[user_input_products_index[i]] in KIAN_ETF_ASSETS)):
                        print("your product already purchased")
                    else:
                        if PRODUCTS[user_input_products_index[i]] in KIAN_ETF_ASSETS:
                            ETF_flag = True
                        purchase(PRODUCTS[user_input_products_index[i]], asset_number, CURRENT_PATH)
                        asset_number = asset_number + 1

            break
        else:
            ETF_flag = False
            asset_number = 0
            for i in range(int(wf_index)):
                if (ETF_flag and (PRODUCTS[user_input_products_index[i]] in KIAN_ETF_ASSETS)):
                    print("your product already purchased\n\n\n")
                else:
                    if PRODUCTS[user_input_products_index[i]] in KIAN_ETF_ASSETS:
                        ETF_flag = True
                    purchase(PRODUCTS[user_input_products_index[i]], asset_number, CURRENT_PATH)
                    asset_number = asset_number + 1
            break
