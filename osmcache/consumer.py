def consume_item(item):
    a = item.to_sqlalchemy_model()
    print a
    print a.id