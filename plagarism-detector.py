import string
import csv
import os

#pre processing 
def preprocess_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
    # Removing punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text.split()
    
    
words = preprocess_text('essay-1.txt')


words2 = preprocess_text('essay-2.txt')
#print(words[:10])
#print(words2[:10])

#frequency count
def word_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
freq1 = word_frequency(words)
freq2 = word_frequency(words2)


#print(list(freq1.items())[:10])
#print(list(freq2.items())[:10])


#looking for common words
def common_words(freq1, freq2):
    common = {}
    for word in freq1:
        if word in freq2:
            common[word] = (freq1[word], freq2[word])
    return common
    

#common = common_words(freq1, freq2)
#for word, counts in common.items():
#    print(f"{word}: Essay1 = {counts[0]}, Essay2 = {counts[1]}")

# Function to display common words
def search_word(freq1, freq2):
    word = input("Enter a word to search: ").lower()
    count1 = freq1.get(word, 0)
    count2 = freq2.get(word, 0)

    if count1 == 0 and count2 == 0:
        print(f"'{word}' not found in either essay.")
        return False
    else:
        print(f"'{word}' found:")
        print(f"  1: {count1} times")
        print(f"  2: {count2} times")
        return True
#search_word(freq1, freq2)

def plagiarism_score(common, total_words1, total_words2):
    common_total = sum(min(freq1, freq2) for freq1, freq2 in common.values())
    average_total = (total_words1 + total_words2) / 2
    score = (common_total / average_total) * 100
    return round(score, 2)

# Calculate total words
total_words1 = sum(freq1.values())
total_words2 = sum(freq2.values())

# Getting common words
common = common_words(freq1, freq2)

# Getting the score
score = plagiarism_score(common, total_words1, total_words2)

# Result
print(f"\nPlagiarism Score: {score}%")

# Plagiarism level indicator
if score > 80:
    print("⚠️ High similarity detected.")
elif score > 50:
    print("⚠️ Moderate similarity.")
else:
    print("✅ Low similarity.")

#exporting results to CSV
def export_csv(common):
    output_file = 'plagiarism_results.csv'
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Word', 'Essay1 Count', 'Essay2 Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for word, counts in common.items():
            writer.writerow({
                'Word': word, 
                'Essay1 Count': counts[0], 
                'Essay2 Count': counts[1]})
common = common_words(freq1, freq2)
export_csv(common)