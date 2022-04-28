from terra_sdk.client.lcd import LCDClient
from terra_sdk.key.mnemonic import MnemonicKey

MNEMONIC ="tragic spell bonus derive limit penalty absorb meadow summer little pill test tackle melody safe panic trash poem wise ten shoot civil owner knee"

def get_terra_address(mnemonic=MNEMONIC):
    mk = MnemonicKey(mnemonic=mnemonic)
    terra = LCDClient("https://lcd.terra.dev", "columbus-5")
    wallet = terra.wallet(mk)
    return wallet.key.acc_address
