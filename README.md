# core_convertToBIDS
This repo converts non-BIDS compliant datasets into BIDS compliant datasets.

## Requirements
- Python Python 3.12.9 or higher

## How to use
1. Clone the repository:
    ```sh
    git clone https://github.com/Empenn-Stroke/core_convertToBIDS.git
    cd core_convertToBIDS
    ```

2. Prepare your configuration file **config.json** with the appropriate regex patterns.
    - **subject_id_regex**: Regex pattern to identify subject IDs
    - **T1_regex**: Regex pattern to identify T1-weighted images
    - **FLAIR_regex**: Regex pattern to identify FLAIR images
    - **T2star_regex**: Regex pattern to identify T2* images
    - **T2_regex**:  Regex pattern to identify T2-weighted images
    - **seg_regex**: Regex pattern to identify lesion mask segmentations
    - **CT_regex**: Regex pattern to identify CT images
    - **metadata_regex**: Regex pattern to identify metadata files

    Here is an example:
    ```json
    {
        "subject_id_regex": "r\\d{3}s\\d{3}",
        "T1_regex": "T1|T13D|t1",
        "FLAIR_regex": "FLAIR|flair|flaire|Flair",
        "T2star_regex": "T2star|T2etoile",
        "T2_regex": "T2",
        "seg_regex": "lesion_mask",
        "CT_regex": "CT",
        "metadata_regex": "20220425_ATLAS_2.0_MetaData.xlsx"
    }
    ```

3. Run the conversion script:
    ```sh
    python convertor.py --sourcedata /path/to/source/data --output /path/to/output/folder --config /path/to/config.json
    ```

## Example
```sh
python convertor.py --sourcedata ATLAS2/ --output ATLAS2_BIDS/ --config config_ATLAS.json
```
