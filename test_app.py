import pytest
import unittest
import app


class Testing(unittest.TestCase):
    @pytest.fixture
    def test_index(self):
        assert app