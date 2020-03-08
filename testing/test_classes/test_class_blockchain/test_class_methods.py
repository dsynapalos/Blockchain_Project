def test_class_blockchain_method_create_block_is_defined(blockchain):
    assert blockchain.create_block(1, '0')


def test_class_blockchain_method_create_block_returns_dict(blockchain):
    assert type(blockchain.create_block(1, '0')) == type({})


def test_class_blockchain_method_create_block_appends_block_to_chain(blockchain):
    assert blockchain.chain != []
