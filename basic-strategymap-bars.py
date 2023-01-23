import matplotlib.pyplot as plt

# Create a list of tuples for each category and its corresponding score
trader_joes_data = [('Customer Satisfaction', 8.5), 
                    ('Store Quality', 9.4), 
                    ('Marketing', 7.2), 
                    ('Innovation', 6.7)]

# Create labels for the categories and scores
categories, scores = zip(*trader_joes_data)

# Create a figure
fig, ax = plt.subplots()

# Create a bar chart
ax.bar(categories, scores)

# Set the x-axis label
ax.set_xlabel('Categories')

# Set the y-axis label
ax.set_ylabel('Scores')
