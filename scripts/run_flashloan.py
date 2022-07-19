from brownie import FlashloanV2, config, network, web3
from scripts.helpful_scripts import get_account

ETHERSCAN_TX_URL = "https://kovan.etherscan.io/tx/{}"

# Factory addresses
uniswap_factory = config["networks"][network.show_active()]["uniswap_factory"]
sushiswap_factory = config["networks"][network.show_active()]["sushiswap_factory"]


#flash_Asset is the Aave borrowed token
flash_Asset = config["networks"][network.show_active()]["dai_token"]
flash_amount = web3.toWei(50, "ether") #50,000,000,000,000,000,000 wei

#swapping_pair is the asset you wish to swap with. This is not the aave borrowed token
swapping_pair = config["networks"][network.show_active()]["weth"]

def main():
    acct = get_account()
    flashloan_contract = FlashloanV2[len(FlashloanV2) - 1]


    flashloan_tx = flashloan_contract.startTransaction(
        flash_Asset, 
        flash_amount, 
        swapping_pair, 
        uniswap_factory, 
        {"from": acct, "gas_limit": 12000000, "allow_revert": True, "gas_price": 20000000000}
    )

    if network.show_active() == "kovan":
        print("You did it! View your tx here: " + ETHERSCAN_TX_URL.format(flashloan_tx.txid))
    print("Flashloan success!")
    return flashloan_contract



