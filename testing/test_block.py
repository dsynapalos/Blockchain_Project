def test_pytest_is_working():
    assert True


def test_class_Blockchain_is_defined():
    from main import Blockchain
    assert Blockchain()


def test_class_Blockchain_method_chain_is_empty_list():
    from main import Blockchain
    x = Blockchain()
    assert x.chain == []


def test_class_Blockchain_method_create_block_is_defined():
    from main import Blockchain
    x = Blockchain()
    assert x.create_block(proof=1, previous_hash=0)
