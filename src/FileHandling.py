import pandas as pd
import json 
import os

class FileHandling:
    
    def __init__(self, source_file_directory:str, destination_file_directory:str) -> None:
        """ 
        Sets the source folder - the folder with the source files
        and sets the destination folder - the folder to save the files
        """
        self.source_file_directory = source_file_directory
        self.destination_file_directory = destination_file_directory
    
    def upload_data_file(self, file_name: str) -> pd.DataFrame:
        """
        Gets a file name and concatenates it with the source file path and uploads the file.
        """
        os.makedirs(self.source_file_directory, exist_ok=True)
        file = os.path.join(self.source_file_directory, file_name)
        return pd.read_csv(file)
    
    def saving_data_file(self, file_name: str, data:pd.DataFrame) -> None:
        """ 
        Gets a file and a filename, concatenates it with the destination folder path and saves the file. 
        """
        os.makedirs(self.destination_file_directory, exist_ok=True)
        file = os.path.join(self.destination_file_directory, f"{file_name}.csv")
        data.to_csv(file, index=False)
            
    def saving_results_json(self, file_name: str, results:dict) -> None:
        """ 
        Gets a file and a filename, concatenates it with the path to the destination folder and saves the file as a .jsun file. 
        """
        os.makedirs(self.destination_file_directory, exist_ok=True)
        
        with open(file= os.path.join(self.destination_file_directory, f"{file_name}.json") , mode="w", encoding="utf-8") as file:
            json.dump(obj=results, fp=file, indent=4)



    