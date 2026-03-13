# Oscar Best Picture Dialogue Analysis
An analysis of dialogue across genders in the Best Picture nominees from the 98th and 97th Academy Awards.
## Methodology

In performing this dialogue analysis, I watched and transcribed every Best Picture nomination from the 98th Academy Awards (this year) and the 97th Academy Awards (last year). Each film took 2.5-6 hours to transcribe.

I pulled film transcripts from the independent film magazine Scraps from the Loft and OpenSubtitles. On the Scraps from the Loft website, each transcript is messy, with stage directions and the occasional music note symbol included throughout. I needed to efficiently remove these from the text and put them in a spreadsheet, so I could then manually spotcheck and correct each transcript.

 I downloaded each transcript as a .txt file. With assistance from Claude AI, I created a Python script called transcript\_cleaner.py that enabled me to efficiently remove these stage directions and symbols and place the remaining text into organized .CSV files. Then, I watched each film and spotchecked the transcripts as Google Spreadsheets, making corrections where needed. I also manually added the speakers, their gender and the correct number of words for each line using formulas and manual inputs.

I have included .CSV files containing each transcript within this repository. However, to avoid copyright infringement, I have removed the columns identifying the speakers, which prevents each transcript from becoming reproduceable. The gender and speaker_role columns remain, among other fields.

I performed my data analysis in Python and Google Spreadsheets. You can find my analysis in the Python notebook called dialogue\_analysis.ipynb.

## Decision-Making Memo

In making each film’s transcript, I had to make several decisions as to how to record dialogue. There is an element of subjectivity to these transcripts that makes the datasets inevitably imperfect. I have detailed these decisions below.

* **Gender classification.** I record a character’s gender based on the gender they identify as in the film. I will provide additional context for specific characters.

  * Emilia Perez, a trans woman who transitions at the beginning of ‘Emilia Perez,’ is recorded as “FEMALE” throughout the entire transcript, including before her transition.

  * Cardinal Benitez from “Conclave” is (spoiler) revealed to be intersex at the end of the film, something that he himself had not learned until adulthood. It is not explicitly clear if Benitez identifies as nonbinary following his discovery of being intersex. Therefore, I classify Benitez as “MALE” because he grew up identifying as a man, and I interpreted the ending to mean that he continues to live as a man.

  * Bobo, a minor character from “One Battle After Another,” explicitly identifies as nonbinary and is recorded as “NONBINARY.”

* **Group speakers.** If groups of people of multiple genders are speaking, the gender is recorded as “MIXED” and the speaker is typically recorded as “GROUP.” This frequently happens in musicals with an ensemble cast, but can also happen with chanting or shouting crowds.

* **Multiple named speakers.** If more than one named character speaks the same lines at the same time, the words are recorded for each character individually. This typically happens in musical numbers, such as when Remmick, Bert and Joan sing “Picked Poor Robin Clean” in ‘Sinners.’

* **Diegetic sound vs. nondiegetic sound.** I include all words spoken within the world of the film (diegetic sound) in the transcript. This includes when characters sing or speak on the phone, or when a reporter speaks through a radio or television. If nondiegetic sound (sound that plays over the film but does not exist as part of the film’s world) with lyrics plays, I do not include the words in the transcript, with the exception of narrators (as in “Train Dreams”).

* **Numbers.** When a character says a number, I count this as one word. Therefore, numbers may appear fully written out and hyphenated (“twenty-one,” not “twenty one”) or as a numeral (21).

* **Exceptions to numbers.** If a character says a number preceded by “a,” as in “a hundred” or “a thousand,” I transcribe it as such. I do not transcribe “a hundred” as “100.” The word “million” is always written out and never written numerically, but the amount of millions is always written numerically (“100 million,” not “one hundred million”).

* **Time.** I transcribe time according to their numerical values (“8:30 am,” not “eighty thirty a m”).

* **Money.** Money is written as numerals (as in ‘Marty Supreme’: “I’M ASKING FOR WAY MORE THAN 2.50,” not “two fifty”). If a character refers to a certain amount of money in dollars, I transcribe it as the number followed by the word “dollar(s)” (not “$2.50”).

* **Foreign language films.** Films that are not primarily in English — which in this dataset are “Sentimental Value,” “The Secret Agent,” “I’m Still Here” and “Emilia Perez” — are transcribed according to their English subtitles from their corresponding streaming service.

* **Foreign languages within English-language films.** When characters speak other languages in a primarily English speaking film, I transcribe them in one of three ways. If there are English subtitles over the foreign language, I transcribe the English subtitles. If there are no English subtitles and viewers cannot understand what is being said (unless, of course, they speak the language), I will either estimate the number of words in brackets (“\[CHARACTER SPEAKING SPANISH WORDS\]”) or, if possible, attempt to listen and transcribe the language itself. More often than not, the words are bracketed.

* **Sign language.** I count sign language in the transcript according to its English subtitles.

* **Stumbles, stutters and “um”s.** I include any stumbles, stutters, accidental repetitions and filler words as words in the transcript.

* **Speaker discrepancies for minor characters.** For characters who make little appearance, have no name and/or who have extremely minor roles in the film, I often do not include a name for them and opt for something more generic, such as “WOMAN” or “MAN”. This means that I cannot perform any data analysis relating to the number of speakers in each film, because multiple insignificant characters might be recorded as the same one. The same can be said of unnamed occupational roles, of which there might be multiple characters – ie, “COP” or “COMMENTATOR.”
