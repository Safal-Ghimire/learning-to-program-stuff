list_x=[]
span = 24
final_list=[]
new_list=[]
for i in range (0,span):
  list_x.append(" ")

for i in range (0,span):

    final_list.append(list_x)

center = span/2

radius=4
new_list=list_x
final_new_list=[]
for i in range (0,span):

  
  for j in range(0,span):
      
      if (i**2 + j**2) == radius**2:
        new_list[j] = "*"

        

      
  final_new_list.append(new_list)
  new_list=list_x


for i in range (0,span):
  
    
      print(final_new_list[i])