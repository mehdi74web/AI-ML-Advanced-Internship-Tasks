# AI-ML-Advanced-Internship-Tasks
This repository contains the completed advanced engineering tasks for the AI/ML Engineering Internship at **Developers Hub Corporation**[cite: 1, 2]. [cite_start]All tasks are implemented with an emphasis on production-ready structures, rigorous evaluation, and clean deployment
📰 Task 1: News Topic Classifier Using BERT
🎯 Objective
To fine-tune a pre-trained transformer model (bert-base-uncased) to automatically categorize text-based news headlines into four major domains: World, Sports, Business, and Sci/Tech using the AG News Dataset.  

+ 1

⚙️ Methodology & Approach

Data Preprocessing: Loaded the ag_news dataset from Hugging Face. Tokenized raw text using AutoTokenizer, applying sequence padding and truncation down to a max_length of 128 tokens.  

+ 1


Transfer Learning: Loaded AutoModelForSequenceClassification with a 4-class classification head over the base BERT transformer. Fine-tuned the model utilizing Hugging Face's Trainer API over an optimized epoch profile.  



Evaluation: Monitored training convergence using classification Accuracy and Macro F1-score to balance multi-class performance.  



Lightweight Deployment: Built a user-friendly web interface via Streamlit to accept user-input text and compute live, real-time news classifications.  


📊 Key Results & Observations
Performance Metrics: Achieved a test classification accuracy of ~88% and a Macro F1-score of 0.87.

Observation: Transformer models show exceptional capability in picking up subtle vocabulary signals (e.g., brand names vs. stock indices) to differentiate tightly related categories like Business and Sci/Tech.

⚙️ Task 2: End-to-End ML Pipeline with Scikit-learn Pipeline API
🎯 Objective
To design and implement a reusable, modular, and production-ready machine learning framework using scikit-learn's Pipeline component to predict customer churn and eliminate potential data leakage risks.  

+ 1

⚙️ Methodology & Approach

Data Integrity & Imputation: Preprocessed the Telco Churn Dataset by parsing structural discrepancies in the numeric sequences (e.g., casting TotalCharges space characters to median float values).  



Encapsulated Pipelines: Constructed an isolated ColumnTransformer architecture:  



Numerical Channel: Automated numerical normalization using StandardScaler.  



Categorical Channel: Handled textual multi-class variables smoothly using an unknown-resilient OneHotEncoder.  



Hyperparameter Tuning: Bound the preprocessing block alongside a RandomForestClassifier inside a unified Pipeline workspace. Used GridSearchCV with 3-fold cross-validation to search over tree depth configurations.  

+ 1


Serialization: Exported the finalized optimal estimator pipeline into a standalone .joblib binary to facilitate instant downstream integration.  


📊 Key Results & Observations
Optimal Parameters: Found top performance at max_depth: 5 and n_estimators: 100.

Performance Metrics: Secured a strong overall test accuracy of ~80%.

Observation: Enclosing scaling and structural encoders directly inside an atomic scikit-learn pipeline object guarantees clean execution vectors and completely avoids the risk of data leakage during testing or deployment.

🏷️ Task 5: Auto Tagging Support Tickets Using LLM
🎯 Objective
To deploy a Large Language Model (LLM) framework capable of parsing complex, unformatted, free-text IT/software support tickets and accurately sorting and ranking the top 3 most probable tags per issue.  

+ 3

⚙️ Methodology & Approach

Dataset Representation: Established a mock database simulating realistic help desk tickets, featuring messy text structures detailing server lockouts, credit card declines, and software crashes.  



Zero-Shot Classifier: Leveraged an open-source, instruction-tuned foundation LLM framework (facebook/bart-large-mnli) through a Hugging Face pipeline, entirely bypassing the need for computationally heavy custom network adjustments.  



Ranking Matrix: Injected candidate labels (Bug Report, Billing & Payment, Account Security, UI/UX Layout) straight into the model execution context. Computed probability sequences to capture semantic affinity and sort out the top 3 class outputs per entry.  



📊 Key Results & Observations
Tag Accuracy: The semantic context matched flawlessly with high confidence scores without any custom label adjustment. For example, a ticket regarding expired details mapped directly to Billing & Payment as its number one prediction.


Observation: Zero-shot learning through foundation models drastically minimizes engineering overhead by completely removing the prerequisite for large, human-curated training label repositories.  


👥 Intern Details

Internship Track: AI/ML Engineering - Advanced Task Set   


Submission Date: 9th June, 2026   



Company: Developers Hub Corporation   
