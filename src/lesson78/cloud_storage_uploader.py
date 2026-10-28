def generate_storage_key(prefix: str, fie_path_str: str) -> str:
    """
    Normalize local file paths into standard flat cloud object keys (e.g., transforming repors/sales.csv into production-backup/2026/sales.csv).
    """

def compute_payload_intergrity(file_path_str: str) -> dict:
    """
    Reads the file safely in binary cunks and returns file siza, MD5 hash, and SHA-256 checksum.
    """

def evaluate_storage_tier(file_size_gb: float, access_frequency_days: int) -> str:
    """
    Recommends 'HOT', 'COOL', or 'ARHIVE' based on how frequently the file is accessed.
    """

def save_as_JSON(dict_obj: dict, target_dir: str) -> str:
    """
    Save resulets as a JSON-formatted file into target directory. Returns the file path where the file is placed.
    """