from azure.storage.blob import BlockBlobService, PublicAccess
import os

# import SAS credential
with open("cred.txt") as f:
    line = f.readline()

# create BlockBlobService
block_blob_service = BlockBlobService(account_name = "sa030802util", sas_token=line)

# print content of testutils container
generator = block_blob_service.list_blobs("testutils")
for blob in generator:
    print(blob.name)