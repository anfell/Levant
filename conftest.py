def pytest_addoption(parser):
    parser.addoption("--productName", action="store", default="default name")
    parser.addoption("--asset", action="store", default="default name")
def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    product_name = metafunc.config.option.productName
    asset_num = metafunc.config.option.asset
    
    if 'productName' in metafunc.fixturenames and product_name is not None:
        metafunc.parametrize("productName", [product_name])
    
    if 'asset' in metafunc.fixturenames and asset_num is not None:
        metafunc.parametrize("asset", [asset_num])