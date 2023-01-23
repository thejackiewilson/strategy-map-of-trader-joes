import matplotlib.pyplot as plt

# Define the strategic objectives and their relationships
strategic_objectives = {
    'Customer': ['Customer satisfaction', 'Market share', 'Customer retention'],
    'Financial': ['Revenue growth', 'Profitability', 'Cost management'],
    'Internal': ['Product quality', 'Efficiency', 'Partnerships with local suppliers'],
    'Learning & Growth': ['Employee satisfaction', 'Talent development', 'Technology integration'],
    'Customer experience': ['Unique shopping experience', 'Friendly customer service', 'Engaging in-store promotions']
}

# Create the strategy map
fig, ax = plt.subplots()
ax.set_title('Trader Joe\'s Strategy Map')

# Draw the strategic objectives as boxes
for i, (key, value) in enumerate(strategic_objectives.items()):
    ax.text(0.5, i, key, ha='center')
    for j, obj in enumerate(value):
        ax.text(1, i-0.25+j*0.25, obj, ha='left')

# Draw lines connecting the strategic objectives
for i, (key, value) in enumerate(strategic_objectives.items()):
    for obj in value:
        ax.plot([0.5, 1], [i-0.5, i-0.25+value.index(obj)*0.25], '-o', c='black')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([0, 2])
ax.set_ylim([-1, len(strategic_objectives)])
plt.show()
