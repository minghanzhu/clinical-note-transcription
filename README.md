## Rationale

Doctors often verbally dictate their clinical note after seeing a patient. These dictations are transcribed
word-for-word and then formatted to generate the final note. As part of their dictation, doctor's need a simple way to
insert numbered lists. To accomplish this, we have provided the doctor with some phrases that they can say in order to
indicate the start of a numbered list and every next item.

### Implementation

To accomplish this, we have provided the doctor with phrases "Number n" and "Number next" that
they can say in order to indicate the start of a numbered list and every next item.

To start a numbered list, the doctor would say "Number n", where n is a number from one to nine, then say what they
would want as the nth item in the numbered list. To indicate the start of the next item in the numbered list, the doctor
would say "Number next", then say what they would want as the next item in the numbered list.

For example, the "Number next" item after saying the "Number one" item would be the second item in the numbered list.
The doctor would then repeat the "Number next" steps until they reach the end of their numbered list.

The functionality is implemented by `Transcription.__transcript_formatted()` method in the `Transcription` class.

### Testing

To run the tests, run the following command:

```python -m unittest unit_test_transcription.py```
