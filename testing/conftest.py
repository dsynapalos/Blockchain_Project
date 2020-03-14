import pytest


@pytest.fixture()
def blockchain():
    from main import Blockchain
    blockchain = Blockchain()
    return blockchain


@pytest.fixture()
def mine_block():
    from main import mine_block
    block = mine_block()
    return block
