from regex_explorer import RegexExplorer
import os
import shutil

def convert_to_BIDS(data, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for item in data:
        source_path = item['source_path']
        subject_id = item['subject_id']
        acquisition_type = item['acquisition_type']
        ext = os.path.splitext(source_path)[1]
        bids_path = f"sub_{subject_id}/anat/sub_{subject_id}-acq_{acquisition_type}{ext}"
        dest_path = os.path.join(output_folder, bids_path)

        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        shutil.copy2(source_path, dest_path)

explorer = RegexExplorer('sourcedata/', 'config.json')
data = explorer.extract_info()
convert_to_BIDS(data, output_folder='rawdata/')
