#pip install azure-cognitiveservices-vision-computervision 
#pip install azure-ai-vision-imageanalysis

# Docs
# https://learn.microsoft.com/en-us/python/api/azure-ai-vision-imageanalysis/azure.ai.vision.imageanalysis.imageanalysisclient?view=azure-python

import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient   #cl     
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:

load_dotenv()

endpoint = os.getenv("ENDPOINT")  # Replace with your endpoint
key = os.getenv("KEY")  # Replace with your key


# Create an Image Analysis client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Define image URL
image_url = "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/sample.jpg"

# Analyze all visual features from an image stream. This will be a synchronously (blocking) call.

visual_features =[
        VisualFeatures.TAGS,
        VisualFeatures.OBJECTS,
        # VisualFeatures.CAPTION,
        # VisualFeatures.DENSE_CAPTIONS,
        VisualFeatures.READ,
        VisualFeatures.SMART_CROPS,
        VisualFeatures.PEOPLE,
    ]

# Analyze all visual features from an image stream. This will be a synchronously (blocking) call.
result = client.analyze_from_url(
    image_url=image_url,
    visual_features=visual_features,
    smart_crops_aspect_ratios=[0.9, 1.33],
    gender_neutral_caption=True,
    language="en"
)



# Print all analysis results to the console
print("Image analysis results:")

if getattr(result, "caption", None) is not None and result.caption is not None:
    print(" Caption:")
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

if getattr(result, "dense_captions", None) is not None and result.dense_captions is not None:
    print(" Dense Captions:")
    for caption in result.dense_captions.list:
        print(f"   '{caption.text}', {caption.bounding_box}, Confidence: {caption.confidence:.4f}")

if result.read is not None:
    # Some images may return an empty list of blocks; guard against IndexError
    print(" Read:")
    if getattr(result.read, "blocks", None):
        for block in result.read.blocks:
            if not getattr(block, "lines", None):
                continue
            for line in block.lines:
                print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
                if getattr(line, "words", None):
                    for word in line.words:
                        print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")
    else:
        print("   No text detected in the image.")

if result.tags is not None:
    print(" Tags:")
    for tag in result.tags.list:
        print(f"   '{tag.name}', Confidence {tag.confidence:.4f}")

if result.objects is not None:
    print(" Objects:")
    for object in result.objects.list:
        print(f"   '{object.tags[0].name}', {object.bounding_box}, Confidence: {object.tags[0].confidence:.4f}")

if result.people is not None:
    print(" People:")
    for person in result.people.list:
        print(f"   {person.bounding_box}, Confidence {person.confidence:.4f}")

if result.smart_crops is not None:
    print(" Smart Cropping:")
    for smart_crop in result.smart_crops.list:
        print(f"   Aspect ratio {smart_crop.aspect_ratio}: Smart crop {smart_crop.bounding_box}")

print(f" Image height: {result.metadata.height}")
print(f" Image width: {result.metadata.width}")
print(f" Model version: {result.model_version}")