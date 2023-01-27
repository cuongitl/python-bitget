from pybitget import Client

api_key = "your-api-key"
api_secret = "your-secret-key"
api_passphrase = "your-api-passphrase"

client = Client(api_key, api_secret, passphrase=api_passphrase)
result = client.mix_get_accounts(productType='UMCBL')
print(result)
