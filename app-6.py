import wikipedia
from googlesearch import search
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_wikipedia_summary(topic, sentences=2):
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation Error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."


def google_search_results(query, num_results=5):
    try:
        results = list(search(query, num_results=num_results))
        return results
    except Exception as e:
        return f"Error: {e}"


def get_wikipedia_categories(topic):
    try:
        page = wikipedia.page(topic)
        return page.categories
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"Error: {e}"


def get_related_topics(topic, max_links=10):
    try:
        page = wikipedia.page(topic)
        return page.links[:max_links]
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"Error: {e}"


def create_wordcloud(topic):
    try:
        page_content = wikipedia.page(topic).content
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(page_content)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n--- Python Super App ---")
        print("1. Get Wikipedia Summary")
        print("2. Perform Google Search")
        print("3. Get Wikipedia Categories")
        print("4. Find Related Topics on Wikipedia")
        print("5. Generate Word Cloud from Wikipedia Page")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            topic = input("Enter a topic: ")
            sentences = int(input("Number of sentences (default 2): ") or 2)
            print("\n" + get_wikipedia_summary(topic, sentences))
        
        elif choice == "2":
            query = input("Enter search query: ")
            num_results = int(input("Number of results (default 5): ") or 5)
            results = google_search_results(query, num_results)
            print("\nGoogle Search Results:")
            for i, link in enumerate(results, 1):
                print(f"{i}. {link}")
        
        elif choice == "3":
            topic = input("Enter a topic: ")
            categories = get_wikipedia_categories(topic)
            print("\nWikipedia Categories:")
            if isinstance(categories, list):
                for category in categories:
                    print(f"- {category}")
            else:
                print(categories)
        
        elif choice == "4":
            topic = input("Enter a topic: ")
            max_links = int(input("Number of related topics (default 10): ") or 10)
            related_topics = get_related_topics(topic, max_links)
            print("\nRelated Topics:")
            if isinstance(related_topics, list):
                for related in related_topics:
                    print(f"- {related}")
            else:
                print(related_topics)
        
        elif choice == "5":
            topic = input("Enter a topic: ")
            print("Generating Word Cloud...")
            create_wordcloud(topic)
        
        elif choice == "6":
            print("Exiting the app. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
