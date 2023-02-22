from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents"""

    with open(path, mode="r", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',', quotechar='"')

        return list(csv_reader)


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them"""

    jobs = read(path)
    jobs_list = []

    for job in jobs:
        if job["job_type"] not in jobs_list:
            jobs_list.append(job["job_type"])
    return jobs_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
