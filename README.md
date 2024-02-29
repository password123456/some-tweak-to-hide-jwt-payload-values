# some-tweak-to-hide-jwt-payload-values
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpassword123456%2Fsome-tweak-to-hide-jwt-payload-values&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

- a handful of tweaks and ideas to safeguard the JWT payload, making it futile to attempt decoding by constantly altering its value, <br> ensuring the decoded output remains unintelligible while imposing minimal performance overhead.

## What is a JWT Token?
A JSON Web Token (JWT, pronounced "jot") is a compact and URL-safe way of passing a JSON message between two parties. It's a standard, defined in RFC 7519. The token is a long string, divided into parts separated by dots. Each part is base64 URL-encoded.

What parts the token has depends on the type of the JWT: whether it's a JWS (a signed token) or a JWE (an encrypted token). If the token is signed it will have three sections: the header, the payload, and the signature. If the token is encrypted it will consist of five parts: the header, the encrypted key, the initialization vector, the ciphertext (payload), and the authentication tag. Probably the most common use case for JWTs is to utilize them as access tokens and ID tokens in OAuth and OpenID Connect flows, but they can serve different purposes as well.


## Primary Objective of this Code Snippet

This code snippet offers a tweak perspective aiming to enhance the security of the payload section when decoding JWT tokens, where the stored keys are visible in plaintext.
This code snippet provides a tweak perspective aiming to enhance the security of the payload section when decoding JWT tokens. Typically, the payload section appears in plaintext when decoded from the JWT token (base64).
The main objective is to lightly encrypt or obfuscate the payload values, making it difficult to discern their meaning. The intention is to ensure that even if someone attempts to decode the payload values, they cannot do so easily.

## userid

- The code snippet targets the key named "userid" stored in the payload section as an example.
- The choice of "userid" stems from its frequent use for user identification or authentication purposes after validating the token's validity (e.g., ensuring it has not expired).

The idea behind attempting to obscure the value of the key named "userid" is as follows:

### Encryption:

- The timestamp is hashed and then encrypted by performing bitwise XOR operation with the user ID.
- XOR operation is performed using a symmetric key.
- The resulting value is then encoded using Base64.

### Decryption:

- Encrypted data is decoded using Base64.
- Decryption is performed by XOR operation with the symmetric key.
- The original user ID and hashed timestamp are revealed in plaintext.
- The user ID part is extracted by splitting at the "|" delimiter for relevant use and purposes.

### Symmetric Key for XOR Encoding:

- Various materials can be utilized for this key.
- It could be a salt used in conventional password hashing, an arbitrary random string, a generated UUID, or any other suitable material.
- However, this key should be securely stored in the database management system (DBMS).

and..^^
```
in the example, the key is shown as { 'userid': 'random_value' },
making it apparent that it represents a user ID.

However, this is merely for illustrative purposes.

In practice, a predetermined and undisclosed name is typically used.
For example, 'a': 'changing_random_value'
```

## Notes
- This code snippet is created for educational purposes and serves as a starting point for ideas rather than being inherently secure. 
- It provides a level of security beyond plaintext visibility but does not guarantee absolute safety.

Attempting to tamper with JWT tokens generated using this method requires access to both the JWT secret key and the XOR symmetric key used to create the UserID.

# And...
- If you find this helpful, please the **"star"**:star2: to support further improvements.

# preview
```
# python3 main.py

- Current Unix Timestamp: 1709160368
- Current Unix Timestamp to Human Readable: 2024-02-29 07:46:08

- userid: 23243232
- XOR Symmetric key: b'generally_user_salt_or_hash_or_random_uuid_this_value_must_be_in_dbms'
- JWT Secret key: yes_your_service_jwt_secret_key

- Encoded UserID and Timestamp: VVZcUUFTX14FOkdEUUFpEVZfTWwKEGkLUxUKawtHOkAAW1RXDGYWQAo=
- Decoded UserID and Hashed Timestamp: 23243232|e27436b7393eb6c2fb4d5e2a508a9c5c

- JWT Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aW1lc3RhbXAiOiIyMDI0LTAyLTI5IDA3OjQ2OjA4IiwidXNlcmlkIjoiVlZaY1VVRlRYMTRGT2tkRVVVRnBFVlpmVFd3S0VHa0xVeFVLYXd0SE9rQUFXMVJYREdZV1FBbz0ifQ.bM_6cBZHdXhMZjyefr6YO5n5X51SzXjyBUEzFiBaZ7Q
- Decoded JWT: {'timestamp': '2024-02-29 07:46:08', 'userid': 'VVZcUUFTX14FOkdEUUFpEVZfTWwKEGkLUxUKawtHOkAAW1RXDGYWQAo='}


# run again
- Decoded JWT: {'timestamp': '2024-02-29 08:16:36', 'userid': 'VVZcUUFTX14FaRNAVBRpRQcORmtWRGleVUtRZlYXaBZZCgYOWGlDR10='}
- Decoded JWT: {'timestamp': '2024-02-29 08:16:51', 'userid': 'VVZcUUFTX14FZxMRVUdnEgJZEmxfRztRVUBabAsRZkdVVlJWWztGQVA='}
- Decoded JWT: {'timestamp': '2024-02-29 08:17:01', 'userid': 'VVZcUUFTX14FbxYQUkM8RVRZEmkLRWsNUBYNb1sQPREFDFYKDmYRQV4='}
- Decoded JWT: {'timestamp': '2024-02-29 08:17:09', 'userid': 'VVZcUUFTX14FbUNEVEVqEFlaTGoKQjxZBRULOlpGPUtSClALWD5GRAs='}
```

![img](https://github.com/password123456/some-tweak-to-hide-jwt-payload-values/blob/main/jwt.png)


