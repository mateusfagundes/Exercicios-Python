nums = [1, 2, 3]
print (type(nums))

nums.append(3)
nums.append(3)
nums.append(3)
print(len(nums)) # LEN para ver o tamanho da lista

nums[3] = 100 # Para alterar o 4º elemento da lista
nums.insert(0, -200) # deslocou a lista e inseriu o numero -200

print(nums) #(nums) Chama toda a lista
print(nums[2]) #(nums[2]) Chama o item da lista selecionado entre []