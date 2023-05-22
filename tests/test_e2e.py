import pytest
from lkmlfmt import fmt  # type: ignore

from tests import utils


@pytest.mark.parametrize(
    "input_,output",
    [
        (
            """\
dimension: column_name {
html:
{% if value == "foo" %}
<img src="https://example.com/foo"/>
{% else %}
<img src="https://example.com/bar"/>
{% endif %}
;;
}
""",
            """\
dimension: column_name {
  html:
    {% if value == "foo" %}
      <img src="https://example.com/foo"/>
    {% else %}
      <img src="https://example.com/bar"/>
    {% endif %}
  ;;
}
""",
        ),
    ],
    ids=utils.shorten,
)
def test_fmt(input_: str, output: str) -> None:
    res = fmt(input_, plugins=["lkmlfmt_djhtml"])
    assert res == output
