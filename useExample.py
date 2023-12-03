from packageClient.client import Client

client_1 = Client("MDNTEC", "Nicolas", "123456789", True)

print(client_1)
client_1.updatePhone("024681012")
print(client_1)
status = client_1.seeClientStatus()
print(f"Client status: {status}")