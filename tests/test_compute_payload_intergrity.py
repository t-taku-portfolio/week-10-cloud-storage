import pytest
from lesson78.cloud_storage_uploader import compute_payload_intergrity


def test_file_path():

    the_wrong_file_path = "wrong_path"
    result_dict = compute_payload_intergrity(the_wrong_file_path)
    assert result_dict["status"] == "ERROR" and result_dict["message"] == f"file not found: {the_wrong_file_path}"
     