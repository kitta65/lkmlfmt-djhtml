import pytest

from lkmlfmt_djhtml.formatter import fmt_html, to_jinja, to_liquid
from tests import utils


@pytest.mark.parametrize(
    "liquid,jinja",
    [
        (
            '<img src="https://example.com/{{ value }}"/>',
            '<img src="https://example.com/{{ var }}{% set LKMLFMT_MARKER = 0 %}"/>',
        ),
    ],
    ids=utils.shorten,
)
def test_to_jinja(liquid: str, jinja: str) -> None:
    res, *_ = to_jinja(liquid)
    assert res == jinja


@pytest.mark.parametrize(
    "jinja,liquid,templates,dummies",
    [
        (
            """\
<img src="https://example.com/{{ a }}{% set LKMLFMT_MARKER = 0 %}"/>
""",
            """\
<img src="https://example.com/{{ A }}"/>
""",
            ["{{ A }}"],
            ["{{ a }}"],
        ),
    ],
    ids=utils.shorten,
)
def test_to_liquid(
    jinja: str, liquid: str, templates: list[str], dummies: list[str]
) -> None:
    res = to_liquid(jinja, templates, dummies)
    assert res == liquid


@pytest.mark.parametrize(
    "input_,output,indent",
    [
        (
            """\
<img src="https://example.com/image"/>
""",
            """\
<img src="https://example.com/image"/>
""",
            0,
        ),
        (
            """\
<img src="https://example.com/image"/>
""",
            """\
  <img src="https://example.com/image"/>
""",
            1,
        ),
    ],
    ids=utils.shorten,
)
def test_fmt_html(input_: str, output: str, indent: int) -> None:
    res = fmt_html(input_, indent)
    assert res == output
