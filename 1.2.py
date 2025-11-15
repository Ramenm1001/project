cats = 0
def count_cat(text):
    global cats
    amount = text.count("cat")
    cats = cats + amount
