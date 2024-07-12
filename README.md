## About the Task

The SemEval shared task on Multilingual and Crosslingual Fact-Checked Claim Retrieval addresses the critical challenge of efficiently identifying previously fact-checked claims across multiple languages — a task that can be time-consuming for professional fact-checkers even within a single language and becomes much more difficult to perform manually when the claim and the fact-check may be in different languages. Given the global spread of disinformation narratives, the range of languages that one would need to cover not to miss existing fact-checks is vast.

Participants in the task will **develop systems to retrieve relevant fact-checked claims** for given social media posts, using the [MultiClaim dataset](https://zenodo.org/records/7737983) of over 200,000 fact-checked claims and 28,000 social media posts in 27 languages – supporting fact-checkers and researchers in their efforts to curb the spread of misinformation globally. Submissions will be evaluated in terms of two metrics, mean reciprocal rank and success-at-K and in two separate tracks: monolingual and crosslingual. The task not only pushes the boundaries of NLP and information retrieval, but it also has significant potential for real-world impact in the fight against misinformation.s

**Important links:**

* [Shared task webpage](https://kinit-sk.github.io/semeval_2025/);
* [DisAI project webpage](https://disai.eu/);
* [Original dataset paper](https://arxiv.org/abs/2305.07991) for additional details about the dataset;

## Sample Data

[[LINK TO THE SAMPLE DATA AT GITHUB]](https://github.com/kinit-sk/semeval_2025/tree/main/sample_data)

In this task, you are given social media posts (SMP), and a bunch of fact-checks (FC). The goal is to find the most relevant fact-checks for each social media post.

In this trial data, we have in total 50 SMP-FC pairs. Out of them, we have 10 eng-eng pairs and 40 pairs in 2 different languages (each has 20 examples, 10 for monolingual (e.g., kor-kor) and 10 for multilingual (e.g., kor-eng)).

Potential retrieval setup can be various. For example, for each SMP, the FC search pool can be limited to the target language, different languages, and different mix of languages.

In this task, we aim to evaluate in both monolingual and crosslingual setup. Common metrics include mean reciprocal rank and success @ K. 

The sample data consists of three csv files:
### 1) trial_fact_check_post_mapping.csv (50 pairs)
This file contains the mapping between fact checks and social media posts.
It has three fields:
- fact_check_id: the id of the fact check in the trial_fact_checks.csv
- post_id: the id of the post in the trial_posts.csv
- pair_lang: the language info about this mapped pair. For example, spa-eng stands for SMP in Spanish and FC in English. 

### 2) trial_fact_checks.csv (50 fact-checks)
This file contains all fact-checks.
It has four fields:

- fact_check_id
- claim - This is the translated text (see below) of the fact-check claim, original text is also contained.
- instances - Instances of the fact-check – a list of timestamps and URLs.
- title - This is the translated text (see below) of the fact-check title

### 3) trial_posts.csv (47 social media posts)
This file contains all social media posts.
It has five fields:

- post_id
- instances - Instances of the fact-check – a list of timestamps and what were the social media platforms.
- ocr - This is a list of texts and their translated versions (see below) of the OCR transcripts based on the images attached to the post.
- verdicts - This is a list of verdicts attached by Meta (e.g., False information)
- text - This is the text and translated text (see below) of the text written by the user.

### Loading the Data

Along with the CSV files, we provide Python script ``load.py`` to load the data.

### What is a translated text?
A tuple of text, its translation to English and detected languages, e.g., in the sample below we have an original Croatian text, its translation to English and finally the predicted language composition (hbs = Serbo-Croatian):

(  '"...bolnice su pune ? ti  ina, muk...upravo sada, bolnica Rebro..tragi  no sme  no',  '"...hospitals are full? silence, silence... right now, Rebro hospital... tragically funny',  [('hbs', 1.0)] )

### API used for ocr and translation
We use following services to obtain transcripts and translations:
- Google Vision API. We use Google Vision API to extract text from images attached to the post. The API also returns a list of languages found in each image with their percentage.
- Google Translate API. We use Google Translate API to translate all the texts into English. The API also returns a most probable language.
