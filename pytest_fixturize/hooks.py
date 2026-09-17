from pytest import hookspec


@hookspec
def pytest_myhook():
    breakpoint()
    pass
