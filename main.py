
import sha3
import secrets
import string
from ecdsa import SigningKey, SECP256k1
from etherscan import Etherscan


def checksum_encode(addr_str):
    keccak = sha3.keccak_256()
    out = ''
    addr = addr_str.lower().replace('0x', '')
    keccak.update(addr.encode('ascii'))
    hash_addr = keccak.hexdigest()
    for i, c in enumerate(addr):
        if int(hash_addr[i], 16) >= 8:
            out += c.upper()
        else:
            out += c
    return '0x' + out


def generate_keys():
    # Based on https://github.com/vkobel/ethereum-generate-wallet/blob/master/ethereum-wallet-generator.py
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()

    keccak.update(pub)
    address = keccak.hexdigest()[24:]

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(32))  # for a 32-character password

    return {'private_key': priv.to_string().hex(),
            'pub_key': pub.hex(),
            'address': checksum_encode(address),
            'password': password}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    eth = Etherscan('F92Z14GE2DTF6PBBYY1YPHPJ438PT3P2VI')  # key in quotation marks
    i = 1
    while True:
        i += 1
        key = generate_keys()
        balance = int(eth.get_eth_balance(address=key['address']))
        print('key Nb:'+str(i) + " / balance = " + str(balance))

        if (0 != balance):
            with open("./wallets.txt", "a") as text_file:
                text_file.write('balance = ' + str(balance) + "/" + str(key) + '\n')