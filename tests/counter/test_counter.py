from src.pre_built.counter import count_ocurrences


def test_counter():
    """Ensures the correct counting outcome of count_ocurrrences"""

    assert count_ocurrences("data/jobs.csv", "python") == 1639
    assert count_ocurrences("data/jobs.csv", "javascript") == 122
