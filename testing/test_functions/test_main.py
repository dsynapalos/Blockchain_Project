def test_if_file_is_run_directly():
    import main
    assert main.__name__ == "main"
