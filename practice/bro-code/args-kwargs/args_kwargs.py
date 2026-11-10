# *args and **kwargs

# def students(*args):
#     for arg in args:
#         print(arg,end=" ")
# students("nikhil","jeevan")
# [PRIVACY: original personal names replaced with fake placeholders]
# students("student1","student2")

# def info(**kwargs):
#     for key,value in kwargs.items():
#      print(f"{key:<5} -> {value:<5}")
# info(Name="Nikhil",Class="5th",age=19,place="Blr")
# [PRIVACY: original personal info (name, age, place) replaced with fake placeholders]
# info(Name="Student",Class="5th",age=0,place="City")
#

#--------------------------------------------------------

# *args and **kwargs

# ------------------ argsss
# final = [0]

# def data(*args):  #or *args = *flush_data
#     count = 0
#     tt=0
#     for i in args:
#         tt += i
#         final.append(tt)
#         count += 1
#     print(final[count])

# data(1,2,3,4,5,6,7,8,9,0)
# ------------------ argsss
# import time

# def speak(*args):
#     for ch in args:
#         print(ch)
#         time.sleep(0.7)

# print(speak("wake","up","jarvis"))
# ------------------ argsss and kwargs
# import time

# def listen(*args,**kwargs):
#     for arg in args:
#         print(f"Listened :", arg)
#         time.sleep(0.8)
#     for x in kwargs.values():
#         print(x)
# listen("hi","this","is","nikhil",son="nikhil")
# [PRIVACY: original personal name replaced with fake placeholder]
# listen("hi","this","is","student",son="student")
