# Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])
print(color_list[0:4:2])

# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
date = str(exam_st_date[0]) + "/" + str(exam_st_date[1]) + "/" + str(exam_st_date[2])
print(" Exam date is: ", date)
