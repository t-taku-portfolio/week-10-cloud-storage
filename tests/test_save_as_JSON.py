import pytest
from lesson78.cloud_storage_uploader import save_as_JSON


def test_save_as_JSON():
    with pytest.raises(FileNotFoundError):
        mock_obj = {
            "dummy_key" : "dummy_value"
        }
        save_as_JSON(obj_dict= mock_obj, target_dir= "incorrect_path")