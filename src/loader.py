import boto3
from boto3.s3.transfer import TransferConfig
from botocore.client import ClientError


def upload_stock_data_to_s3(file_path: str, s3_bucket_name: str, key_name: str) -> None:
    try:
        s3_client = boto3.client("s3")

        transfer_config = TransferConfig(
            multipart_threshold=1024 * 1024 * 20,
            max_concurrency=4,
            multipart_chunksize=1024 * 1024 * 20,
            use_threads=True,
        )

        with open(file_path, "rb") as f:
            response = s3_client.upload_fileobj(
                Bucket=s3_bucket_name, Key=key_name, Fileobj=f, Config=transfer_config
            )

        print(f"✅ Data uploaded successfully to S3 bucket: {s3_bucket_name}")

    except ClientError as e:
        raise e


if __name__ == "__main__":
    upload_stock_data_to_s3(
        "data/SAN.MC_2026-08-07.parquet", "my-s3-bucket-name", "2026-08-07.parquet"
    )
