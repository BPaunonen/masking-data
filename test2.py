import json
from faker import Faker

fake = Faker()

# Sample JSON data
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "address": {
        "street_name": "Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}

# Function to mask the data
def mask_data(data):
    masked_data = data.copy()
    masked_data["first_name"] = fake.first_name()
    masked_data["last_name"] = fake.last_name()
    masked_data["email"] = fake.email()
    masked_data["address"]["street_name"] = fake.street_name()
    masked_data["address"]["city"] = fake.city()
    masked_data["address"]["zip"] = fake.zipcode()
    return masked_data

# Mask the data
masked_data = mask_data(data)

# Output the masked data as JSON
print(json.dumps(masked_data, indent=4))
