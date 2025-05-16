def sort_by_length(lst):
    return sorted(lst, key=len)


print(sort_by_length(["Google", "Apple", "OpenAI", "Mocrosoft"]))
print("----    ----    ----    ----")
print(sort_by_length(["Leo", "Donny", "Miki", "Raph"]))
print("----    ----    ----    ----")
print(sort_by_length(["Leonardo", "Donatello", "Raphael", "Michelangelo"]))
print("----    ----    ----    ----")
print(sort_by_length(["Turing", "Einstein", "Jung", "King"]))
