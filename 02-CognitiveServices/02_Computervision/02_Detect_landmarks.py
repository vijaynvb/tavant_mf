# Computer vision detect landmarks
from azure.cognitiveservices.vision.computervision import ComputerVisionClient #pip install azure-cognitiveservices-vision-computervision
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Replace with your key
endpoint = "https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.cognitiveservices.azure.com/" # Replace with your endpoint

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

IMAGES = [ "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/TajMahal.avif",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/BennelongPoint.jpg",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/GoldenGateBridge.webp",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/LondonTowerBridge.jpg",
           "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/LondonTowerBridge1.avif",]

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