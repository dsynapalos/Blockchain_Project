import pytest


@pytest.fixture()
def blockchain():
    from main import Blockchain
    blockchain = Blockchain()
    return blockchain


def test_class_Blockchain_method_chain_is_defined(blockchain):
    blockchain.chain


def test_class_Blockchain_method_chain_is_empty_list(blockchain):
    assert blockchain.chain == []


def test_class_Blockchain_method_create_block_is_defined(blockchain):
    blockchain.create_block(1, '0')


def test_class_Blockchain_method_create_block_has_defaul_arguments(blockchain):
    assert blockchain.create_block()
