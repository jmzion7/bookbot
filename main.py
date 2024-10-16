def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_final = count_words(text)
    lowered_text = text.lower()
    char = count_characters(lowered_text)
    chars_sorted_list = chars_dict_to_sorted_list(char)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_final} words found in the document")
    print()

    for item in chars_sorted_list:
       if not item["char"].isalpha():
          continue
       print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


# function to count words
def count_words(text):
  counter = 0
  words = text.split()
  for i in range(len(words)):
    counter += 1
  return counter


# function to sort
def sort_on(d):
    return d["num"]

# function to sort and append list
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# function to count characters
def count_characters(lowered_text):
   char_count = {}
   for k in lowered_text:
      char_count.setdefault(k, 0)
      char_count[k] = char_count[k] +1
   return char_count

# function to read file
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

