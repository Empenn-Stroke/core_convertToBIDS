from regex_explorer import RegexExplorer
import os
import shutil
import argparse

def convert_to_BIDS(data, metadata, sourcedata_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for item in data:
        source_path = item['source_path']
        subject_id = item['subject_id']
        acquisition_type = item['acquisition_type']
        seg_acquisition_type = item['seg_acquisition_type']

        if acquisition_type == "seg":
            ext = os.path.splitext(source_path)[1]
            if ext == ".gz": ext = ".nii.gz"
            bids_path = f"derivatives/sub-{subject_id}/anat/sub-{subject_id}_acq-{seg_acquisition_type}_seg{ext}"
            dest_path = os.path.join(output_folder, bids_path)
        else:
            ext = os.path.splitext(source_path)[1]
            if ext == ".gz": ext = ".nii.gz"
            bids_path = f"rawdata/sub-{subject_id}/anat/sub-{subject_id}_acq-{acquisition_type}{ext}"
            dest_path = os.path.join(output_folder, bids_path)

        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        shutil.copy2(source_path, dest_path)

        if metadata is not None:
            ext = os.path.splitext(metadata)[-1]
            metadata_dest = os.path.join(output_folder, "rawdata/participants"+ext)
            metadata_dir = os.path.dirname(metadata_dest)
            if not os.path.exists(metadata_dir):
                os.makedirs(metadata_dir)
            shutil.copy2(metadata, metadata_dest)
    sourcedata_dest = os.path.join(output_folder, "sourcedata")
    if not os.path.exists(sourcedata_dest):
        os.makedirs(sourcedata_dest)
    for item in os.listdir(sourcedata_folder):
        s = os.path.join(sourcedata_folder, item)
        d = os.path.join(sourcedata_dest, item)
        if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
     
def main():
    parser = argparse.ArgumentParser(description="Convert data to BIDS format")
    parser.add_argument('--sourcedata', type=str, required=True, help='Path to the source data folder')
    parser.add_argument('--output', type=str, required=True, help='Path to the output folder')
    parser.add_argument('--config', type=str, required=True, help='Path to the configuration file')
    args = parser.parse_args()

    explorer = RegexExplorer(args.sourcedata, args.config)
    data, metadata = explorer.extract_info()
    convert_to_BIDS(data, metadata, sourcedata_folder=args.sourcedata, output_folder=args.output)

if __name__ == "__main__":
    main()