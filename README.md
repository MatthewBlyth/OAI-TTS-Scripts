If you're converting plaintext to audio you can probably use an LLM in place of the latex to python scripts. The important points to maintain are:

1. Keep each text chunk under 4000 characters (OAI TTS model input limit)
2. Ensure each chunk ends at a paragrpah boundary (in case the stitching together of .wav files isn't seamless)
3. Insert newlines ("\n") at the end of and between all paragraphs. (Otherwise the model might not pause between paragraphs)
4. Replace any single-word acronym in parentheses with 'or <ACRONYM>'. (Otherwise the model says the acronym too fast imo)
