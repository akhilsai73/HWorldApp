import os
from azure.search.documents import SearchClient
from azure.core.exceptions import ClientAuthenticationError
from azure.identity import ManagedIdentityCredential

# Retrieve environment variables
search_service_name = os.getenv("test-cognitivesearch01")
search_index_name = os.getenv("hotels-sample-index")

# Check if environment variables are correctly set
if not search_service_name or not search_index_name:
    raise ValueError("Please set the SEARCH_SERVICE_NAME and SEARCH_INDEX_NAME environment variables.")

# Build the Azure Search endpoint
endpoint = f"https://{search_service_name}.search.windows.net"

# Authenticate using Managed Identity (System-assigned or User-assigned Managed Identity)
credential = ManagedIdentityCredential()

# Create a search client
search_client = SearchClient(endpoint=endpoint, index_name=search_index_name, credential=credential)

# Function to perform a search query
def search_documents(query):
    try:
        print(f"Searching for: '{query}'\n")
        results = search_client.search(search_text=query)
        
        # Display results and inspect structure
        for result in results:
            print(result)
    
    except ClientAuthenticationError as e:
        print("Authentication failed: Please check your Managed Identity and permissions.")
        print(f"Error details: {e}")

# Take user input for search query
search_query = input("Enter search query: ")

# Perform the search and display the results
search_documents(search_query)
