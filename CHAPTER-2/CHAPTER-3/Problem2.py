#write a program to fill in a letter template given below with name and date

letter = '''Dear <|Name|>,
            You are selected 
            <|Date|>'''

print(letter.replace("<|Name|>","Abhinav").replace("<|Date|>", "25 september 2026"))        