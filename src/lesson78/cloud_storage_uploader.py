import os
from pathlib import Path


def generate_storage_key(prefix: str, file_path_str: str) -> str:
    """
    Normalize local file paths into standard flat cloud object keys (e.g., transforming reports/sales.csv into production-backup/2026/sales.csv).
    """

    # Prefix is consisted with the structure of "<storage-account>/<container>/<folder-or-subfolder>" in Azure Blob

    file_name_str = os.path.basename(file_path_str)
    normalized_path_str = Path(prefix) / file_name_str

    # prefix size must be in 1024 characters
    if 3 <= normalized_path_str <= 1024:
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



def evaluate_storage_tier(file_size_gb: float, access_frequency_days: int) -> str:
    """
    Recommends 'HOT', 'COOL', or 'ARHIVE' based on how frequently the file is accessed.
    """

def save_as_JSON(dict_obj: dict, target_dir: str) -> str:
    """
    Save resulets as a JSON-formatted file into target directory. Returns the file path where the file is placed.
    """