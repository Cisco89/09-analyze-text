# count Alpha chars
# count char "e"
# percent of chars are "e" to two decimals

def count_alpha_char(string):
    alpha_count = 0
    for char in string:
        if char.isalpha():
            alpha_count += 1
    return alpha_count

def count_e_char(string):
    e_count = 0
    e = "e"
    cap_e = "E"
    for char in string:
        if char == e or char == cap_e:
            e_count +=1
    return e_count
    
def percent_of_char_is_e(e_count, alpha_count):
    percent = e_count / alpha_count
    percent = percent * 100
    percent = "{:.2f}".format(percent)
    return percent

def analyze_text(text):
    # Your code here
    alpha_count = count_alpha_char(text)

    e_count = count_e_char(text)

    percent = percent_of_char_is_e(e_count, alpha_count)
 
    return (f"The text contains {alpha_count} alphabetic characters, of which {e_count} ({percent}) are 'e'.")
