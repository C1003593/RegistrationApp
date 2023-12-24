from storages.backends.azure_storage import AzureStorage
class AzureMediaStorage(AzureStorage):
    account_name = 'c1003593dcbs'
    account_key = 'v3gWAOAvCOxwBbsNjdKn+ebpQd7jB3JD13UsQr8kRUpCrlulIR58aPqxrESjsssuvmMXHf4o6j41+ASthcGo9w=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'c1003593dcbs'
    account_key = 'v3gWAOAvCOxwBbsNjdKn+ebpQd7jB3JD13UsQr8kRUpCrlulIR58aPqxrESjsssuvmMXHf4o6j41+ASthcGo9w=='
    azure_container = 'static'
    expiration_secs = None