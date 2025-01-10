def round_half_away_from_zero(x):
    import math
    if x >= 0:
        decimal = x - math.floor(x)
        if decimal < 0.5: return math.floor(x)
        return math.ceil(x)
    else:
        decimal = x - math.ceil(x)
        if decimal > -0.5: return math.ceil(x)
        return math.floor(x)


def reported_round(fractional_ticks_per_currency: float):
    if fractional_ticks_per_currency <= 6000:
        num = 6000
        text = 'MIN'
    elif fractional_ticks_per_currency <= 360000:
        num = 360000
        text = 'HOUR'
    elif fractional_ticks_per_currency <= 8640000:
        num = 8640000
        text = 'DAY'
    elif fractional_ticks_per_currency <= 60480000:
        num = 60480000
        text = 'WEEK'
    else:
        # A 28 day is the only whole number amount of days that correctly builds the gem earning tables, but technically num could be lesser or greater.
        num = 241920000
        text = 'MONTH'
    return f'{round_half_away_from_zero(num/fractional_ticks_per_currency)}/{text}'