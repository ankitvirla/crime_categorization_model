import fasttext
import time
import re

#clean text function
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove emojis (Unicode range covers most emojis)
    text = re.sub(r'[\U0001F600-\U0001F64F'  # emoticons
                  r'\U0001F300-\U0001F5FF'  # symbols & pictographs
                  r'\U0001F680-\U0001F6FF'  # transport & map symbols
                  r'\U0001F700-\U0001F77F'  # alchemical symbols
                  r'\U0001F780-\U0001F7FF'  # Geometric Shapes Extended
                  r'\U0001F800-\U0001F8FF'  # Supplemental Arrows-C
                  r'\U0001F900-\U0001F9FF'  # Supplemental Symbols and Pictographs
                  r'\U0001FA00-\U0001FA6F'  # Chess Symbols
                  r'\U0001FA70-\U0001FAFF'  # Symbols and Pictographs Extended-A
                  r'\U00002700-\U000027BF'  # Dingbats
                  r'\U0001F1E0-\U0001F1FF'  # flags (iOS)
                  r']+', '', text)
    
    # Remove special symbols (e.g., #, @) and dashes
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    
    # Remove extra spaces
    clean_text = re.sub(r'\s+', ' ', text).strip().lower()
    
    return clean_text

#load fasttext model
model = fasttext.load_model("fasttext_classification_model.bin")
class_labels = ['any_other_cyber_crime', 'cyberbullying_and_online_harassment', 'financial_frauds', 'system_hacking_and_damage']

# Example inference
def predict(text):
    text = clean_text(text)
    label, probability = model.predict(text)
    label = label[0]
    label = int(label.replace('__label__',''))
    label = class_labels[label]
    return label, probability[0]
