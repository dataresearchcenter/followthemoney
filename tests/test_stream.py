from followthemoney.dataset.dataset import Dataset
from followthemoney.statement.entity import StatementEntity
from followthemoney.stream import StreamEntity


EXAMPLE = {
    "id": "jane",
    "schema": "Person",
    "properties": {"name": ["Jane Doe"], "birthDate": ["1976"]},
}


def test_stream_entity():
    se = StreamEntity.from_dict(EXAMPLE)
    assert se.schema.name == "Person"
    assert se.id == "jane"
    assert se.caption == "Jane Doe"
    assert se.datasets == set()
    exported = se.to_dict()
    assert exported == {
        "id": "jane",
        "caption": "Jane Doe",
        "schema": "Person",
        "properties": {"name": ["Jane Doe"], "birthDate": ["1976"]},
        "referents": [],
        "datasets": [],
        "target": False,
    }

    # with dataset
    data = {**EXAMPLE, **{"datasets": ["test"]}}
    se = StreamEntity.from_dict(data)
    assert se.datasets == {"test"}

    # StatementEntity -> StreamEntity
    ds = Dataset({"name": "test", "title": "Test"})
    sp = StatementEntity.from_data(ds, EXAMPLE)
    se = StreamEntity.from_dict(sp.to_dict())
    assert sp.id == se.id == "jane"
    assert sp.datasets == se.datasets == {"test"}

    # StreamEntity -> StatementEntity
    data = {**EXAMPLE, **{"datasets": ["test"]}}
    se = StreamEntity.from_dict(data)
    sp = StatementEntity.from_data(ds, se.to_dict())
    assert sp.id == se.id == "jane"
    assert sp.datasets == se.datasets == {"test"}
