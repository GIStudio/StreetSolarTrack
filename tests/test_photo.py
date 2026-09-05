# test_photo.py
import sys
import os

# 将项目根目录添加到 sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from StreetSolarTrack.utils.photo import Photo
from StreetSolarTrack.utils.load_metadata import load_images_metadata, load_folder
import tempfile
import pandas as pd
import shutil
from PIL import Image


def test_analyze_metadata():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate 90 to 110 random images
        import random
        for _ in range(random.randint(90, 110)):
            width = random.randint(1, 1024)
            height = random.randint(1, 1024)
            dummy_image_path = os.path.join(temp_dir, f'random_image_{_}.jpg')
            image = Image.new('RGB', (width, height))
            image.save(dummy_image_path)

        # Call load_images_metadata to gather the metadata
        df = load_images_metadata(temp_dir)
        print(df.head())

        # Check if the report file was created
        report_path = os.path.join(temp_dir, 'metadata_report.html')
        assert os.path.exists(report_path), "Report file not generated."

        # Optionally: verify basic report content (e.g. title)
        with open(report_path, 'r') as file:
            report_content = file.read()
            assert "<h1>Image Metadata Analysis Report</h1>" in report_content, "Report content is missing the title."

def test_load_folder():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate 5 dummy images
        for i in range(5):
            dummy_image_path = os.path.join(temp_dir, f'dummy_image_{i}.jpg')
            image = Image.new('RGB', (100, 100))
            image.save(dummy_image_path)

        # Call load_folder to gather the metadata
        df = load_folder(temp_dir)

        # Check if the DataFrame is not empty
        assert not df.empty, "DataFrame should not be empty."

        # Verify metadata for the first image
        assert len(df) == 5, "DataFrame should contain 5 entries."
        assert df['name'].iloc[0] == 'dummy_image_0.jpg', "First image name should match."
        assert df['folder'].iloc[0] == temp_dir, "First image folder path should match."

    print("All tests passed!")

if __name__ == '__main__':
    test_analyze_metadata()
    test_load_folder()
    test_analyze_metadata()
