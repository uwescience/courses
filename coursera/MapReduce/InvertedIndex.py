import MapReduce
import nltk

def data():
    books = {}
    book_titles = nltk.corpus.gutenberg.fileids()
    for title in book_titles:
        books[title] = nltk.corpus.gutenberg.words(title)
    return books

def mapper(mr, book, words):
    for word in words:
        mr.emit_intermediate(word, book)

def reducer(mr, word, books):
    mr.emit({word : list(set(books))})

def main():
    MapReduce.execute(data(), mapper, reducer)

if __name__ == '__main__':
    main()
