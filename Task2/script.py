class CountVectorizer:

    def __init__(self):
        self._feature_names = []
        self._vocabulary = {}

    def _tokenize(self, document: str) -> list[str]:
        words = document.lower().split()
        cleaned_words = []
        for word in words:
            cleaned_word = ''.join(char for char in word if char.isalpha())
            if cleaned_word:
                cleaned_words.append(cleaned_word)
        return cleaned_words

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        processed_corpus = [self._tokenize(doc) for doc in corpus]

        feature_count = 0
        for words in processed_corpus:
            for word in words:
                if word not in self._vocabulary:
                    self._vocabulary[word] = feature_count
                    self._feature_names.append(word)
                    feature_count += 1

        matrix = []
        vocab_size = len(self._feature_names)

        for words in processed_corpus:
            vector = [0] * vocab_size
            for word in words:
                word_index = self._vocabulary[word]
                vector[word_index] += 1
            matrix.append(vector)

        return matrix

    def get_feature_names(self) -> list[str]:
        return self._feature_names


# Код из PDFки
''' 
if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())

    print(count_matrix)
'''