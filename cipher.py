def pattern_cipher(word):
      if word is None or word == "":
        return word                                       #returned immediately
      

      if not word.isalpha():
        return word
      
      
      lower_word = word.lower()

      if lower_word == lower_word[::-1]:
        return word
##Repeated letters (but NOT palindrome)
      if len(set(lower_word)) < len(lower_word):
        return word[::-1]                                #reverse the word

      return word[1:] + word[0]                          #rotate the word (for unique words)
        
        #If the number is palindrome and also repeated letters then priority wise palindrome executed first not repeated letters condition.


