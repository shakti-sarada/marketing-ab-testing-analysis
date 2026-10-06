import pandas as pd
from scipy.stats import chi2_contingency


def chi_square_test(
    contingency_table: pd.DataFrame,
) -> tuple[float, float, int]:
    """
    Perform a chi-square test of independence.

    Parameters
    ----------
    contingency_table : pd.DataFrame
        Contingency table containing observed frequencies.

    Returns
    -------
    tuple
        chi2_statistic, p_value, degrees_of_freedom
    """

    chi2_statistic, p_value, degrees_of_freedom, _ = chi2_contingency(
        contingency_table
    )

    return chi2_statistic, p_value, degrees_of_freedom