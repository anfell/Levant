import os

for i in range(100):
    print(f"Running test iteration {i + 1}")
    os.system('python -m pytest -v -s .\\TestOnboardingEsign')
