import matplotlib.pyplot as plt

# Define the strategic objectives and their relationships
strategic_objectives_trader_joes = {
    'Financial': ['Revenue growth', 'Profitability'],
    'Customer': ['Customer satisfaction', 'Market share'],
    'Internal': ['Efficiency', 'Innovation'],
    'Team Growth': ['Employee satisfaction', 'Talent development']
}

# Create the strategy map
fig, ax = plt.subplots()
ax.set_title('Strategy Map of Trader Joes')

# Draw the strategic objectives as boxes
for i, (key, value) in enumerate(strategic_objectives_trader_joes.items()):
    ax.text(0.5, i, key, ha='center')
    for j, obj in enumerate(value):
        ax.text(1, i-0.25+j*0.25, obj, ha='left')

# Draw lines connecting the strategic objectives
for i, (key, value) in enumerate(strategic_objectives_trader_joes.items()):
    for obj in value:
        ax.plot([0.5, 1], [i-0.5, i-0.25+value.index(obj)*0.25], '-o', c='black')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([0, 2])
ax.set_ylim([-1, len(strategic_objectives_trader_joes)])
plt.show()
