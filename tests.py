import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def format_text(text):
    replace_dic = {261 : 97,
        281 : 101,
        263 : 99,
        347 : 115,
        380 : 122,
        378 : 122,
        322 : 108,
        243 : 111}
    
    new_text = text.lower()
    new_text = new_text.replace("\n", "")
    new_text = new_text.replace(" ", "")
    new_text = new_text.translate(replace_dic)
    
    return new_text


def compare_strings_histogram_method(ground_truth, ocr_result):
    truth_map = {}
    ocr_result_map = {}
    for char_t, char_ocr in zip(ground_truth, ocr_result):
        if char_t in truth_map: truth_map[char_t] += 1
        else: truth_map[char_t] = 1
            
        if char_ocr in ocr_result_map: ocr_result_map[char_ocr] += 1
        else: ocr_result_map[char_ocr] = 1
    
    x_true = list(truth_map.keys())
    y_true = list(truth_map.values())
    x_test = list(ocr_result_map.keys())
    y_test = list(ocr_result_map.values())
    
    sns.set_style(style='darkgrid')
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    axes[0].set_title('Ground Truth Character Histogram')
    sns.barplot(x=x_true, y=y_true, hue=y_true, ax=axes[0], legend=False)
    axes[0].set_xlabel('Characters')
    axes[0].set_ylabel('Frequency')
    
    sns.set_style(style='darkgrid')
    sns.barplot(x=x_test, y=y_test, hue=y_test, ax=axes[1], legend=False)
    axes[0].set_xlabel('Characters')
    axes[0].set_ylabel('Frequency')
    
    plt.show()


def compare_strings_levenshtein(ground_truth, ocr_result):
    
    

files_list = os.listdir('results//')

for i in range(len(files_list)):
    files_list[i] = os.path.join('results//', files_list[i])

validation = files_list[-1]
tests = files_list[:-1]


with open(validation, 'r', encoding='utf-8') as f:
    ground_truth = f.read()
    f.close()
    
for test in tests:
    with open(test, 'r', encoding='utf-8') as f:
        sample = f.read()     
        f.close()
    

ground_truth = format_text(ground_truth)
sample = format_text(sample)

compare_strings_histogram_method(ground_truth, sample)
