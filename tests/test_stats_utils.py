import pandas as pd

from src.stats_utils import chi_square_test


def test_chi_square_test():
    """
    Test the chi-square test helper using a small
    artificial contingency table.
    """

    table = pd.DataFrame(
        {
            "group_a": [20, 30],
            "group_b": [30, 20],
        },
        index=["category_1", "category_2"],
    )

    chi2_stat, p_value, degrees_of_freedom = chi_square_test(table)

    assert chi2_stat >= 0
    assert 0 <= p_value <= 1
    assert degrees_of_freedom == 1