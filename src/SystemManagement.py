import pandas as pd
from src.DataAnalyzer import DataAnalyzer
from src.FileHandling import FileHandling
from src.ReportBuilder import ReportBuilder
from src.DataCleaning import DataCleaning

class SystemManagement:
    
    def __init__(self, source_file_directory:str, destination_file_directory:str) -> None:
        self.file_handling = FileHandling(source_file_directory, destination_file_directory)
        self.data = None
    
    def upload_data_file(self, file_name) -> None:
        self.data:pd.DataFrame = self.file_handling.upload_data_file(file_name)
    
    def run_analysis(self) -> dict:
        if self.data is not None:
            data_analyzer = DataAnalyzer(self.data)
            return ReportBuilder.bild(
                data_analyzer.most_10_common_words_by_category(),
                data_analyzer.most_3_longest_tweets_text_by_category(),
                data_analyzer.sum_tweets(),
                data_analyzer.average_word_length_by_category(),
                data_analyzer.sum_uppercase_words_by_category(),
            )

    def run_cleaning(self, relevant_columns:list) -> pd.DataFrame:
        if self.data is not None:
            data_cleaning:pd.DataFrame = DataCleaning(self.data, relevant_columns).activation()
            return data_cleaning
    
    def export_investigation(self, file_name, data_cleaning:pd.DataFrame) -> None:
        self.file_handling.saving_data_file(file_name, data_cleaning)
            
    def exportcleaning_results(self, file_name, analysis_results:dict) -> None:
        self.file_handling.saving_results_json(file_name, analysis_results)
    
    def activation(self, upload_file_name:str, cleaningd_file_name:str ,analysis_results_file_name:str,  relevant_columns:list):
        self.upload_data_file(upload_file_name)
        analysis_results = self.run_analysis()
        data_cleaning: pd.DataFrame = self.run_cleaning(relevant_columns)
        self.export_investigation(cleaningd_file_name, data_cleaning)
        self.exportcleaning_results(analysis_results_file_name,analysis_results)
            