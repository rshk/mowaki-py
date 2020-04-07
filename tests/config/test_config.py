from mowaki.config import Config
import pytest


class Test_load_string:

    def test_annotation_and_default(self):

        class AppConfig(Config):
            FOO: str = 'default'

        cfg = AppConfig({'FOO': 'foo'})
        assert cfg.FOO == 'foo'

    def test_annotation_only(self):

        class AppConfig(Config):
            FOO: str

        cfg = AppConfig({'FOO': 'foo'})
        assert cfg.FOO == 'foo'

    def test_default_only(self):

        class AppConfig(Config):
            FOO = 'default'

        cfg = AppConfig({'FOO': 'foo'})
        assert cfg.FOO == 'foo'


class Test_default_value:

    def test_annotation_and_default(self):

        class AppConfig(Config):
            FOO: str = 'default'

        cfg = AppConfig({})
        assert cfg.FOO == 'default'

    def test_annotation_only(self):

        class AppConfig(Config):
            FOO: str

        cfg = AppConfig({})
        assert cfg.FOO is None

    def test_default_only(self):

        class AppConfig(Config):
            FOO = 'default'

        cfg = AppConfig({})
        assert cfg.FOO == 'default'


def test_load_integer():

    class AppConfig(Config):
        FOO: int = None

    cfg = AppConfig({'FOO': '123'})
    assert cfg.FOO == 123


def test_load_boolean():

    class AppConfig(Config):
        FOO: bool = False

    cfg = AppConfig({'FOO': 'true'})
    assert cfg.FOO is True

    cfg = AppConfig({'FOO': 'false'})
    assert cfg.FOO is False


def test_accessing_non_existing_var_raises_attributeerror():

    class AppConfig(Config):
        FOO = None

    cfg = AppConfig({})

    with pytest.raises(AttributeError):
        cfg.BAR
