from src.FileHandling import FileHandling








print("---- testing a ----")
file_handling = FileHandling(r"data", r"results")
data = file_handling.upload_data_file("tweets_dataset.csv")
file_handling.saving_data_file("test",data)
file_handling.saving_results_json("aa", {"aaa":444})
