from typing import List

class CountVectorizer:
    def __init__(self):
        self._feature_names = []
        self._vocabulary = {}

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        feature_count = 0
        for document in corpus:
            words = document.lower().split()
            for word in words:
                if word not in self._vocabulary:
                    self._vocabulary[word] = feature_count
                    self._feature_names.append(word)
                    feature_count += 1

        matrix = []
        vocab_size = len(self._feature_names)

        for document in corpus:
            vector = [0] * vocab_size
            words = document.lower().split()
            for word in words:
                if word in self._vocabulary:
                    word_index = self._vocabulary[word]
                    vector[word_index] += 1
            matrix.append(vector)

        return matrix

    def get_feature_names(self) -> List[str]:
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