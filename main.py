import jwt
import base64
from datetime import datetime
import hashlib


# Get the current timestamp in seconds
def get_current_unix_timestamp():
    return str(int(datetime.now().timestamp()))


# Convert the current Unix timestamp to a human-readable format
def get_human_readable_timestamp(timestamp):
    current_datetime = datetime.fromtimestamp(int(timestamp))
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")


# Encode the user ID with the timestamp using XOR operation
def encode_userid_with_timestamp(userid, current_unix_timestamp, secret_key):
    # Hash the timestamp and trim to 32 characters
    hashed_timestamp = hashlib.sha256((current_unix_timestamp + secret_key.decode()).encode()).hexdigest()[:32]

    # Combine the hashed timestamp with the user ID
    data = userid + "|" + hashed_timestamp
    data_bytes = data.encode()

    # Perform XOR operation
    repeated_key = secret_key * ((len(data_bytes) // len(secret_key)) + 1)
    repeated_key = repeated_key[:len(data_bytes)]
    encoded_data_bytes = bytes([a ^ b for a, b in zip(data_bytes, repeated_key)])

    # Encode the result in Base64 and return
    encoded_data = base64.b64encode(encoded_data_bytes).decode()
    return encoded_data


# Decode the XOR-encoded data
def decode_userid_timestamp(encoded_data, key):
    # Decode from Base64
    encoded_data_bytes = base64.b64decode(encoded_data.encode())

    # Perform XOR operation
    repeated_key = key * ((len(encoded_data_bytes) // len(key)) + 1)
    repeated_key = repeated_key[:len(encoded_data_bytes)]
    decoded_data_bytes = bytes([a ^ b for a, b in zip(encoded_data_bytes, repeated_key)])

    # Separate the user ID and the hashed timestamp
    decoded_data = decoded_data_bytes.decode()
    userid, hashed_timestamp = decoded_data.split("|")

    # Return the hashed timestamp
    return userid, hashed_timestamp


def main():
    userid = "23243232"
    xor_secret_key = b'generally_user_salt_or_hash_or_random_uuid_this_value_must_be_in_dbms'
    jwt_secret_key = 'yes_your_service_jwt_secret_key'

    current_unix_timesstamp = get_current_unix_timestamp()
    human_readable_timestamp = get_human_readable_timestamp(current_unix_timesstamp)

    encoded_userid_timestamp = encode_userid_with_timestamp(userid, current_unix_timesstamp, xor_secret_key)
    decoded_userid, hashed_timestamp = decode_userid_timestamp(encoded_userid_timestamp, xor_secret_key)

    jwt_token = jwt.encode({'timestamp': human_readable_timestamp, 'userid': encoded_userid_timestamp}, jwt_secret_key, algorithm='HS256')
    decoded_token = jwt.decode(jwt_token, jwt_secret_key, algorithms=['HS256'])

    print("")
    print("- Current Unix Timestamp:", current_unix_timesstamp)
    print("- Current Unix Timestamp to Human Readable:", human_readable_timestamp)
    print("")
    print("- userid:", userid)
    print("- XOR Symmetric key:", xor_secret_key)
    print("- JWT Secret key:", jwt_secret_key)
    print("")
    print("- Encoded UserID and Timestamp:", encoded_userid_timestamp)
    print("- Decoded UserID and Hashed Timestamp:", decoded_userid + "|" + hashed_timestamp)
    print("")
    print("- JWT Token:", jwt_token)
    print("- Decoded JWT:", decoded_token)

if __name__ == "__main__":
    main()
