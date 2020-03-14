def test_get_new_proof(blockchain):
    assert blockchain.proof_of_work(blockchain.get_previous_block()['proof'])


def test_get_previous_hash(blockchain):
    assert blockchain.hash(blockchain.get_previous_block())


def test_create_block(blockchain):
    assert blockchain.create_block(blockchain.proof_of_work(blockchain.get_previous_block()['proof']),
                                   blockchain.hash(blockchain.get_previous_block()))
