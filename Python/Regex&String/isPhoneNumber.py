def is_phone_number(text):
    if len(text) != 12: # Phone numbers have exactly 12 characters.
        return False
    for i in range(0, 12): # The first 12 characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True

print('Is 415555424212 a phone number?', is_phone_number('415551254242'))
print(is_phone_number('415512554242'))
print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
print(is_phone_number('Moshi moshi'))
   
# Finding using normal Method