from googlesearch import search

def google_search_results(query, num_results=5):
    """
    Fetches the top search results for a query using Google Search.
    :param query: Search term
    :param num_results: Number of results to fetch
    """
    try:
        results = list(search(query, num_results=num_results))
        return results
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    query = "Python programming tutorials"
    print(google_search_results(query))
