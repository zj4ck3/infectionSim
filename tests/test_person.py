
import pytest
from person import Person

@pytest.fixture
def person():
    return Person("healthy")


@pytest.mark.parametrize("status, expected_id, color", [
    ("healthy", 1, (0, 0, 255)),
    ("sick", 2, (255, 0, 0)),
    ("carrier", 3, (255, 255, 0)),
    ("vaccinated", 4, (0, 255, 0)),
])
def test_change_status(person, status, expected_id, color):
    person.change_status(status)
    assert person.status == status
    assert person.id == expected_id
    assert person.color == color

    if person.status in ["sick", "carrier"]:
        assert person.days == 0


def test_invalid_status(person):
    with pytest.raises(ValueError, match="invalid status"):
        person.change_status("invalid_status")
