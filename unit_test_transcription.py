from transcription import Transcription
import unittest


class TestTranscription(unittest.TestCase):

    def test_transcript_formatted_with__empty_transcript(self):
        """The transcript is empty.
        Expected result is that the empty transcript is logged and returned as is."""
        transcript = ""
        expected = ""
        self.assertEqual(expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__no_numbered_sentences(self):
        """The transcript has no "Numbered <n>." sentences.
        Expected result is that the transcript is returned as is."""
        transcript = "This is an regular sentence."
        expected = "This is an regular sentence."
        self.assertEqual(expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__with_multiple_numbered_sentences(self):
        """The transcript has a regular sentence and a list of numbered sentences starting from one.
        The expected result is that the numbered sentences are numbered correctly."""
        # Consider the possibility that a regular sentence may start with "Number <not-n>" (e.g. "Number of patients").
        transcript = "Patient presents today with several issues. " \
                     "Number one BMI has increased by 10% since their last visit " \
                     "number next patient reports experiencing dizziness several times in the last two weeks. " \
                     "Number next patient has a persistent cough that hasn't improved for last 4 weeks " \
                     "Number next patient is taking drug number five several times a week"

        expected = "Patient presents today with several issues.\n" \
                   "1. BMI has increased by 10% since their last visit\n" \
                   "2. Patient reports experiencing dizziness several times in the last two weeks.\n" \
                   "3. Patient has a persistent cough that hasn't improved for last 4 weeks\n" \
                   "4. Patient is taking drug number five several times a week"
        self.assertEqual(
            expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__with_single_numbered_sentence(self):
        """The transcript has a regular sentence and a single numbered sentence.
        The expected result is that the numbered sentence is numbered correctly."""
        transcript = "This is an regular sentence. " \
                     "Number one This is the first numbered sentence."
        expected = "This is an regular sentence.\n" \
                   "1. This is the first numbered sentence."
        self.assertEqual(expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__with_non_one_number_n_sentence(self):
        """The transcript has a list of numbered sentences starting from a starting number other than one.
        The expected result is that the numbered sentences are numbered correctly."""
        transcript = "This is an regular sentence. " \
                     "Number nine this is the first numbered sentence. " \
                     "Number next this is the second numbered sentence. " \
                     "Number next is the third numbered sentence."
        expected = "This is an regular sentence.\n" \
                   "9. This is the first numbered sentence.\n" \
                   "10. This is the second numbered sentence.\n" \
                   "11. Is the third numbered sentence."
        self.assertEqual(
            expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__only_numbered_sentences(self):
        """The transcript only has numbered sentences but no regular sentence.
        The expected result is that the numbered sentences are numbered correctly."""
        transcript = "Number one This is the first numbered sentence. " \
                     "Number next this is the second numbered sentence. " \
                     "Number next is the third numbered sentence."
        expected = "1. This is the first numbered sentence.\n" \
                   "2. This is the second numbered sentence.\n" \
                   "3. Is the third numbered sentence."
        self.assertEqual(
            expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__with_non_period_punctuations(self):
        """The transcript has non-period punctuations.
        The expected result is that the punctuation are preserved as is."""
        transcript = "Number one This is the first numbered sentence! " \
                     "Number next this is the second numbered sentence? " \
                     "Number next is the third numbered sentence."
        expected = "1. This is the first numbered sentence!\n" \
                   "2. This is the second numbered sentence?\n" \
                   "3. Is the third numbered sentence."
        self.assertEqual(
            expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__with_empty_number_n_sentence(self):
        """The transcript has an empty "Numbered <n>." sentence.
        The expected result is that the empty "Numbered <n>." sentence is ignored and treated as a regular sentence."""
        transcript = "Number five. Scratch that. " \
                     "Number one this is the first sentence. " \
                     "Number next is the second sentence. " \
                     "Number next is the third sentence."

        expected = "Number five. Scratch that.\n" \
                   "1. This is the first sentence.\n" \
                   "2. Is the second sentence.\n" \
                   "3. Is the third sentence."
        self.assertEqual(
            expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted__with_only_number_next_sentence(self):
        """The transcript has "Numbered next" keyword but no "Numbered <n>" keyword The expected result is that
        "Numbered next" sentences without a preceding "Numbered <n>" sentence are treated as regular sentences."""
        transcript = "Number next is not the first sentence. Number next is not the second sentence. " \
                     "Number one is the first sentence."
        expected = "Number next is not the first sentence. Number next is not the second sentence.\n" \
                   "1. Is the first sentence."
        self.assertEqual(
            expected, Transcription._transcript_formatted(transcript))

    def test_transcript_formatted_with__with_empty_number_next_sentence(self):
        """The transcript has an empty "Numbered next" sentence.
        Expected result is that the empty numbered sentence is ignored and treated as a regular sentence."""
        transcript = "Number one This is the first numbered sentence. Inside the first numbered sentence, there is " \
                     "another regular sentence. " \
                     "Number next. " \
                     "Number next is the second numbered sentence."
        expected = "1. This is the first numbered sentence. Inside the first numbered sentence, there is " \
                   "another regular sentence. Number next.\n" \
                   "2. Is the second numbered sentence."
        self.assertEqual(expected, Transcription._transcript_formatted(transcript))


if __name__ == '__main__':
    unittest.main()
