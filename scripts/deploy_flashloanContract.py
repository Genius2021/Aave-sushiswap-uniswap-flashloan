from brownie import FlashloanV2, config, network
from scripts.helpful_scripts import get_account

# AAVE_LENDING_POOL_ADDRESS_PROVIDER = "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"
ETHERSCAN_ADDRESS_URL = "https://kovan.etherscan.io/address/{}"


def main():
    """
    Deploy the `FlashloanV2` contract with `accounts[0]`.
    """

    aave_lending_pool_v2 = config["networks"][network.show_active()]["aave_lending_pool_v2"]
    uniswap_router = config["networks"][network.show_active()]["uniswap_router"]
    sushiswap_router = config["networks"][network.show_active()]["sushiswap_router"]


    acct = get_account()

    flashloan = FlashloanV2.deploy(
        aave_lending_pool_v2,
        uniswap_router,
        sushiswap_router,
        {"from": acct},
    )
    print("You did it! View your deployed contract at here: " + ETHERSCAN_ADDRESS_URL.format(flashloan.address))
    # print("flashloan Contract deployed at: ", flashloan.address)
    return flashloan
