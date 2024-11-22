import wikipedia

def get_wikipedia_summary(topic, sentences=2):
    """
    Fetches the summary of a topic from Wikipedia.
    :param topic: Topic to search on Wikipedia
    :param sentences: Number of sentences in the summary
    """
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation Error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."

# Example usage
if __name__ == "__main__":
    topic = "Python programming language"
    print(get_wikipedia_summary(topic))
