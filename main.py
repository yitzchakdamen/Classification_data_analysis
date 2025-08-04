from src.SystemManagement import SystemManagement


if __name__ == "__main__":
    system_management = SystemManagement(source_file_directory="data", destination_file_directory="results")
    system_management.activation(upload_file_name="tweets_dataset.csv",cleaningd_file_name="cleaningd_tweets_dataset",
                                analysis_results_file_name="analysis_cleaningd", relevant_columns=["Text", "Biased"])
    





