class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Given a list of strings consisting of many roots and a sentence
        consisting of words separated by spaces, replace all the derivatives
        in the sentence with the root forming it. If a derivative can be
        replaced by more than one root, replace it with the root that has
        the shortest length.
        """

        # sort roots by length
        dictionary.sort(key=lambda root: len(root))

        # pad sentence with spaces so first and lest can be detected as words
        sentence = f" {sentence} "

        for word in sentence.split(" ")[1:-1]:
            for root in dictionary:
                if word.startswith(root):
                    # hacky way to replace this specific word with root
                    sentence = sentence.replace(f" {word} ", f" {root} ")
                    # root was the shortest in dict, which fits,
                    # so don't need to consider any others
                    break

        return sentence[1:len(sentence)-1]
