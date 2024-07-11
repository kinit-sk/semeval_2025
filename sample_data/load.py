"""
This is just a quick script that is able to load the files. Just using pandas can be tricky because of the newline characters in the text data. Here it is handled via the `parse_col` method.
"""

import ast
import os

import pandas as pd

our_dataset_path = '.'

posts_path = os.path.join(our_dataset_path, 'posts.csv')
fact_checks_path = os.path.join(our_dataset_path, 'fact_checks.csv')
fact_check_post_mapping_path = os.path.join(our_dataset_path, 'fact_check_post_mapping.csv')

for path in [posts_path, fact_checks_path, fact_check_post_mapping_path]:
    assert os.path.isfile(path)

# We need to apply t = t.replace('\n', '\\n') for text fields before using `ast.literal_eval`.
# `ast.literal_eval` has problems when there are new lines in the text, e.g.:
# `ast.literal_eval('("\n")')` effectively tries to interpret the following code:

# ```
# ("
# ")
# ```

# This raises a SyntaxError exception. By escaping new lines we are able to force it to interpret it properly. There might
# be some other way to do this more systematically, but it is a workable fix for now.

parse_col = lambda s: ast.literal_eval(s.replace('\n', '\\n')) if s else s

df_fact_checks = pd.read_csv(fact_checks_path).fillna('').set_index('fact_check_id')
for col in ['claim', 'instances', 'title']:
    df_fact_checks[col] = df_fact_checks[col].apply(parse_col)


df_posts = pd.read_csv(posts_path).fillna('').set_index('post_id')
for col in ['instances', 'ocr', 'verdicts', 'text']:
    df_posts[col] = df_posts[col].apply(parse_col)


df_fact_check_post_mapping = pd.read_csv(fact_check_post_mapping_path) 
