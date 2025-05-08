

to_do_list=[]
while(True):
 user_choice= input("what do you want: add or remove or view or exit: ")
 if user_choice=='add':
  task=input('what add your to do list')
  to_do_list.append (task)
  print("task added")

 elif user_choice=='view':
      if not to_do_list:
         print("not fuond eny task")
      else:
       for task in to_do_list:
         print(task)
 elif user_choice=='remove': 
   if not to_do_list:
        print('not fuond eny task')
   else:   
    task_remove=input("input a task you ned removed:  ")  
    if not task_remove in to_do_list:
           print('not fuond this task')
    else:
      to_do_list.remove( task_remove)
      print("task removed")
 elif user_choice=='exit': 
   break
 else :
   print("i dont understand you")