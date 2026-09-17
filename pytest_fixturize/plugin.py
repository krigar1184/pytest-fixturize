import pytest


def fixturize(obj: object):
    return obj


def pytest_addhooks(pluginmanager: pytest.PytestPluginManager):
    from pytest_fixturize import hooks
    pluginmanager.add_hookspecs(hooks)
