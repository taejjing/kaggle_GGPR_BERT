import wget
import os

def load_data():
    gap_url = "https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/"
    bert_url = "https://raw.githubusercontent.com/google-research/bert/master/"
    print("Download GAP, BERT repo")

    gapFileList = ['gap-development.tsv', 'gap-validation.tsv', 'gap-test.tsv']
    bertFileList = ['modeling.py', 'extract_features.py', 'tokenization.py']

    if not os.path.isdir('gap'):
        os.mkdir('gap')
        for file in gapFileList:
            if not os.path.exists('gap/'+file): 
                wget.download(gap_url + file, 'gap/'+file)
    if not os.path.isdir('bert') :
        os.mkdir('bert')             
        for file in bertFileList:
            if not os.path.exists('bert/'+file): 
                wget.download(bert_url + file, 'bert/'+file)


