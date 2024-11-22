import pandas as pd
import fasttext
# Load your data
df = pd.read_excel('data/train_clean_data.xlsx')

# Prepare data in FastText format
# OR you can download it from here: https://drive.google.com/file/d/1kegRHWMRJHzsoI3lVVo6JhkLdGnMO4p5/view?usp=sharing
def prepare_fasttext_format(df, output_file):
    with open(output_file, 'w') as f:
        for _, row in df.iterrows():
            label = f"__label__{row['label']}"  # Prefix label with __label__
            text = row['clean_text'].replace("\n", " ")  # Ensure text is on one line
            f.write(f"{label} {text}\n")

# Generate the training file
prepare_fasttext_format(df, 'fasttext_train.txt')



# Train the model
model = fasttext.train_supervised(
    input="fasttext_train.txt",  # Path to your training file
    lr=1.0,                      # Learning rate
    epoch=25,                    # Number of epochs
    wordNgrams=2,                # Use bigrams
    verbose=2,                   # Verbosity level
    minCount=1,                  # Include all words
    loss='softmax'               # Use softmax for classification
)

# Save the model
model.save_model("fasttext_classification_model.bin")
