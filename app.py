import streamlit as st
from PIL import Image
import numpy as np
import glob

# main.py
import argparse
import sys
from pathlib import Path

from src.entry import entry_point
from src.logger import logger

import streamlit as st
import os
from PIL import Image
import numpy as np
import pandas as pd

# Function to perform operations on the uploaded image
def apply_OMR(sample_path):

    # defin require arguments for omr checker
    args = parse_args(sample_path)
    entry_point_for_args(args)

    file_list = glob.glob('./samples/'+selected_sample+"/*")
    folder_list = [item for item in file_list if os.path.isdir(item)]
    folder_names = [os.path.basename(folder) for folder in folder_list]
    
    st.header("CSV Resulted Outputs:")
    if sample_path.split("/")[-1].startswith("sample4"):
        csv_file = glob.glob("outputs/"+"/Results"+"/*.csv")
        st.dataframe(pd.read_csv(csv_file[-1]))
    else:
        for file in folder_names:
            st.write("Resulted CSV Output Path:", "outputs/"+file+"/Results")
            csv_file = glob.glob("outputs/"+file+"/Results"+"/*.csv")
            st.dataframe(pd.read_csv(csv_file[-1]))
            # st.write("csv files:",csv_file[-1])

def parse_args(path):
    # construct the argument parse and parse the arguments
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        "-i",
        "--inputDir",
        default=[f"{path}"],
        # https://docs.python.org/3/library/argparse.html#nargs
        nargs="*",
        required=False,
        type=str,
        dest="input_paths",
        help="Specify an input directory.",
    )

    argparser.add_argument(
        "-d",
        "--debug",
        required=False,
        dest="debug",
        action="store_false",
        help="Enables debugging mode for showing detailed errors",
    )

    argparser.add_argument(
        "-o",
        "--outputDir",
        default="outputs",
        required=False,
        dest="output_dir",
        help="Specify an output directory.",
    )

    argparser.add_argument(
        "-a",
        "--autoAlign",
        required=False,
        dest="autoAlign",
        action="store_true",
        help="(experimental) Enables automatic template alignment - \
        use if the scans show slight misalignments.",
    )

    argparser.add_argument(
        "-l",
        "--setLayout",
        required=False,
        dest="setLayout",
        action="store_true",
        help="Set up OMR template layout - modify your json file and \
        run again until the template is set.",
    )

    (
        args,
        unknown,
    ) = argparser.parse_known_args()

    args = vars(args)

    if len(unknown) > 0:
        logger.warning(f"\nError: Unknown arguments: {unknown}", unknown)
        argparser.print_help()
        exit(11)
    return args


def entry_point_for_args(args):
    if args["debug"] is True:
        # Disable tracebacks
        sys.tracebacklimit = 0
    for root in args["input_paths"]:
        entry_point(
            Path(root),
            args,
        )

st.title("OMR Checker")


# Create a dropdown menu with six values
selected_sample = st.selectbox("Select a sample:", ["sample1", "sample2", "sample3", "sample4", "sample5", "sample6"])

if selected_sample:
    if os.path.exists('./samples/'+selected_sample):
        if st.button("Apply OMR"):
            apply_OMR('./samples/'+selected_sample)
    else:
        st.warning("Folder path does not exist. Please enter a valid path.")


# file_list = glob.glob('./samples/'+selected_sample+"/*")
# # Filter out only the directories
# folder_list = [item for item in file_list if os.path.isdir(item)]

# # Extract just the folder names
# folder_names = [os.path.basename(folder) for folder in folder_list]
# st.write(folder_names)


# # csv reader
# # Create a file upload widget
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# # Check if a file is uploaded
# if uploaded_file is not None:
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(uploaded_file)

#     # Display the DataFrame as a table
#     st.write("CSV Data:")
#     st.dataframe(df)