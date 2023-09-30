import os




file_opt = {"pt": "sample_pt.txt",
            "en": "sample_en.txt"}



dict_all = {}

list_words = []




choose_file = input("Choose (pt) or (en), to load text:\n")




text_to_read = open(file_opt[choose_file], "r")




#print(text_to_read.read())



dataset = text_to_read.read()



list_words = dataset.split(" ")




print(list_words)


# reject everything that is 1 letter


print("STARTING TO ANALYSE \n")




for word in list_words:
    
    if len(word) <= 1:
        list_words.remove(word)
    
    # triagem, verifica as que são só duas letras e adiciona ao dict
    
    if len(word) == 2:
        dict_all[word] = 1
        
    
        
        
print(list_words)



# for line in dataset:
    
#     print("line\n")
#     print(line)

#     for i in range(0, len(line),2):
        
#         print("", line[i], line[i+1], "\n")
        
