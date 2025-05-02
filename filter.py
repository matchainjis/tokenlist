import json

# List of allowed contract addresses
allowed_addresses = {
    "0xB2174052dd2F3FCAB9Ba622F2e04FBEA13fc0dFC",  # LOL
    "0x50fBAA0ACD30055B2376289b93AA8558630fDa72",  # OVM
    "0x33930C6b365EdB83e60ba80CB1c8445511862762",  # EGG
    "0x1F294E3B71189dAD7dce235d6FAFBC845C7CD177",  # TOX
    "0xb49ed45d594aB849C46e01eba11C794d955A2EaD",  # CDARI
    "0x2CaD7C4F05B3ec45D3d8dFb284fd73ea7b89792d",  # Don't FOMO
    "0xF6D90c6BC676eF3bF40697BC45a4D869BAa20667",  # Miner Drop
    "0xA625f0Efc6f9cba33233A9c9B2AE36AE716a370e",  # Inca Swap
    "0x0f04c0E43dc436A375893F3F5e2D48dB7BC2Da67",  # Matchain Banana
    "0xA88B1C28fE2994fEe38758b963E1507c817CbC71",  # Matchain x PSG Points
}

# Load your original JSON
with open('tokenlist.json', 'r') as f:
    tokens = json.load(f)

# Filter to only allowed addresses
filtered_tokens = [token for token in tokens if token['address'].lower() in {addr.lower() for addr in allowed_addresses}]

# Save the filtered result
with open('filtered_tokens.json', 'w') as f:
    json.dump(filtered_tokens, f, indent=2)

print(f"Done! Shortlisted {len(filtered_tokens)} tokens.")
