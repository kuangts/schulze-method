'''
The selection of new team name
In schulze.py, 'iterkeys' is changed to 'keys' for python3

'''

import schulze

# indices of all candidates (1-16)
candidate_names = list(range(1,17)) 

# ballots (8 total)
ballots = [
    [[ 5], [ 7], [15], [ 9], [ 2], [ 1]],
    [[15], [16], [ 7]],
    [[16], [13], [ 2], [ 4], [ 7], [10]],
    [[ 9], [ 7], [14], [11], [15], [10]],
    [[ 7], [ 5], [15], [ 6], [ 4], [ 9]],
    [[ 2], [ 1], [ 8]],
    [[ 1]],
    [[16], [15], [ 8], [ 7]],
]

# complete each ballots by adding the other candidates as equally last
ranks = [b + [list(set(candidate_names)-set([x[0] for x in b]))] for b in ballots]

# add equal weight to all ballots
weight = 1/8
weighted_ranks = [(b, weight) for b in ranks]

# calculate ranking and print
ranks = schulze.compute_ranks(candidate_names, weighted_ranks)
print(*[f'{i+1} place: {r}' for i,r in enumerate(ranks)], sep='\n')
