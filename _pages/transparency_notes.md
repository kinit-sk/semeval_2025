---
layout: single
title: "Transparency Notes"
permalink: /transparency_notes.html
---

<a id="data" />
## Data

- The task uses the [MultiClaim dataset](https://zenodo.org/records/7737983), which contains:
  - 206k fact-checked claims from 142 fact-checking organizations;
  - 28k social media posts (SMPs) with references to relevant fact-checked claims;
  - 31k SMP-Claim pairs;
  - 27 languages;
  
- Collection method and scope:
  - Data was collected by scraping fact-checks and associated social media posts;
  - Posts are from before 2023;
  - Data includes both original language versions and English translations;

- The test set will contain ~5000 new samples collected using the same methodology;

A more detailed description of the dataset can be found in the [dataset paper](https://arxiv.org/abs/2305.07991).

<a id="intended_use" />
## Intended Use

- To develop and evaluate multilingual fact-checked claim retrieval systems;
- To advance research on combating online disinformation across multiple languages;
- To support fact-checkers in identifying previously checked claims more efficiently;
- The shared data is only to be used for the purpose of participating in the shared task – for any other use, one needs to request the [version published at Zenodo](https://zenodo.org/records/7737983);
- Models, approaches and systems created in the shared task are not intended for immediate deployment – further testing and application of proper safeguards is necessary;

<a id="biases" />
## Potential Biases and Errors

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

<a id="ethical" />
## Ethical Considerations

- Data collection involved scraping publicly available social media posts;
- Some content may cover sensitive topics related to e.g. politics, health or social issues;
- Re-sharing or otherwise spreading the provided data is not permitted;
- Steps were taken to minimize the risk of exposing private details of third persons;

**Flagging Mechanism:**

- To ensure that any residual privacy concerns are adequately addressed, any potential issues discovered by the participants can be flagged by e-mail at [semeval@disai.eu](mailto:semeval@disai.eu);

<a id="limitations" />
## Limitations

- ~15% of cases key information is present in the visual modality and not captured in the textual data (e.g. the claim is written out in an image and part of the text of the post);
  - This is not an issue in the case of evaluation (it should affect all models equally), but can be a concern when fine-tuning models on the data;

- Evaluation metrics may not fully capture real-world utility for fact-checkers;

- The dataset may not be fully representative of all types of misinformation or fact-checks;

- The dataset does not include the full fact-checking articles, only titles that summarize them (and URLs to the full texts);

- The dataset is not balanced in terms of true vs. false claims, so it is likely not be suitable for training models for misinformation detection;
