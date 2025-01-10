def build_true_ticks_per_gem_earning_table(earn_gems: int):
    earning_table = []
    for level in range(1,11):
        if level <= 5: earning_rate = int(earn_gems/(level*.11+0.89))
        else: earning_rate = int(earn_gems/(level*.11+0.9))
        earning_table.append(earning_rate)
    
    return earning_table


def build_true_gem_per_week_earning_table(earn_gems: int):
    earning_table = []
    for level in range(1,11):
        if level <= 5: earning_rate = 60480000/int(earn_gems/(level*.11+0.89))
        else: earning_rate = 60480000/int(earn_gems/(level*.11+0.9))
        earning_table.append(earning_rate)
    
    return earning_table


def build_reported_gem_earning_table(earn_gems: int):
    from shared_functions import reported_round
    
    earning_table = []
    for level in range(1,11):
        if level <= 5: fractional_ticks_per_gem = earn_gems/(level*.11+0.89)
        else: fractional_ticks_per_gem = earn_gems/(level*.11+0.9)
        earning_table.append(reported_round(fractional_ticks_per_gem))
    
    return earning_table