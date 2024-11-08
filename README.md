# Sentiment Analysis App

This repository provides a **Sentiment Analysis App** built with **Streamlit** that allows users to input text and analyze its sentiment using **NLTK's VADER** sentiment analysis tool. The app identifies and displays the overall sentiment (positive, negative, or neutral) along with a visual breakdown.

### Features

1. **Text Input**: 
   - Accepts user input through a text area for the sentiment analysis.

2. **Sentiment Analysis**:
   - **VADER Sentiment Analyzer**: Uses NLTK's `SentimentIntensityAnalyzer` to assess the input text's sentiment and produces a compound score, as well as positive, negative, and neutral score breakdowns.

3. **Sentiment Result Display**:
   - **Compound Score**: Overall sentiment score indicating positive, negative, or neutral sentiment.
   - **Breakdown Scores**: Displays individual scores for positive, negative, and neutral aspects of the text.
   - **Sentiment Label**: Classifies the text sentiment as "Positive," "Negative," or "Neutral" based on the compound score.

4. **Visualization**:
   - **Pie Chart of Sentiment Distribution**: Displays a pie chart for a visual representation of positive, negative, and neutral sentiment proportions.

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sentiment-analysis-app
   ```
3. Install required dependencies:
   ```bash
   pip install streamlit nltk matplotlib
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Download the VADER lexicon (only necessary on the first run):
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

### Screenshots

- **Sentiment Analysis Results**: Shows compound and breakdown scores along with a sentiment label.
- **Sentiment Distribution Chart**: Pie chart visualizing positive, negative, and neutral sentiment proportions.

### Technologies Used

- **Streamlit**: For building the interactive web interface.
- **NLTK**: For sentiment analysis using VADER.
- **Matplotlib**: For generating the pie chart visualization.

### Future Enhancements

- Enable sentiment analysis on longer texts and documents.
- Integrate a live feed of user text inputs for real-time analysis.
- Improve visualizations with more granular sentiment score graphs.

---

This description provides an overview of the Sentiment Analysis App, including its setup instructions, features, and potential future improvements.
