from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs"""

    salaries = read(path)
    max_salaries = []

    for salary in salaries:
        if salary["max_salary"].isdigit():
            max_salaries.append(int(salary["max_salary"]))
    return max(max_salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs"""

    salaries = read(path)
    min_salaries = []

    for salary in salaries:
        if salary["min_salary"].isdigit():
            min_salaries.append(int(salary["min_salary"]))
    return min(min_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job"""

    try:

        MAX_SALARY = int(job["max_salary"])
        MIN_SALARY = int(job["min_salary"])

        if MIN_SALARY > MAX_SALARY:
            raise ValueError

        return MIN_SALARY <= int(salary) <= MAX_SALARY

    except (TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
