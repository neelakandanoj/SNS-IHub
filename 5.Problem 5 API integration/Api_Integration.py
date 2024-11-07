import requests

def fetch_news(topic):
    """
    Fetches top news headlines based on a user-defined topic using the News API.
    
    Parameters:
    - topic (str): The topic or keyword to search for in the news.

    Returns:
    - list: A list of dictionaries containing news articles if successful; None if an error occurs.
    """
    # Define the API endpoint and parameters
    api_key = "b02ded4ef5a6452793deff6719c0b6bd"  # Replace with your News API key
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "apiKey": api_key,
        "language": "en",
        "pageSize": 5  # Limit to 5 articles for simplicity
    }

    try:
        # Make a GET request to the API
        response = requests.get(url, params=params)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check for API-specific errors
        if data.get("status") != "ok":
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None

        # Extract relevant information from each article
        articles = []
        for article in data["articles"]:
            articles.append({
                "Title": article["title"],
                "Description": article["description"],
                "URL": article["url"],
                "Published At": article["publishedAt"]
            })

        return articles

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    
    return None

def display_news(topic):
    """
    Fetches and displays news headlines for a specified topic.

    Parameters:
    - topic (str): The topic to search news articles for.
    """
    news_articles = fetch_news(topic)
    
    if news_articles:
        print("\nTop News Headlines:")
        for i, article in enumerate(news_articles, start=1):
            print(f"\nArticle {i}:")
            print(f"Title: {article['Title']}")
            print(f"Description: {article['Description']}")
            print(f"URL: {article['URL']}")
            print(f"Published At: {article['Published At']}")
    else:
        print("Could not fetch news articles. Please try again.")

# Example usage
topic = input("Enter the topic for news search: ")
display_news(topic)
