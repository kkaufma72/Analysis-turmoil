# Visual Analysis: Creating Bar and Pie Charts

# Bar Chart for Total vs. Nonfamily Households
plt.figure(figsize=(14, 7))
index = np.arange(len(trend_data['Year']))
bar_width = 0.35

plt.bar(index, trend_data['Total Households'], bar_width, label='Total Households')
plt.bar(index + bar_width, trend_data['Nonfamily Households'], bar_width, label='Nonfamily Households')

plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Households', fontsize=14)
plt.title('Total vs. Nonfamily Households (2014-2021)', fontsize=16)
plt.xticks(index + bar_width / 2, trend_data['Year'])
plt.legend()
plt.tight_layout()
plt.show()

# Pie Chart for the most recent year's household composition
most_recent_year = trend_data.iloc[-1]
labels = ['Nonfamily Households', 'Other Households']
sizes = [most_recent_year['Nonfamily Households'], most_recent_year['Total Households'] - most_recent_year['Nonfamily Households']]
colors = ['lightblue', 'lightgreen']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title(f'Household Composition in {most_recent_year["Year"]}', fontsize=16)
plt.show()
a
