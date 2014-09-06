

def test_if_configuration_is_set():
    import credentials
    assert hasattr(credentials, 'POSTGRES_USERNAME')
    assert hasattr(credentials, 'POSTGRES_PASSWORD')
    assert hasattr(credentials, 'POSTGRES_DBNAME')


def test_if_test_configuration_is_set():
    import credentials
    assert hasattr(credentials, 'TEST_POSTGRES_USERNAME')
    assert hasattr(credentials, 'TEST_POSTGRES_PASSWORD')
    assert hasattr(credentials, 'TEST_POSTGRES_DBNAME')
