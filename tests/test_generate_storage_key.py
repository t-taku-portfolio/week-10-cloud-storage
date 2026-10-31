from lesson78.cloud_storage_uploader import generate_storage_key


def test_path():
    the_prefix = "production-backup/2026/"
    the_local_file_path = "reports/sales.csv"
    assert_result = "production-backup/2026/sales.csv"

    the_result = generate_storage_key(the_prefix, the_local_file_path)
    assert assert_result == the_result