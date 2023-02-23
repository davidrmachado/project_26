from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industry and returns a list of them"""

    industries_list = read(path)
    industry = []

    for title in industries_list:
        if title["industry"] not in industry and title["industry"] != '':
            industry.append(title["industry"])
    return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
