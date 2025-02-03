import subprocess


def purchase(product,asset_number, current_path):
    if asset_number == 0:
        print(subprocess.run(
            ['pytest', '-v', '-s', f"{current_path}/KianDigitalFundsV3Esign/test_01_users_onboarding_esign_kd.py",
             "--productName", f"{product}"], stdout=subprocess.PIPE).stdout.decode(
            'utf-8'))
        print(subprocess.run(
            ['pytest', '-v', '-s', f"{current_path}/KianDigitalFundsV3Esign/test_02_users_crm_esign_kd.py"],
            stdout=subprocess.PIPE).stdout.decode('utf-8'))
    elif asset_number > 0:
        print(subprocess.run(
            ['pytest', '-v', '-s', f"{current_path}/Kian_Digital_Funds_Asset/test_01_users_onboarding_esign_kd.py",
             "--productName", f"{product}", "--asset", str(asset_number)],
            stdout=subprocess.PIPE).stdout.decode('utf-8'))
        print(subprocess.run(
            ['pytest', '-v', '-s', f"{current_path}/Kian_Digital_Funds_Asset/test_02_users_crm_esign_kd.py",
             "--asset", str(asset_number)], stdout=subprocess.PIPE).stdout.decode('utf-8'))