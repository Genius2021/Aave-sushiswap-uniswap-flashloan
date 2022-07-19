from brownie import FlashloanV2, config, network
from scripts.helpful_scripts import get_account


asset = config["networks"][network.show_active()]["dai_token"]


def main():
    acct = get_account()
    flashloan_contract = FlashloanV2[len(FlashloanV2) - 1]

    flashloan_contract.pullTokens(asset, {"from": acct})
    print("pull successful!")



