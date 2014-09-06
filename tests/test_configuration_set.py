

def test_if_configuration_is_set():
    import credentials
    assert hasattr(credentials, 'POSTGRES_USERNAME')
    assert hasattr(credentials, 'POSTGRES_PASSWORD')
    assert hasattr(credentials, 'POSTGRES_DBNAME')
