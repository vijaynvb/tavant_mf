import os


def analyze_identity_documents():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient
    from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest

    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = "https://vijaytavant.cognitiveservices.azure.com/"
    key = "xxxxxxxxxxxxxxxxx"   

    document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Analyze a document at a URL:
    local_file_path = "./Docs/identity_documents.png"
    # Replace with your actual identityUrl:
    with open(local_file_path, "rb") as f:
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-idDocument",
            AnalyzeDocumentRequest(bytes_source=f.read())
        )    

    # # If analyzing a local document, remove the comment markers (#) at the beginning of these 8 lines.
    # # Delete or comment out the part of "Analyze a document at a URL" above.
    # # Replace <path to your sample file>  with your actual file path.
    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_intelligence_client.begin_analyze_document(
    #         "prebuilt-idDocument", analyze_request=f, content_type="application/octet-stream"
    #     )
    id_documents: AnalyzeResult = poller.result()

    # [START analyze_idDocuments]
    if id_documents.documents:
        for idx, id_document in enumerate(id_documents.documents):
            print(f"--------Analyzing ID document #{idx + 1}--------")
            if id_document.fields:
                first_name = id_document.fields.get("FirstName")
                if first_name:
                    print(f"First Name: {first_name.get('valueString')} has confidence: {first_name.confidence}")
                last_name = id_document.fields.get("LastName")
                if last_name:
                    print(f"Last Name: {last_name.get('valueString')} has confidence: {last_name.confidence}")
                document_number = id_document.fields.get("DocumentNumber")
                if document_number:
                    print(
                        f"Document Number: {document_number.get('valueString')} has confidence: {document_number.confidence}"
                    )
                dob = id_document.fields.get("DateOfBirth")
                if dob:
                    print(f"Date of Birth: {dob.get('valueDate')} has confidence: {dob.confidence}")
                doe = id_document.fields.get("DateOfExpiration")
                if doe:
                    print(f"Date of Expiration: {doe.get('valueDate')} has confidence: {doe.confidence}")
                sex = id_document.fields.get("Sex")
                if sex:
                    print(f"Sex: {sex.get('valueString')} has confidence: {sex.confidence}")
                address = id_document.fields.get("Address")
                if address:
                    print(f"Address: {address.get('valueString')} has confidence: {address.confidence}")
                country_region = id_document.fields.get("CountryRegion")
                if country_region:
                    print(
                        f"Country/Region: {country_region.get('valueCountryRegion')} has confidence: {country_region.confidence}"
                    )
                region = id_document.fields.get("Region")
                if region:
                    print(f"Region: {region.get('valueString')} has confidence: {region.confidence}")
    # [END analyze_idDocuments]

if __name__ == "__main__":
    from azure.core.exceptions import HttpResponseError
    # from dotenv import find_dotenv, load_dotenv

    try:
        # load_dotenv(find_dotenv())
        analyze_identity_documents()
    except HttpResponseError as error:
        # Examples of how to check an HttpResponseError
        # Check by error code:
        if error.error is not None:
            if error.error.code == "InvalidImage":
                print(f"Received an invalid image error: {error.error}")
            if error.error.code == "InvalidRequest":
                print(f"Received an invalid request error: {error.error}")
            # Raise the error again after printing it
            raise
        # If the inner error is None and then it is possible to check the message to get more information:
        if "Invalid request".casefold() in error.message.casefold():
            print(f"Uh-oh! Seems there was an invalid request: {error}")
        # Raise the error again
        raise
