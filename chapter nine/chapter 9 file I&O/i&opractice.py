# # # with open("iopractice.txt",)as f:
# # #     data=f.read()
# # #     print(data)
# # st="this is python programming"
# # with open("iopractice.txt","w")as f:
# #     f.write(st)
# with open("iopractice.txt")as f:
#     lines=f.readlines()
#     print((lines,type(lines)))
with open("iopractice.txt")as f:
    lines1=f.readline()
    print((lines1,type(lines1)))
    lines2=f.readline()
    print((lines2,type(lines2)))
    lines3=f.readline()
    print((lines3,type(lines3)))
    lines4=f.readline()
    print((lines4,type(lines4)))
