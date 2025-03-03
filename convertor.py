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
        seg_acquisition_type = item['seg_acquisition_type']

        if acquisition_type == "seg":
            ext = os.path.splitext(source_path)[1]
            bids_path = f"derivatives/sub-{subject_id}/anat/sub-{subject_id}_acq-{seg_acquisition_type}_seg{ext}"
            dest_path = os.path.join(output_folder, bids_path)
        else:
            ext = os.path.splitext(source_path)[1]
            bids_path = f"rawdata/sub-{subject_id}/anat/sub-{subject_id}_acq-{acquisition_type}{ext}"
            dest_path = os.path.join(output_folder, bids_path)

        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        shutil.copy2(source_path, dest_path)

explorer = RegexExplorer('sourcedata/', 'config.json')
data = explorer.extract_info()
convert_to_BIDS(data, output_folder='BIDS/')
