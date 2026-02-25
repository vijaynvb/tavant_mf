#pip install azure-cognitiveservices-vision-computervision
# pip install Pillow

# Computer vision detect landmarks
from azure.cognitiveservices.vision.computervision import ComputerVisionClient 
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
import dotenv
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image 
import sys
import time
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.getenv("KEY")  # Replace with your key
endpoint = os.getenv("ENDPOINT")  # Replace with your endpoint

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

IMAGES = [ 
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/taj_new_contant_edited.jpg",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/BennelongPoint.jpg",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/GoldenGateBridge.webp",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/LondonTowerBridge.jpg",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/londonbridge2.jpg"
           ]

# Call API with content type (landmarks) and URL
for image_url in IMAGES:
    detect_domain_results_landmarks = computervision_client.analyze_image_by_domain("landmarks", image_url)
    print("###### Computer Vision - Domain specific content - Landmarks #######")
    print("Landmarks in the remote image:")
    if len(detect_domain_results_landmarks.result["landmarks"]) == 0:
        print("No landmarks detected.")
    else:
        for landmark in detect_domain_results_landmarks.result["landmarks"]:
            print(landmark["name"])