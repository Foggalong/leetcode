class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Given a list of words, list letters, and score of every character. Return
        the maximum score of any valid set of words formed by using the given
        letters. Each word in words and letter in letters can only be used once.
        """

        # dict of each word's score (ord gives ASCII key, 'a' is 97, 'b' 98, etc)
        word_score = {word: sum(score[ord(l)-97] for l in word) for word in words}

        best_score: int = 0

        for word in words:
            # copy prevents changing original between words
            letters_left: List[str] = letters.copy()

            try:
                for l in word: letters_left.remove(l)
            except ValueError:
                # word that's impossible, move to next
                continue

            # each words[i] can only be used once, so remove from list available
            words_left = words.copy()
            words_left.remove(word)

            # add maximum possible score from remaining letters
            total = word_score[word] + self.maxScoreWords(words_left, letters_left, score) 

            best_score = max(total, best_score)

        return best_score
