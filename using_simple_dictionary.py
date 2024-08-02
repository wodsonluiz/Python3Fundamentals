acronyms = {'LOL': 'Laugh out Loud', 
            'IDK': "I don't know", 
            'TBH': 'To be honest'}

del acronyms['IDK']

print(acronyms)

definition = acronyms.get("BTW")

if definition:
    print(definition)
else:
    print("Cannot exits definition")
