from lesson78.cloud_storage_uploader import evaluate_storage_tier


def test_return_value():
    expected_answer_list = ["HOT", "COOL", "ARCHIVE"]
    assert evaluate_storage_tier(10, 10) in expected_answer_list