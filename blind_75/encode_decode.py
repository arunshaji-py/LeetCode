
class Solution:
    def encode(strs: str) -> str:
        result = ""
        #when we loop over a list of strings, s hold one string in it. eg Hello World, s hold 'Hello'
        for s in strs:
            #result will be 5#Hello
            result += str(len(s))+ "#" + s
        return result
    
    def decode(encoded):
        result = []
        i = 0

        while i < len(encoded):
            j = i
            while encoded[j] != "#": #walk forward until we hit #
                j += 1
            
            length = int (encoded[i:j]) #extract the number before #
            #use python string slicing to extract the word
            word = encoded[j+1 : j+1+length] #this extracts the word from the # to the end of that word
            result.append(word)
            i = j+1 + word #move the pointer to the next word.
        return result
    
    







"""Notes
Encoding and Encryption are completely two concepts. Encoding is the process of how that string or data is prepared for transferring over the 
network. Encoding doesn't need any secret keys. Its basically telling the decoder where a string starts and where it ends and where the next 
words starts and stops.
Encryption is where the data is being changed into a completely new form for privacy it needs a key to decrypt.
"""