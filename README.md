A Natural Language Processing (NLP) model designed to classify crime details into predefined Categories and Sub-Categories based on input data.
## Prerequisites
- Python 3.10 or higher
- Libraries: Install the required dependencies listed in requirements.txt


## Data Preparation
### Exploratory Data Analysis (EDA) and Cleaning
#### 1.	Initial Observations
Columns had mismatch counts
- crimeaditionalinfo: 93666
- sub_category: 87096
- category: 93687

#### 2. Cleaning Process
- applied .strip() function for trimming whitespace
- Removed blank rows in crimeaditionalinfo
- Deduplicated the cleaned text

#### 3. Post Cleaning
- Remaining records: 79,399 rows for all columns.

### Test Data Cleaning
##### 1. Initial Counts
- crimeaditionalinfo: 31230
- sub_category: 28994
- category: 31223
  
#### 2. Post Cleaning
27157 records for all columns

## Data Categorization
### Subcategory Standardization
#### Corrected typos and merged ambiguous labels:
- Combined similar terms (e.g., Ransomware and Ransomware Attack → Ransomware)
- Split merged terms into distinct categories (e.g., DebitCredit Card FraudSim Swap Fraud → Debit/Credit Card Fraud and SIM Swap Fraud)

Below is the mapping of categories available in the dataset to those mentioned in the document

| Old Category (From Dataset)                            | New Category  (From Document)                                           |
|-------------------------------------------|----------------------------------------------------------|
| Cyber Bullying  Stalking  Sexting         | Cyber Bullying/Stalking/Sexting                          |
| Fraud CallVishing                         | Fraud Call/Vishing                                       |
| Online Gambling  Betting                  | Online Gambling/Betting Fraud                           |
| Online Job Fraud                          | Online Job Fraud                                         |
| UPI Related Frauds                        | UPI-Related Frauds                                       |
| Internet Banking Related Fraud            | Internet Banking-Related Fraud                          |
| Other                                     | Any Other Cyber Crime                                    |
| Profile Hacking Identity Theft            | Profile Hacking/Identity Theft                          |
| EWallet Related Fraud                     | E-Wallet Related Frauds                                 |
| Data Breach/Theft                         | Unauthorized Access/Data Breach                         |
| Denial of Service (DoS)/Distributed Denial of Service (DDOS) attacks | Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks |
| FakeImpersonating Profile                 | Fake/Impersonating Profile                              |
| Cryptocurrency Fraud                      | Cryptocurrency Crime                                     |
| Malware Attack                            | Malware attacks                                          |
| Business Email CompromiseEmail Takeover   | Business Email Compromise/Email Takeover                |
| Email Hacking                             | Email Hacking                                            |
| Cheating by Impersonation                 | Cheating by Impersonation                               |
| Hacking/Defacement                        | Defacement/Hacking                                      |
| Unauthorised AccessData Breach            | Unauthorized Access/Data Breach                         |
| SQL Injection                             | SQL Injection                                           |
| Provocative Speech for unlawful acts      | Provocative Speech of Unlawful Acts                     |
| Ransomware Attack                         | Ransomware                                              |
| Cyber Terrorism                           | Cyber Terrorism                                         |
| Tampering with computer source documents  | Tampering with computer source documents                |
| DematDepository Fraud                     | Demat/Depository Fraud                                  |
| Online Trafficking                        | Online Cyber Trafficking                                |
| Online Matrimonial Fraud                  | Online Matrimonial Fraud                                |
| Website DefacementHacking                 | Defacement/Hacking                                      |
| Damage to computer computer systems etc   | Damage to Computer Systems                              |
| Impersonating Email                       | Impersonating Email                                     |
| EMail Phishing                            | Email Phishing                                          |
| Ransomware                                | Ransomware                                              |
| Intimidating Email                        | Intimidating Email                                      |
| Against Interest of sovereignty or integrity of India | Against Interest of sovereignty or integrity of India |
| Computer Generated CSAM/CSEM             | Child Pornography/Child Sexual Abuse Material (CSAM)    |
| Cyber Blackmailing & Threatening          | Cyber Bullying/Stalking/Sexting                         |
| Sexual Harassment                         | Cyber Bullying/Stalking/Sexting                         |
| DebitCredit Card Fraud                    | Debit/Credit Card Fraud                                 |
| Sim Swap Fraud                            | SIM Swap Fraud                                          |


### Final Subcategory Count
- Defined 39 subcategories by mapping dataset categories to consistent names

## Dataset Review and Identified Issue
### Issues Identified
1. The dataset contained only 39 subcategories (from both train and test data) compared to the 62 subcategories mentioned in the document.
2. Categories in the train-test dataset were actually subcategories
3. 3,783 records in the dataset lacked subcategory labels.
4. Some subcategories were misclassified.

### Resolution Method
1. Worked with the available data to address inconsistencies.
2. Grouped the 62 subcategories into 4 top-level categories for streamlined classification:
   1. any_other_cyber_crime
   2. cyberbullying_and_online_harassment
   3. financial_frauds
   4. system_hacking_and_damage
3. Check this [file](data/subcategory_mapping.txt) for the mapping of 62 subcategories to the top four categories.
4. Used LLMs to classify the data into these four categories

## Data Distribution After Mapping to Top-Level Categories
After mapping the subcategories to the four top-level categories, the data distribution was as follows:
- any_other_cyber_crime: 1,981 records
- cyberbullying_and_online_harassment: 9,026 records
- financial_frauds: financial_frauds
- system_hacking_and_damage: 1,981 records

Approach to predict Sub-Category and Category

![image](https://github.com/user-attachments/assets/d4098c02-944e-4d98-a723-36efc1ca98ba)

## Model Development
### Algorithms Evaluated
1. Boosting Algorithm: XGBoost
2. Neural Networks: FastText
3. Transformers: DistilBERT and ALBERT

Confusion matrix and classification report on test data using different algorithms
#### XGBoost

![image](https://github.com/user-attachments/assets/216213e3-8cd3-4af6-b3c9-e0128d948363) ![image](https://github.com/user-attachments/assets/a9b1316e-4188-4db3-8ec0-9b3d8a681c21)

#### Fasttext

![image](https://github.com/user-attachments/assets/ede062af-b30c-4d00-a78a-231905f7082c) ![image](https://github.com/user-attachments/assets/f40b8f83-e120-4809-a5a5-ce06e231c399)

#### Albert

![image](https://github.com/user-attachments/assets/e983721a-fe6b-4198-9652-4e92f008cd22) ![image](https://github.com/user-attachments/assets/06569506-7caa-4556-bc44-c45a1746f6a7)

#### Distilbert

![image](https://github.com/user-attachments/assets/1ae7d610-3d62-457b-93b0-72d63eb228bd) ![image](https://github.com/user-attachments/assets/2b8a15a4-0728-4407-8893-f8bb9c70d0b1)

## Model Comparison and results on grouped categories
| model      | data_count_to_test | ram    | model_size (mb) | gpu            | taken_time_to_process_records (seconds) | precision | recall | accuracy | f1-score |
|------------|--------------------|--------|-----------------|----------------|----------------------------------------|-----------|--------|----------|----------|
| distillbert| 27158              | 2.8 GB | 767.3           | 485 MB (60)    | 140.87                                 | 0.937     | 0.937  | 0.94     | 0.937    |
| albert     | 27158              | 3.2 GB | 134.6           | 213 MB(65 - 70%)| 240                                    | 0.936     | 0.937  | 0.94     | 0.936    |
| fasttext   | 27158              | 2.7 GB | 806.6           | 0              | 9.93                                  | 0.92      | 0.92   | 0.93     | 0.925    |

**Decision**: Chose FastText due to its efficiency and competitive performance.

## Implementation Highlights
1. Handling Imbalanced Data
   - Optimized hyperparameters to handle imbalanced data
    
2. Subcategory Prediction
   - Applied rule-based mappings for subcategories
   - Grouped predicted subcategories into the top-level categories
     
## Results and Performance
- Accuracy:
- Precision:
- Recall:
- Processing Speed: FastText completed predictions significantly faster compared to transformer-based models.


## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/ankitvirla/crime_categorization_model.git
   cd crime-categorization
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Do Inference: Modify the script based on input and use inference.py
   ```bash
   python3 scripts/inference.py
