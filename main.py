from aiobotocore.session import get_session

class S2Client:
    def __init__(
        self, 
        access_key: str, 
        secret_key: str,
        endpoint_url: str,
        bucket_name: str,
        ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
            
        }
        self.bucket_name: bucket_name
        self.session: get_session()
