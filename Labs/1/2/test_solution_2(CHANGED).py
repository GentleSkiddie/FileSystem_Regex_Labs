import os
import importlib.util
from pathlib import Path
from dataclasses import asdict, is_dataclass

import pytest

path = Path(__file__).parent

spec_cases = importlib.util.spec_from_file_location(
    "test_cases.cases", f"{path}/test_cases/cases.py"
)
cases = importlib.util.module_from_spec(spec_cases)
spec_cases.loader.exec_module(cases)

spec_solution = importlib.util.spec_from_file_location(
    "solution", f"{path}/solution.py"
)
solution = importlib.util.module_from_spec(spec_solution)
spec_solution.loader.exec_module(solution)


def _generate_test_ids(cases_amount):
    base_id = "test_case_"
    return [f"{base_id}{index}" for index in range(1, cases_amount + 1)]


@pytest.fixture(scope="function")
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


@pytest.mark.parametrize(
    "test_case", cases.cases, ids=_generate_test_ids(len(cases.cases))
)
@pytest.mark.usefixtures("change_test_dir")
def test_solution(test_case):
    user_out = solution.solve(**asdict(test_case.in_data))
    correct_answer = test_case.out_data

    msg_type_error = "Answer has the wrong type."
    assert type(user_out) == type(correct_answer), msg_type_error

    if isinstance(user_out, (int, str, bool)):
        assert user_out == correct_answer
        return

    # if list, dict
    msg_len_error = "Length of collection isn't correct."
    assert len(user_out) == len(correct_answer), msg_len_error

    if _is_answer_sorted(test_case.in_data):
        assert user_out == correct_answer
        return

    # not sorted collections
    if isinstance(user_out, list):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # CHANGED BECAUSE THE LIST CAN BE OF ZERO LENGTH : CASE № 9
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if len(user_out):

            if isinstance(user_out[0], dict):
                for user_out_i, correct_answer_i in zip(user_out, correct_answer):
                    _check_dict(user_out_i, correct_answer_i)
                return
        assert set(user_out) == set(correct_answer)
        return

    if isinstance(user_out, dict):
        _check_dict(user_out, correct_answer)


def _is_answer_sorted(in_data):
    try:
        return in_data.is_sorted
    except AttributeError:
        return False


def _generate_test_ids(cases_amount):
    base_id = "test_case_"
    return [f"{base_id}{index}" for index in range(1, cases_amount + 1)]


def _check_dict(user_out, correct_answer):
    list_user_out = list(user_out.items())
    list_correct_answer = list(correct_answer.items())

    for user_out in list_user_out:
        msg_find_error = (
            f"Collection isn't correct. Can't find {user_out} in correct answer."
        )
        assert user_out in list_correct_answer, msg_find_error
