import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Ensure VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Title
st.title("Sentiment Analysis App")

# Text input
text = st.text_area("Enter your text:")

# Analyze button
if st.button("Analyze"):
    # Initialize SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Analyze sentiment
    sentiment = sia.polarity_scores(text)
    
    # Display results
    st.write("Sentiment Analysis Results:")
    
    # Safely access and display results
    compound_score = sentiment.get('compound', 0)
    positive_score = sentiment.get('pos', 0)
    negative_score = sentiment.get('neg', 0)
    neutral_score = sentiment.get('neu', 0)

    st.write(f"Compound: {compound_score:.2f}")
    st.write(f"Positive: {positive_score:.2f}")
    st.write(f"Negative: {negative_score:.2f}")
    st.write(f"Neutral: {neutral_score:.2f}")
    
    # Determine sentiment
    if compound_score > 0.05:
        st.success("Positive Sentiment")
    elif compound_score < -0.05:
        st.error("Negative Sentiment")
    else:
        st.warning("Neutral Sentiment")
    
    # Plot sentiment distribution
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_score, negative_score, neutral_score]
    
    # Create pie chart
    plt.figure(figsize=(6, 6))  # Optional: Set the size of the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(plt)
    plt.clf()  # Clear the figure for the next use
