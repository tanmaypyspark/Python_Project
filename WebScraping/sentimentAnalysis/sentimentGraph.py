import nltk
import pandas as pd
import numpy as np
import os, sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Download Vader Package
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

## Read .csv file
def read_file(filePath, format = 'csv'):
    
    if 'csv' in format:
        df = pd.read_csv(filePath)
    if '.json' in format:
        df = pd.read_json(filePath)
    if '.xlsx' in format:
        df = pd.read_excel(filePath)
    if '.txt' in format:
        df = pd.read_csv(filePath, delimiter = '\t')
    return df

def write_file(filePath, df, format = 'csv'):
    
    if 'csv' in format:
        df.to_csv(filePath, index = False)
    if '.json' in format:
        df.to_json(filePath)
    if '.xlsx' in format:
        df.to_excel(filePath, index = False)
    if '.txt' in format:
        df.to_csv(filePath, index = False, sep = '\t')

def translatorTOENG(df, column_name):
    
    #Create Translator object
    trans = Translator()
    
    # Apply translation to each row in the specified column
    df['Translated_Text'] = df[column_name].apply(
        lambda text: trans.translate(text, src='hi', dest='en').text if pd.notnull(text) else text
    )
    
    return df
    
    
def sentiment_Analyzer(df):
    # Apply Sentiment Analysis to the 'Comment' column
    try:
        if 'Comment' in df.columns:
            ## Fill the NaN values with empty string
            df['Comment'] = df['Comment'].fillna('')
            
            ## Apply Sentiment Analysis
            df['Sentiment_Score'] = df['Comment'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
            
            df["Sentiment_Label"] = np.where(df["Sentiment_Score"] > 0, 'Positive', (np.where(df["Sentiment_Score"] < 0, 'Negative', 'Neutral')))
            return df
        else:
            logger.error("'Comment' column not found in the DataFrame.")
        
    except Exception as e:
        logger.error(f"An error occurred during Sentiment Analysis: {e}")
        sys.exit(1)

def kickOffTheSentimentAnalysis(basepath, finalPath):
    ''' This Function is use to Kick Off the Sentiment Analysis'''
    logger.info("Starting Sentiment Analysis...")
    
    for file in os.listdir(basepath):
        logger.info(f"Sentiment Analysis Start For: {file}")
        removeFromFileName = '_'.join(file.split('_')[-2:])
        finalFileName = file.replace(f"_{removeFromFileName}", '.csv').replace('comments','Sentiment_Analysis')
        logger.info(f"Final File Name: {finalFileName}")
        # Read the file
        df = read_file(os.path.join(basepath, file))
        
        # Translate the comments to English, If any Hinlish comments are present
        df_translated = translatorTOENG(df, 'Comment')
        
        # Apply Sentiment Analysis
        df_Final = sentiment_Analyzer(df_translated)
        if not os.path.exists(finalPath):
            os.makedirs(finalPath)
        df_Final.to_csv(os.path.join(finalPath, finalFileName), index = False)

# if __name__ == "__main__":
#     os.path.dirname(os.path.abspath(__file__))
#     # print("Pathh",os.getcwd())
#     basepath = 'C:\\Users\\tanma\\Desktop\\GIT_PUSH\\Python_Project\\WebScraping\\output\\Stagging'
#     finalPath = 'C:\\Users\\tanma\\Desktop\\GIT_PUSH\\Python_Project\\WebScraping\\output\\Analysis'
#     kickOffTheSentimentAnalysis(basepath, finalPath)
    