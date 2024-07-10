---
layout: single
title: "Transparency Notes"
permalink: /transparency_notes.html
---

## Data
<a id="data" />

- The task uses the MultiClaim dataset, which contains:
  - 206k fact-checked claims from 142 fact-checking organizations;
  - 28k social media posts (SMPs) with references to relevant fact-checked claims;
  - 31k SMP-Claim pairs;
  - 27 languages;
  
- Data was collected by scraping fact-checks and associated social media posts;
- Posts are from before 2023;
- Data includes both original language versions and English translations;
- Test set will contain ~5000 new samples collected using the same methodology;

## Potential Biases and Errors
<a id="biases" />

- Biases due to the collection/fact-checking process:
  - Dataset may have biases in topic coverage and language distribution based on the sources used;
  - Some languages are significantly more represented than others;
  - The data collection process may favor certain types of claims or posts that are more likely to be fact-checked;

- Biases due to preprocessing:
  - The English versions of originally non-English posts were created using machine translation, which may introduce additional errors and biases;
  - Transcripts of images produced by OCR may contain errors;

- Biases / errors present in the data:
  - Social media posts may contain grammatical errors and other noise;
  - Social media posts may contain biases, which are less relevant/salient to fact-checkers and so not addressed in the corresponding fact-checks;
  - Fact-checks may contain errors or inaccuracies;

- ...

## Ethical Considerations
<a id="ethical" />

- Data collection involved scraping publicly available social media posts;
- Some content may cover sensitive topics related to e.g. politics, health or social issues;
- Re-sharing or otherwise spreading the provided data is not permitted;
- Steps were taken to minimize the risk of exposing private details of third persons; if the participants         

  ....

++++ TBD: flagging mechanism ++++




<!--

## Limitations
<a id="limitations" />


the data is not balanced



- ~15% of connections rely on visual information not captured in the text data
- Performance varies significantly across languages and monolingual vs crosslingual settings
- Evaluation metrics may not fully capture real-world utility for fact-checkers 


- Approximately 15% of connections rely on visual information (images or videos) not captured in the text data
- Performance varies significantly across languages and monolingual vs crosslingual settings
- The dataset may not be fully representative of all types of misinformation or fact-checks globally
- The task focuses on textual similarity, which may not capture all aspects of claim matching in real-world scenarios
- The evaluation setup (ranking claims) may not perfectly align with how fact-checkers work in practice
- The dataset does not include the full fact-checking articles, only the claim summaries
- Temporal aspects of misinformation spread are not captured in the current dataset
- The task does not address the veracity of claims, only their similarity to previously fact-checked claims
- Models trained on this data may not generalize well to rapidly evolving topics or new forms of misinformation




## Intended Use
<a id="intended_use" />

- To develop and evaluate multilingual claim retrieval systems 
- To advance research on combating online disinformation
- Not intended for deployment without further testing and safeguards

- The provided data can only be used for the purpose of participating in the shared task – for any other use, you need to acquire the [version published at Zenodo](https://zenodo.org/records/7737983);


The organizers are committed to responsible development and use of this technology. Participants are encouraged to consider potential societal impacts of their work.





- To develop and evaluate multilingual and crosslingual claim retrieval systems 
- To advance research on combating online disinformation across multiple languages
- To support fact-checkers in identifying previously checked claims more efficiently
- Not intended for deployment without further testing, safeguards, and consideration of real-world implications

The organizers are committed to responsible development and use of this technology. Participants are encouraged to consider potential societal impacts of their work and to disclose any additional data sources used in their models. 

-->