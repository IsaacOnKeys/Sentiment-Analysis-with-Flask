# Sentiment-Analysis-with-Flask
This is based on this project from IBM:
https://github.com/ibm-developer-skills-network/zzrjt-practice-project-emb-ai.git

Uses the BERT based Sentiment Analysis function of the Watson NLP Library

### Interacting With the Bert function:
```python
URL: 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
Headers: {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
Input json: { "raw_document": { "text": text_to_analyse } } 
```
#### Note: it is necessary to implement an account with IBM Cloud to use this app