import argparse
from utils.data_preprocessing.extract_semeval_PT_data import extract_semeval_PT_data
from utils.data_preprocessing.extract_sample1_DR_data import extract_sample1_DR_data
from utils.data_preprocessing.pool_data_and_log_results import pool_data_and_log_results
from utils.data_preprocessing.count_pt_and_dr import save_pt_and_dr_pivot_tables
from DR_parsers.semeval_datasets_DR_parser_with_LLM import semeval_datasets_DR_parser
from DR_parsers.PDTB_DR_parser_with_LLM import parser_DR_with_LLM
from evaluation.evaluate_DR_parser_lvl2 import evaluate_DR_parser_with_f1
from statistics_module.perform_statistical_analysis import perform_statistical_analysis

parser = argparse.ArgumentParser(description='Run parts of the script based on flags provided.')
parser.add_argument('--preprocess', action='store_true', help='Run data preprocessing')
parser.add_argument('--parseDR', action='store_true', help='Run DR parsing')
parser.add_argument('--evaluateDRParsers', action='store_true', help='Run evaluation')
parser.add_argument('--parsePTForDR', action='store_true', help='Parse PT dataset for DR') 
parser.add_argument('--poolDatasets', action='store_true', help='Pool datasets')
parser.add_argument('--performStatistics', action='store_true', help='Pool datasets')


args = parser.parse_args()

if args.preprocess:
    # extract_semeval_PT_data()  # You need to have access to the SemEval dataset, not included in this repository
    extract_sample1_DR_data()  

elif args.parseDR:
    parser_DR_with_LLM()

elif args.parsePTForDR:
    semeval_datasets_DR_parser()

elif args.evaluateDRParsers:
    evaluate_DR_parser_with_f1()

elif args.poolDatasets:
    pool_data_and_log_results()
    save_pt_and_dr_pivot_tables()

elif args.performStatistics:
    perform_statistical_analysis()









