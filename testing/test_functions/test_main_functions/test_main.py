def test_if_main_imports_correctly():
    import main
    assert main.__name__ == "main"


def test_if_mine_block_imports():
    import main
    assert main.mine_block
