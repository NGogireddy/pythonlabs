import numpy as np

outcomes = ["00", "01", "10", "11"]
probabilities = [0.5, 0.0, 0.0, 0.5]

measurements = np.random.choice(
    outcomes,
    size=1000,
    p=probabilities
)

counts = {'00':0, '01':0, '10':0, '11':0}
for result in measurements:
    counts[result] += 1

print(counts)

exp_count = sum(counts.values())
assert exp_count == 1000
assert counts['01'] == 0
assert counts['10'] == 0

"""
Learning: 
The standard deviation of the count for an outcome with probability p is:
sigma=sqrt(np(1-p)) where n is sample size. 

For sample size of 1000 and outcome of state '00' in a bell state (probability is 0.5) is 
sqrt(1000 * 0.5 (1-0.5))
"""
