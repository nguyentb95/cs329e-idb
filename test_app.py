import pytest
from app import index

@pytest.fixture
def test_index():
    index()
    pass