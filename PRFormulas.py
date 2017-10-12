# Formulas and statistics for calculating passer rating
# NOTE: pr will be used to abbreviate passer rating


# Calculates Passer Rating based on NFL formula must use floats for function parameters
def calculate_pr_nfl(att, comp, yds, td, ints):
    a = ((comp / att) - 0.3) * 5.0
    b = ((yds / att) - 3) * 0.25
    c = (td / att) * 20.0
    d = 2.375 - ((ints / att) * 25.0)
    pr = round(((a + b + c + d) / 6.0) * 100.0, 1)
    print pr
    return pr
