import datetime
import hashlib
import json
import zoneinfo
from pathlib import Path


def generate_storage_key(prefix: str, file_path_str: str) -> str:
    """
    Normalize local file paths into standard flat cloud object keys (e.g., transforming reports/sales.csv into production-backup/2026/sales.csv).
    """

    # Prefix is consisted with the structure of "<storage-account>/<container>/<folder-or-subfolder>" in Azure Blob

    normalized_path_str = str(Path(prefix) / Path(file_path_str).name)

    # prefix size must be in 1024 characters
    if 3 <= len(normalized_path_str) <= 1024:
        return normalized_path_str



def compute_payload_intergrity(file_path_str: str) -> dict:
    """
    Reads the file safely in binary chunks and returns file size, MD5 hash, and SHA-256 checksum.
    """

    file_path = Path(file_path_str)
    if not file_path.exists():
        return {
            "status" : "ERROR",
            "message" : f"file not found: {file_path_str}"
        }

    md5_hasher = hashlib.md5(usedforsecurity= False)
    sha256_hasher = hashlib.sha224(usedforsecurity= False)

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                md5_hasher.update(chunk)
                sha256_hasher.update(chunk)

        return {
            "file_name" : file_path.name,
            "size_byte" : file_path.stat().st_size,
            "md5_etag" : md5_hasher.hexdigest(),
            "sha256" : sha256_hasher.hexdigest()
        }
    except OSError:
        return {
            "status" : "ERROR",
            "message" : f"file operation error: {file_path_str}"
        }



def evaluate_storage_tier(file_size_gb: float, access_frequency_days: int) -> str:
    """
    Recommends 'HOT', 'COOL', or 'ARHIVE' based on how frequently the file is accessed.
    """

    # the dict expresses as following scheme 
    # [tier] : {"storage" : [storage pricing per gb], "retrieval" : [retrieval pricing per gb]} 
    RATES = {
        "HOT" : {"storage" : 0.03, "retrieval" : 0.0 },
        "COOL" : {"storage" : 0.0138, "retrieval" : 0.01 },
        "ARCHIVE" : {"storage" : 0.005, "retrieval" : 0.03 }
    }

    tier_estimate = {}
    for tier, pricing in RATES.items():
        
        storage_cost = file_size_gb * pricing["storage"]
        retrieval_cost = file_size_gb * access_frequency_days * pricing["retrieval"]
        total_cost = round(storage_cost + retrieval_cost, 2)

        tier_estimate[tier] = total_cost

    return min(tier_estimate, key= lambda t: tier_estimate[t]) 



def save_as_JSON(obj_dict: dict, target_dir: str) -> str:
    """
    Save resulets as a JSON-formatted file into target directory. Returns the file path where the file is placed.
    """

    JAPAN_TOKYO = zoneinfo.ZoneInfo("Asia/Tokyo")
    timestamp = datetime.datetime.now(JAPAN_TOKYO).strftime("%Y_%m_%d")
    obj_dict["timestamp"] = timestamp

    if target_dir is None:
        target_dir = Path.cwd()
    file_path = target_dir / "storage_manifest.json"

    try:
        with open(file_path, "w") as f:
            json.dump(obj= obj_dict, fp= f, indent= 4)
    except FileNotFoundError:
        print("Target directory is not found")
        raise

    return file_path


print(f"{evaluate_storage_tier(10, 10)}")