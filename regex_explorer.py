import re
import json
import os
import csv

class RegexExplorer:
    def __init__(self, input_folder, config_file):
        self.input_folder = input_folder
        self.config_file = config_file
        self.patterns = self.load_patterns()

    def load_patterns(self):
        with open(self.config_file, "r") as f:
            return json.load(f)

    def extract_info(self):
        extracted = []
        metadata = None
        for root, _, files in os.walk(self.input_folder):
            for filename in files:
                pattern = self.patterns["subject_id_regex"]
                match = re.search(pattern, filename)
                if not match:
                    print(f"Failed to match {filename}")
                if match:
                    seg_acquisition_type = None
                    subject_id = match.group(0)
                    if re.findall(self.patterns["seg_regex"], filename):
                        acquisition_type = "seg"
                        if re.search(self.patterns["T1_regex"], filename):
                            seg_acquisition_type = "T1w"
                        if re.search(self.patterns["FLAIR_regex"], filename):
                            seg_acquisition_type = "FLAIR"
                        if re.search(self.patterns["CT_regex"], filename):
                            seg_acquisition_type = "CT"
                    elif re.search(self.patterns["T1_regex"], filename):
                        acquisition_type = "T1w"
                    elif re.search(self.patterns["T2star_regex"], filename):
                        acquisition_type = "T2starw"
                    elif re.search(self.patterns["T2_regex"], filename):
                        acquisition_type = "T2w"
                    elif re.search(self.patterns["FLAIR_regex"], filename):
                        acquisition_type = "FLAIR"
                    elif re.search(self.patterns["CT_regex"], filename):
                        acquisition_type = "CT"
                    else:
                        acquisition_type = "Unknown"
                    
                    extracted.append({
                            "subject_id": subject_id,
                            "acquisition_type": acquisition_type,
                            "seg_acquisition_type": seg_acquisition_type,
                            "filename": filename,
                            "source_path": os.path.join(root, filename)
                        })
        metadata = None
        for root, _, files in os.walk(self.input_folder):
            for filename in files:
                match = re.match(self.patterns["metadata_regex"], filename)
                if match:
                    metadata_file = match.group(0)
                    metadata = os.path.join(root, metadata_file)
                    break
            if metadata is not None : break
        if metadata is not None : metadata = os.path.join(root, metadata_file)
        return extracted, metadata

    def print_results(self):
        results = self.extract_info()
        print(f"Found {len(results)} files")
        for result in results:
            print(result)