from bitcoin.rpc import RawProxy

# Create a connection to local Bitcoin Core node
p = RawProxy()

TX_ID = input("Iveskite transakcijos ID:")
# TX_ID = 'd0bd3560694a1c2db52b8411b7a6d6557fde298528b97b30c27271f32c8abd5b'
try:

    raw_tx = p.getrawtransaction(TX_ID)
    decoded_tx = p.decoderawtransaction(raw_tx)

    output_value = sum([i['value'] for i in decoded_tx['vout']])

    # raw_tx_input = p.getrawtransaction(decoded_tx['vin'])

    input_value = 0
    for vin in decoded_tx['vin']:
        vin_TX_ID = vin['txid']
        vin_vout = vin['vout']

        vin_tx = p.getrawtransaction(vin_TX_ID)
        decoded_vin_tx = p.decoderawtransaction(vin_tx)
        input_value += decoded_vin_tx['vout'][vin_vout]['value']

    # raw_tx_input_id = decoded_tx['vin'][0]['vout']
    # decoded_tx_input = p.decoderawtransaction(raw_tx_input)
    # input_value = decoded_tx_input['vout'][raw_tx_input_id]['value']

    # print(decoded_tx['vin'])
    print(output_value, input_value)
    TX_FEE = input_value-output_value
    print(f"Transaction's {TX_ID} fee was {TX_FEE} BTC.")
except ValueError:
    print(ValueError)



# MOST EXPENSIVE TRANSACTION
# OUTPUT: 94504.03465148 INPUT: 94504.10000000
# Transaction's 4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d fee was 0.06534852 BTC.