class Article:
    all = [] 

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._title = title 
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title 
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []
        self._magazines = set()

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(self._magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        self._magazines.add(magazine)
        return article

    def topic_areas(self):
        return list(set(mag.category for mag in self._magazines)) if self._magazines else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")

        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1

        return [author for author, count in author_count.items() if count > 2] if author_count else None
