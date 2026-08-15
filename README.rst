================
pytest-fixturize
================

.. image:: https://img.shields.io/pypi/v/pytest-fixturize.svg
    :target: https://pypi.org/project/pytest-fixturize
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-fixturize.svg
    :target: https://pypi.org/project/pytest-fixturize
    :alt: Python versions

.. image:: https://github.com/krigar1184/pytest-fixturize/actions/workflows/main.yml/badge.svg
    :target: https://github.com/krigar1184/pytest-fixturize/actions/workflows/main.yml
    :alt: See Build Status on GitHub Actions

This plugin is intended to provide arbitrary attributes as `pytest` fixtures.

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install "pytest-fixturize" via `pip`_ from `PyPI`_::

    $ pip install pytest-fixturize


Usage
-----

.. code-block:: python
   import pytest

    class MyClass:
      a: int = 1
      b: str = "pewpew"


    @fixturize
    @pytest.fixture
    def myfixture():
        return MyClass()


    @pytest.mark.parametrize(("myfixture__a", "myfixture__b"), [2, "powpow"])
    def test_my_class(myfixture):
        assert myfixture.a == 2
        assert myfixture.b == "powpow"

Methods and underscore/dunder attributes are not fixturized by default.

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-fixturize" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: https://opensource.org/licenses/MIT
.. _`BSD-3`: https://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: https://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: https://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/krigar1184/pytest-fixturize/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
