from bitcoin.rpc import RawProxy
import hashlib
import binascii

# Create a connection to local Bitcoin Core node


def little_endian(string, number=False):
    if number:
        string = hex(string)[2:]

    arr = list(string)

    for i in range(0, len(arr), 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    arr = ''.join(arr)

    return arr[::-1]

p = RawProxy()
# block_hash = '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'
block_hash = input('Input block hash to confirm')

block_header = p.getblockheader(block_hash)

version = little_endian(str(block_header['versionHex']))
prev_block_hash = little_endian(str(block_header['previousblockhash']))
merkle = little_endian(str(block_header['merkleroot']))
timestamp = little_endian(block_header['time'], number=True)
bits = little_endian(str(block_header['bits']))
nonce = little_endian(block_header['nonce'], number=True)

header_hex = (version + prev_block_hash + merkle + timestamp + bits + nonce)

header = binascii.unhexlify(header_hex)


'''
STEPS
1. string to binary string
2. hash binary string and convert to binary
3. hash again and convert to hex
4. little endian that found hex
'''
hash_object = hashlib.sha256(hashlib.sha256(header).digest()).hexdigest()
final_hashed = little_endian(hash_object)


print(little_endian(hash_object))
print(block_header['hash'])
if block_header['hash'] == final_hashed:
    print('Block header hash and calculated hash of header parameters match!')
else:
    print("Hashes are different.")
