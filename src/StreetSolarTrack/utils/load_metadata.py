import pandas as pd
import os
from PIL import Image
from PIL.ExifTags import TAGS


#  添加一个load folder 函数，读取文件夹下所有的图片为一个df，df中存储图片的metadata，包括名称，大小，格式，mode，exif，以及对应的folder 的路径等
# 
def load_folder(folder_path):
    """
    Load metadata from all images in the specified folder into a DataFrame.

    Args:
        folder_path (str): The path to the folder containing images.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted metadata for all images.
    """
    metadata_list = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(folder_path, filename)
            metadata = load_image_metadata(file_path)
            metadata['name'] = filename
            metadata['folder'] = folder_path
            metadata_list.append(metadata)

    return pd.DataFrame(metadata_list)

def load_images_metadata(folder_path):
    """
    Load metadata from all images in the specified folder and generate a report.

    Args:
        folder_path (str): The path to the folder containing images.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted metadata for all images.
    """
    df = load_folder(folder_path)

    # Generate an HTML report from the DataFrame
    report_path = os.path.join(folder_path, 'metadata_report.html')
    with open(report_path, 'w', encoding='utf-8') as report_file:
        report_file.write('<h1>Image Metadata Analysis Report</h1>\n')
        report_file.write(df.to_html(index=False))

    return df

def load_image_metadata(file_path):
    """
    Load metadata from the specified image file into a dictionary.

    Args:
        file_path (str): The path to the image file.

    Returns:
        dict: A dictionary containing the extracted metadata.
    """
    image = Image.open(file_path)
    metadata = {}

    # Extract basic image details
    metadata['format'] = image.format
    metadata['mode'] = image.mode
    metadata['size'] = image.size

    # Extract EXIF data if available
    if hasattr(image, '_getexif'):
        exif_data = image._getexif()
        if exif_data is not None:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = value

    return metadata
