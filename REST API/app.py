import streamlit as st

def combine_single_elements(lst):
    i = 0
    while i<len(lst):
        if (lst[i].isalpha() and len(lst[i]) == 1):
            start = i
            end = i
            while (i<len(lst) and len(lst[i]) == 1):
                end = i
                i+=1
            lst[start:end+1] = [''.join(lst[start:end+1])]
            i = start+1
        else:
            i+=1      
    return lst

def currency(lst):
    i = 0
    while i<len(lst):
        if (lst[i].lower() == 'dollar' or lst[i].lower() == 'dollars') and i>0:
            lst[i] = '$'
            if lst[i-1].isdigit():
                lst[i-1 : i+1] = [''.join(lst[i-1 : i+1])] 
        else:
            i+=1
    return lst

def n_tuple(lst):
    n_tpl = {'single':1,'double':2,'triple':3,'quadruple':4}
    i=0
    while i<len(lst):
        if lst[i].lower() in n_tpl and len(lst)>=i+1 and len(lst[i+1]) == 1:
            lst[i:i+2] = [n_tpl[lst[i]] * lst[i+1]]
        else:
            i+=1
    return(lst)


def spoken_to_written(text):
    units = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
        "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
      }
    #splitting each words of the text seperated with space and storing them in a list
    lst = text.split()
    for i in range(len(lst)):
        if lst[i] in units:
            lst[i] = str(units[lst[i]])
    n_lst = combine_single_elements(lst)
    n_lst = currency(n_lst)
    n_lst = n_tuple(n_lst)
    
    return ' '.join(n_lst)

def main():
    st.title('Speech to written english')
    text = st.text_input('Enter text')
    result = ''
    if st.button('Submit'):
        result = spoken_to_written(text)
    st.success(f"{result}")

if __name__ ==  '__main__':
    main()