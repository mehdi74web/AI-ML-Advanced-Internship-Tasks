import streamlit as st
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

st.set_page_config(page_title="BERT News Classifier", layout="centered")
st.title("📰 News Topic Classifier Using Fine-Tuned BERT")
st.write("This application uses your fine-tuned BERT model to predict news categories.")

# Load the saved model instantly from your local folder
@st.cache_resource
def load_saved_model():
    tokenizer = AutoTokenizer.from_pretrained("./my_saved_bert_model")
    model = AutoModelForSequenceClassification.from_pretrained("./my_saved_bert_model")
    return tokenizer, model

tokenizer, model = load_saved_model()

st.subheader("Test the Model with Live News Headlines")
user_input = st.text_area("Enter a news headline or short summary here:")
label_names = ["World", "Sports", "Business", "Sci/Tech"]

if st.button("Predict Category"):
    if user_input.strip() != "":
        # Process input text
        inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True, max_length=128)
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        
        # Make prediction
        outputs = model(**inputs)
        prediction = np.argmax(outputs.logits.detach().cpu().numpy(), axis=-1)[0]
        result = label_names[prediction]
        
        # Display results cleanly
        st.metric(label="Predicted Topic Category", value=result)
    else:
        st.warning("Please enter some text before clicking predict.")
