email = ["ali@gmail.com", "sara@yahoo.com", "ali@gmail.com", "ahmed@gmail.com", "sara@yahoo.com", "zain@hotmail.com"]
unique = set()
for address in email:
    if address not in unique:
        unique.add(address)
print("Unique mails: ", unique)