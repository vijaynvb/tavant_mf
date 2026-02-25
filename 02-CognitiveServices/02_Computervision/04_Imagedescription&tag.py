from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from dotenv import load_dotenv
from msrest.authentication import CognitiveServicesCredentials

import os

load_dotenv()

subscription_key = os.getenv("KEY")  # Replace with your key
endpoint = os.getenv("ENDPOINT")  # Replace with your endpoint

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = "https://raw.githubusercontent.com/vijaynvb/tavant_mf/main/Docs/taj_new_contant_edited.jpg"

print("********Describe an image - remote*********")
# Call ComputerVision API
description_results = computervision_client.describe_image(remote_image_url)

# Get the captions (descriptions) from the response, with confidence level
print("Description of remote image: ")
if len(description_results.captions) == 0:
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()

print("===== Tag an image - remote =====")
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url)

# Print results with confidence score
print("Tags in the remote image: \n")
if len(tags_result_remote.tags) == 0:
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
