import streamlit as st
import pandas as pd
from wordcloud import WordCloud

# Dummy data
data = pd.DataFrame({
    'Employee': ['A', 'B', 'C', 'D', 'E'],
    'Team': ['Alpha', 'Alpha', 'Beta', 'Beta', 'Gamma'],
    'Manager': ['Atul Anand'] * 5,
    'Date': pd.date_range(start='2025-01-01', periods=5, freq='M'),
    'Communication': [4, 3, 5, 4, 2],
    'Recognition': [5, 4, 4, 3, 2],
    'Growth': [3, 4, 5, 2, 1],
    'Comments': [
        "Great team spirit",
        "Need more feedback",
        "Excellent growth opportunities",
        "Recognition could improve",
        "Poor communication"
    ]
})

# Title
st.title("Team Engagement Dashboard - Atul Anand's Span")

# Overall Engagement Score
st.header("Overall Engagement Score")
engagement_scores = data[['Communication', 'Recognition', 'Growth']].mean().mean()
st.metric("Average Engagement Score", f"{engagement_scores:.2f} / 5")

# Trend Over Time
st.header("Engagement Trend Over Time")
trend_data = data.groupby('Date')[['Communication', 'Recognition', 'Growth']].mean()
st.line_chart(trend_data)

# Breakdown by Dimension
st.header("Breakdown by Engagement Dimension")
dimension_avg = data[['Communication', 'Recognition', 'Growth']].mean()
st.bar_chart(dimension_avg)

# Team-wise Comparison
st.header("Team-wise Engagement Comparison")
team_avg = data.groupby('Team')[['Communication', 'Recognition', 'Growth']].mean()
st.dataframe(team_avg)

# Word Cloud for Comments
st.header("Feedback Word Cloud")
comments_text = " ".join(data['Comments'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(comments_text)

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)
st.area_chart(data, y ='Employee')


