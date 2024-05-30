import pytest
from mtgcdb import MTGCDB


@pytest.fixture
def mtgcdb():
    return MTGCDB()


def test_get_card_by_name(mtgcdb):
    card = mtgcdb.get_card_by_name("Snapcaster Mage")
    assert card is not None
    assert card.name == "Snapcaster Mage"

    card = mtgcdb.get_card_by_name("Snapcaster Mage", set_code="ISD")
    assert card is not None
    assert card.name == "Snapcaster Mage"

    card = mtgcdb.get_card_by_name("Fable of the Mirror-Breaker")
    assert card is not None
    assert card.name == "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki"

    card = mtgcdb.get_card_by_name("Fable of the Mirror-Breaker", set_code="NEO")
    assert card is not None
    assert card.name == "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki"

    card = mtgcdb.get_card_by_name(
        "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki", set_code="NEO"
    )
    assert card is not None
    assert card.name == "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki"


def test_card_by_face_name(mtgcdb):
    card = mtgcdb.get_card_by_face_name("Fable of the Mirror-Breaker")
    assert card is not None
    assert card.faceName == "Fable of the Mirror-Breaker"

    card = mtgcdb.get_card_by_face_name("Fable of the Mirror-Breaker", set_code="NEO")
    assert card is not None
    assert card.faceName == "Fable of the Mirror-Breaker"


def test_get_cards_by_names(mtgcdb):
    cards = mtgcdb.get_cards_by_names(
        ["Snapcaster Mage", "Fable of the Mirror-Breaker"]
    )
    assert len(cards) == 2
    sorted(cards, key=lambda x: x.name)
    assert cards[0].name == "Snapcaster Mage"
    assert cards[1].name == "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki"


def test_get_cards_by_set_code(mtgcdb):
    cards = mtgcdb.get_cards_by_set_code("NEO")
    assert len(cards) > 200
    for card in cards:
        assert card.setCode == "NEO"
