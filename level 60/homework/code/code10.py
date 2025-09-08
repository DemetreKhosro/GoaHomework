'''https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python'''
# Convert string to camel case

def to_camel_case(text):
    if not text:
        return ''
    
    for i in ['-', '_']:
        text = text.replace(i, ' ')
        
    words = text.split()
    
    return words[0] + ''.join(word.capitalize() for word in words[1:])