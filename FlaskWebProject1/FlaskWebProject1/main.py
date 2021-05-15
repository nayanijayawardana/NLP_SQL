import nltk
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
import string
import where

text1 = input("Enter the Query : ")
text2 = input("Need to group ?")
lower_case = text1.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_word = cleaned_text.split()

# pass arguments for the where condition
whereClause = where.main(text1)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_word = []
for word in tokenized_word:
    if word not in stop_words:
        final_word.append(word)

print(tokenized_word)
print(final_word)

filtered_tokens_Array = []
for item in final_word:
    words = wordnet_lemmatizer.lemmatize(item)

    filtered_tokens_Array.append(words)

print(filtered_tokens_Array)

# POS tagging
pos = nltk.pos_tag(filtered_tokens_Array)
print(pos)

# Parser
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(pos)
print(result)
result.draw()

selective_pos = ['NN']
selective_pos_words = []
for word, tag in pos:
    if tag in selective_pos:
        selective_pos_words.append((word))
print(selective_pos_words)

table = []

aggregation_words = []

with open('tables.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in selective_pos_words:
            table.append(emotion)

# print(table)

if not table:
    print("Cannot find table name")

if table:

    if ' employee' in table:
        attrEmp = []
        with open('attributesEmp.txt', 'r') as file_Emp1:
            for line in file_Emp1:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')

                if word in selective_pos_words:
                    attrEmp.append(emotion)

        if not attrEmp:
            print("cannot find attribute names")

        if attrEmp:
            with open('aggregation.txt', 'r') as file_E2:
                for line in file_E2:
                    clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                    word, emotion = clear_line.split(':')

                    if word in selective_pos_words:
                        aggregation_words.append(emotion)

                    if aggregation_words:
                        for word in aggregation_words:
                            if ' COUNT' in aggregation_words:
                                print("SELECT" + ' '.join(str(x) for x in aggregation_words) + "(employee_id )")
                                print("FROM" + ' '.join(str(x) for x in table))
                                print(whereClause)

                                for x in range(5):
                                    print(x, end=",")
                            else:
                                print("SELECT" + ' '.join(str(x) for x in aggregation_words) + "(" + ''.join(
                                    str(x) for x in attrEmp) + " )")
                                print("FROM" + ' '.join(str(x) for x in table))

            if not aggregation_words:
                print("select" + ' '.join(str(x) for x in attrEmp))
                print("from" + ' '.join(str(x) for x in table))
                print(whereClause)

elif ' department' in table:
    attrDept = []
    with open('attributesDept.txt', 'r') as file_Dept1:
        for line in file_Dept1:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                attrDept.append(emotion)

    with open('aggregation.txt', 'r') as file_Dept2:
        for line in file_Dept2:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                aggregation_words.append(emotion)

                print(aggregation_words)

        if aggregation_words:
            print("select" + ' '.join(str(x) for x in aggregation_words) + " (" + ' '.join(
                str(x) for x in attrDept) + " )")
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

        if not aggregation_words:
            print("select" + ' '.join(str(x) for x in attrDept))
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

elif ' dependent' in table:
    attrDepend = []
    with open('attributesDepend.txt', 'r') as file_Depend1:
        for line in file_Depend1:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                attrDepend.append(emotion)

    with open('aggregation.txt', 'r') as file_Depend2:
        for line in file_Depend2:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                aggregation_words.append(emotion)

                print(aggregation_words)

        if aggregation_words:
            print("select" + ' '.join(str(x) for x in aggregation_words) + " (" + ' '.join(
                str(x) for x in attrDepend) + " )")
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

        if not aggregation_words:
            print("select" + ' '.join(str(x) for x in attrDepend))
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

elif ' job' in table:
    attrJob = []
    with open('attributesDept.txt', 'r') as file_Job1:
        for line in file_Job1:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                attrJob.append(emotion)

    with open('aggregation.txt', 'r') as file_Job2:
        for line in file_Job2:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                aggregation_words.append(emotion)

                print(aggregation_words)

        if aggregation_words:
            print("select" + ' '.join(str(x) for x in aggregation_words) + " (" + ' '.join(
                str(x) for x in attrJob) + " )")
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

        if not aggregation_words:
            print("select" + ' '.join(str(x) for x in attrJob))
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

elif ' region' in table:
    attrRegion = []
    with open('attributesDept.txt', 'r') as file_Region1:
        for line in file_Region1:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                attrRegion.append(emotion)

    with open('aggregation.txt', 'r') as file_Region2:
        for line in file_Region2:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                aggregation_words.append(emotion)

                print(aggregation_words)

        if aggregation_words:
            print("select" + ' '.join(str(x) for x in aggregation_words) + " (" + ' '.join(
                str(x) for x in attrRegion) + " )")
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

        if not aggregation_words:
            print("select" + ' '.join(str(x) for x in attrRegion))
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

elif ' country' in table:
    attrCountry = []
    with open('attributesDept.txt', 'r') as file_Country1:
        for line in file_Country1:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                attrCountry.append(emotion)

    with open('aggregation.txt', 'r') as file_Country2:
        for line in file_Country2:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                aggregation_words.append(emotion)

        if aggregation_words:
            print("select" + ' '.join(str(x) for x in aggregation_words) + " (" + ' '.join(
                str(x) for x in attrCountry) + " )")
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

        if not aggregation_words:
            print("select" + ' '.join(str(x) for x in attrCountry))
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

elif ' location' in table:
    attrLocation = []
    with open('attributesLocation.txt', 'r') as file_Location1:
        for line in file_Location1:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                attrLocation.append(emotion)

    with open('aggregation.txt', 'r') as file_Location2:
        for line in file_Location2:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in selective_pos_words:
                aggregation_words.append(emotion)

        if aggregation_words:
            print("select" + ' '.join(str(x) for x in aggregation_words) + " (" + ' '.join(
                str(x) for x in attrLocation) + " )")
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)

        if not aggregation_words:
            print("select" + ' '.join(str(x) for x in attrLocation))
            print("from" + ' '.join(str(x) for x in table))

            print(whereClause)
