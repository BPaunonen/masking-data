import json
from faker import Faker

# Initialize faker object
fake = Faker()

# Function to mask data in a json
def mask_json(json_data):
    # Iterate through each key in json
    for key in json_data:
        # If the key is a string, mask the value
        if isinstance(json_data[key], str):
            json_data[key] = fake.word()
        # If the key is a dictionary, recursively call the function
        elif isinstance(json_data[key], dict):
            json_data[key] = mask_json(json_data[key])
    return json_data

# Example input json
data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "NY",
        "zip": "12345"
    }
}

# Mask the data
masked_data = mask_json(data)

# Output the masked data as json
print(json.dumps(masked_data))
