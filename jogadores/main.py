import argparse
import logging
from typing import TypedDict
from pathlib import Path
import boto3
from botocore.exceptions import BotoCoreError
from PIL import Image, ImageDraw, UnidentifiedImageError


logging.basicConfig(level=logging.INFO)
client = boto3.client("rekognition")

class BoundingBoxType(TypedDict):
    Left: float
    Top: float
    Width: float
    Height: float

def validate_image(path: str) -> bool:
    try:
        Image.open(path).verify()
        return True
    except UnidentifiedImageError:
        logging.error(f"Arquivo inválido: {path}")
        return False

def compare_faces(source_path: str, target_path: str, threshold: int = 80):
    if not all(validate_image(p) for p in [source_path, target_path]):
        return None

    try:
        with open(source_path, "rb") as src, open(target_path, "rb") as tgt:
            return client.compare_faces(
                SourceImage={"Bytes": src.read()},
                TargetImage={"Bytes": tgt.read()},
                SimilarityThreshold=threshold,
            )
    except BotoCoreError as e:
        logging.error(f"Erro no AWS Rekognition: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--output", default="result.jpg")
    parser.add_argument("--threshold", type=int, default=80)
    args = parser.parse_args()

    response = compare_faces(args.source, args.target, args.threshold)
    if response and response.get("FaceMatches"):
        draw_boxes(args.target, args.output, response["FaceMatches"])