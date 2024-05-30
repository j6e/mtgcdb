import time

import pytest
from mtgcdb.db import (
    DB_GENERIC_PATH,
    clean_old_dbs,
    download_card_definitions_db,
    get_most_recent_db,
)


@pytest.mark.dependency()
def test_download_card_definitions_db():
    db_path = download_card_definitions_db()
    assert db_path.exists()


@pytest.mark.dependency(depends=["test_download_card_definitions_db"])
def test_most_recent_db():
    _old = download_card_definitions_db()
    time.sleep(1.5)
    new = download_card_definitions_db()
    new_db = get_most_recent_db()
    assert new_db is not None
    assert new_db.exists()
    assert new_db == new


@pytest.mark.dependency(depends=["test_most_recent_db"])
def test_clean_old_dbs():
    folders = sorted(DB_GENERIC_PATH.iterdir())
    new = folders[-1]
    clean_old_dbs()
    new_db = get_most_recent_db()
    assert new == new_db.parent

    now_folders = sorted(DB_GENERIC_PATH.iterdir())
    assert len(now_folders) == 1
