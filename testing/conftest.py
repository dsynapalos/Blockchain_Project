import pytest
@pytest.fixture()
def blockchain():
    from main import Blockchain
    blockchain = Blockchain()
    return blockchain