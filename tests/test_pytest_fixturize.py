from pytest import Pytester


def test_fixturize_decorator(pytester: Pytester):
    pytester.makepyfile("""
    import pytest

    class MyClass:
        a: int = 1
        b: str = "pewpew"


    @pytest.fixture
    def myfixture():
        return fixturize(MyClass())


    #@pytest.mark.parametrize(("myfixture__a", "myfixture__b"), [2, "powpow"])
    def test_my_class(myfixture):
        assert myfixture.a == 2
        assert myfixture.b == "powpow"
    """)

    result = pytester.runpytest("-v")

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0
