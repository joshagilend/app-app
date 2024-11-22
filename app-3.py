import wikipedia

def get_related_topics(topic, max_links=10):
    """
    Fetches related topics from a Wikipedia page.
    :param topic: Wikipedia page topic
    :param max_links: Maximum number of related topics to fetch
    """
    try:
        page = wikipedia.page(topic)
        return page.links[:max_links]
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    topic = "Python programming language"
    print(get_related_topics(topic))
