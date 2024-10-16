# Import necessary libraries
from azure.search.documents import SearchClient
from azure.core.exceptions import ClientAuthenticationError
from azure.identity import ManagedIdentityCredential

# Define Azure Cognitive Search settings
search_service_name = "test-cognitivesearch01"
search_index_name = "hotels-sample-index"

# Managed Identity client ID (user-assigned Managed Identity)
user_assigned_mi_client_id = "mi-28227802bs"  # Replace with your Managed Identity's client ID

# Build the Azure Search endpoint
endpoint = f"https://{search_service_name}.search.windows.net"

# Authenticate using Managed Identity (User-assigned Managed Identity)
credential = ManagedIdentityCredential(client_id=user_assigned_mi_client_id)

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
