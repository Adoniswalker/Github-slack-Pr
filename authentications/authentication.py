import os
import time

import jwt
from cryptography.hazmat.backends import default_backend


def authenticate():
    cert_bytes = os.environ.get("GITHUB_PRIVATE_KEY").encode()
    private_key = default_backend().load_pem_private_key(cert_bytes, None)
    time_since_epoch_in_seconds = int(time.time())

    payload = {
        # issued at time
        'iat': time_since_epoch_in_seconds,
        # JWT expiration time (10 minute maximum)
        'exp': time_since_epoch_in_seconds + (10 * 60),
        # GitHub App's identifier
        'iss': os.environ.get("GITHUB_ISS")
    }
    test_jwt = jwt.encode(payload, private_key, algorithm='RS256')
    headers = {"Authorization": "Bearer {}".format(test_jwt.decode()),
               "Accept": "application/vnd.github.machine-man-preview+json"}

    return headers


authenticate()
