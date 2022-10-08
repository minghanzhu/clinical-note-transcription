"""
Methods reformatting doctor clinical notes transcript.
"""
import re

# A dictionary of words to their corresponding numbers from one to nine.
WORD_TO_NUM_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class Transcription:
    """A class that represents a doctor clinical note transcript."""

    _transcript: str = ""

    def __init__(self, transcript: str):
        self._transcript = transcript

    @classmethod
    def _transcript_formatted(cls, transcript: str) -> str:
        """
        Return a formatted transcript string with a numbered list of note items.
        :param transcript: The transcript to format.
        :return: The transcript formatted.
        """

        # If the transcript is empty or has no numbered sentences, return the original transcript.
        if transcript == "" and "Number " not in transcript:
            return transcript

        # Split the transcript into a list of words by spaces.
        transcript_words = transcript.split(" ")

        number_n = 0

        # Iterate over the transcript words, look for sentences starting with "Number <n>" and  "Number next" phrases.
        for index, word in enumerate(transcript_words):

            # # If the sentence starts with "Number next" and we have seen a "Number <n>" phrase
            if number_n > 0 and (word == "Number" or word == "number"):
                number_next_str = str(transcript_words[index + 1])
                if number_next_str == "next":
                    number_n += 1
                    transcript_words[index] = ""
                    transcript_words[index + 1] = "".join(["\n", str(number_n), "."])
                    next_word = transcript_words[index + 2]
                    # Capitalize the first letter of the next word.
                    transcript_words[index + 2] = next_word[0].capitalize() + next_word[1:]

            # Look for sentences starting with "Number <n>" if not found yet
            elif number_n == 0 and word == "Number":
                number_n_str = str(transcript_words[index + 1])
                # If the word is a number from one to nine
                if number_n_str in WORD_TO_NUM_MAP:
                    number_n = WORD_TO_NUM_MAP[number_n_str]
                    transcript_words[index] = ""
                    transcript_words[index + 1] = f"\n{number_n}."
                    next_word = transcript_words[index + 2]
                    # Capitalize the first letter of the next word
                    transcript_words[index + 2] = next_word[0].capitalize() + next_word[1:]

        # Remove empty strings from the list of words.
        transcript_words = list(filter(lambda w: w != "", transcript_words))

        # Join the transcript words into a string.
        formatted_transcript = " ".join(transcript_words)
        formatted_transcript = re.sub(r'\s+$', '', formatted_transcript, flags=re.M)

        return formatted_transcript.strip()
