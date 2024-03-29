import pytest

from lib.multihost import TopologyDomain


def test_topology_domain__init():
    obj = TopologyDomain('test', master=1, client=1)

    assert obj.type == 'test'
    assert obj.roles == {'master': 1, 'client': 1}


def test_topology_domain__get():
    obj = TopologyDomain('test', master=1, client=1)

    assert obj.get('master') == 1
    assert obj.get('client') == 1

    with pytest.raises(KeyError):
        obj.get('unknown')


def test_topology_domain__describe():
    obj = TopologyDomain('test', master=1, client=1)
    expected = {'type': 'test', 'hosts': {'master': 1, 'client': 1}}

    assert obj.describe() == expected


def test_topology_domain__str():
    obj = TopologyDomain('test', master=1, client=1)

    assert str(obj) == str(obj.describe())


def test_topology_domain__contains():
    obj = TopologyDomain('test', master=1, client=1)

    assert 'master' in obj
    assert 'client' in obj
    assert 'unknown' not in obj


def test_topology_domain__eq():
    obj1 = TopologyDomain('test', master=1, client=1)
    obj2 = TopologyDomain('test', master=1, client=1)
    obj3 = TopologyDomain('test', master=1, client=2)

    assert obj1 == obj2
    assert not obj1 == obj3
    assert not obj2 == obj3


def test_topology_domain__ne():
    obj1 = TopologyDomain('test', master=1, client=1)
    obj2 = TopologyDomain('test', master=1, client=1)
    obj3 = TopologyDomain('test', master=1, client=2)

    assert not obj1 != obj2
    assert obj1 != obj3
    assert obj2 != obj3


def test_topology_domain__le():
    obj1 = TopologyDomain('test', master=1, client=1)
    obj2 = TopologyDomain('test', master=1, client=1)
    obj3 = TopologyDomain('test', master=1, client=2)
    obj4 = TopologyDomain('test', master=1)
    obj5 = TopologyDomain('diff', master=1, client=2)

    assert obj1 <= obj2
    assert obj1 <= obj3
    assert not obj1 <= obj4
    assert not obj1 <= obj5
