import wikipedia

def get_wikipedia_categories(topic):
    """
    Fetches the categories of a given Wikipedia page.
    :param topic: Topic to fetch categories for
    """
    try:
        page = wikipedia.page(topic)
        return page.categories
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    topic = "Python programming language"
    print(get_wikipedia_categories(topic))
