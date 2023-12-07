from pathlib import Path
import argparse
import sys, os


class ProjectConfig():
    def __init__(self) -> None:
        self.parse_arguments()
        self.generate_paths()


    def parse_arguments(self) -> None:
        # Argument parser
        parser = argparse.ArgumentParser()

        #Specifying the arguments that need to be inserted
        parser.add_argument('--raw_dataset_name', type=str, help='The name of the raw dataset file', default='dataset.csv')
        parser.add_argument('--processed_dataset_name', type=str, help='The name of the raw dataset file', default='dataset.csv')
        # Add logic for when .csv is missing in the file name


        #Parsing and controlling the arguments
        self.args = parser.parse_args()
    
    def generate_paths(self) -> None:
        self.project_dir = Path(__file__).resolve().parents[2] # adjust whenever moving to another folder or file
        self.src_dir = Path(__file__).resolve().parents[1] # adjust whenever moving to another folder or file

        # Insert Project Path into PATH
        sys.path.insert(0, str(self.src_dir))
        print(f'{self.src_dir} inserted into PATH')


        self.raw_data_dir = self.project_dir / "data" / "raw"
        self.raw_data_dir.mkdir(parents=True, exist_ok=True)

        self.interim_data_dir = self.project_dir / "data" / "interim"
        # self.interim_data_dir.mkdir(parents=True, exist_ok=True)
        
        self.processed_data_dir = self.project_dir / "data" / "processed"
        # self.processed_data_dir.mkdir(parents=True, exist_ok=True)
        
        self.external_data_dir = self.project_dir / "data" / "external"
        # self.external_data_dir.mkdir(parents=True, exist_ok=True)
        
        self.results_dir = self.project_dir / "reports"
        # self.results_dir.mkdir(parents=True, exist_ok=True)

        self.img_dir = self.results_dir / "img"
        # self.img_dir.mkdir(parents=True, exist_ok=True)


        self.dataset_name = self.args.raw_dataset_name 
        self.processed_dataset_name = self.args.processed_dataset_name

