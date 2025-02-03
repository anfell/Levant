import subprocess


def run_pipeline(index,CURRENT_PATH,productName):
    match index:
        case "11":
            # One step -> <productName> -> Onboarding - Complete
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py",
                "--productName", f"{productName}"], stdout=subprocess.PIPE).stdout.decode('utf-8'))

        case "12":
            # One step -> <productName> -> Onboarding -> Confirm Fetch Sejam
            print(subprocess.run(['pytest', '-v', '-s',
                                  f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py::test_get_application"],
                                 stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                  f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py::test_start_application"],
                                 stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                  f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py::test_send_otp_fetch_sejam_data"],
                                 stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                  f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py::test_fetch_data_from_sejam"],
                                 stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                  f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py::test_confirm_fetch_data_from_sejam"],
                                 stdout=subprocess.PIPE).stdout.decode('utf-8'))

        case "13":
            # One step -> <productName> -> only CRM - Complete
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py"],
                stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "14":
            # One step -> <productName> -> Onboarding -> CRM - Complete
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py",
                "--productName", f"{productName}"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py"],
                stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "15":
            # One step -> <productName> -> Onboarding -> CRM - Barresi Ettelaat
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py",
                "--productName", f"{productName}"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_do_action_rq"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_get_opportunity_identification"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "16":
            # One step -> <productName> -> RQ to Barresi Ettelaat
            print(subprocess.run(['pytest', '-v', '-s',
                                  f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_do_action_rq"],
                                 stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "17":
            # One step -> <productName> -> Onboarding -> CRM - Taeid Nahaei
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_submit_check_identification"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "18":
            # One step -> <productName> -> Onboarding -> CRM - Payan
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_confirm_by_qc"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))

        case "19":
            # One step -> <productName> -> Onboarding -> CRM - Purched
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_finish_pipeline"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "110":
            # One step -> <productName> -> Onboarding -> CRM -> Barresi Ettelaat -> Taeid Nahaei
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py",
                "--productName", f"{productName}"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_do_action_rq"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_get_opportunity_identification"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_submit_check_identification"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))


        case "111v":
            # One step -> <productName> -> Onboarding -> CRM -> Barresi Ettelaat -> Taeid Nahaei -> Payan
            print(subprocess.run(
                ['pytest', '-v', '-s', f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py",
                "--productName", f"{productName}"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_do_action_rq"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_get_opportunity_identification"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_submit_check_identification"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))
            print(subprocess.run(['pytest', '-v', '-s',
                                f"{CURRENT_PATH}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py::test_submit_additional_info"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8'))

