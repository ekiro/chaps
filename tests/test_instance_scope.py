from haps.scopes.instance import InstanceScope


def test_get_object(some_class):
    some_instance = InstanceScope().get_object(some_class)
    assert isinstance(some_instance, some_class)


def test_get_multiple_objects(some_class):
    scope = InstanceScope()

    objects = {scope.get_object(some_class) for _ in range(100)}
    assert all(isinstance(o, some_class) for o in objects)
    assert len({id(o) for o in objects}) == 100
