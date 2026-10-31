import hashlib
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
    Reads the file safely in binary chunks and returns file siza, MD5 hash, and SHA-256 checksum.
    """

    file_path = Path(file_path_str)
    if not file_path.exists():
        return {
            "status" : "ERROR",
            "message" : f"file not found: {file_path_str}"
        }

    md5_hasher = hashlib.md5(usedforsecurity= False)
    sha256_hasher =hashlib.sha224(usedforsecurity= False)

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

def save_as_JSON(dict_obj: dict, target_dir: str) -> str:
    """
    Save resulets as a JSON-formatted file into target directory. Returns the file path where the file is placed.
    """