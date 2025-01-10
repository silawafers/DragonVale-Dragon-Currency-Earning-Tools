def build_true_ticks_per_etherium_earning_table(earn_etherium: int, elder: bool):
    earning_table = []
    for level in range(1,21 + elder):
        earning_rate = int(earn_etherium/level)
        earning_table.append(earning_rate)
    
    return earning_table


def build_true_etherium_per_hour_earning_table(earn_etherium: int, elder: bool):
    earning_table = []
    for level in range(1,21 + elder):
        earning_rate = 360000/int(earn_etherium/level)
        earning_table.append(earning_rate)
    
    return earning_table


def build_reported_etherium_earning_table(earn_etherium: int, elder: bool):
    from shared_functions import reported_round
    
    earning_table = []
    for level in range(1,21 + elder):
        fractional_ticks_per_etherium = earn_etherium/level
        earning_table.append(reported_round(fractional_ticks_per_etherium))
    
    return earning_table