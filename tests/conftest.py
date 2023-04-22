import typing

import pytest

SUPP, CONF = 0.5, 0.5
MAX_SUPP, MAX_CONF = 1, 1
ANTECEDENT_TYPE = 'ante'
SUCCEDENT_TYPE = 'succ'


@pytest.fixture
def attr_factory() -> typing.Callable[[int, str], str]:
    def make_attr(index: int, cedent_type: str):
        return f'{cedent_type}_attr_{index}'

    return make_attr


@pytest.fixture
def cedent_factory(attr_factory) -> typing.Callable[[int, str], typing.Set[str]]:
    def make_cedent(number_of_attrs: int, cedent_type: str):
        return set(attr_factory(i, cedent_type) for i in range(number_of_attrs))

    return make_cedent


@pytest.fixture
def rule_factory():
    def make_rule(ante: typing.Set[str], succ: typing.Set[str], supp: float, conf: float) -> typing.Dict[str, typing.Set[str | float]]:
        return {
            'antecedent': ante,
            'succedent': succ,
            'support': supp,
            'confidence': conf,
        }

    return make_rule
