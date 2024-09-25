input_words = [
    "increasing?",
    "accountable?",
    "enduring?",
]

def stutter(input_words):
    output_words = []
    for word in input_words:
        sliced_word = word[:2]
        output_words = sliced_word + "..." + sliced_word + "..." + word
        print(output_words)

stutter(input_words)
    

            
            
        