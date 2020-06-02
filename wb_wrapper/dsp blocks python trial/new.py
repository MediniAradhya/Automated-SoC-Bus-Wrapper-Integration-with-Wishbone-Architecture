base_number  = 32
inp_number = 96
rem = inp_number/base_number
str1 = "data"
f=open("shit.txt", "w+")
if(int(rem)>=1):
    for i in range(0,int(rem)):
            str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
            f.write(str2)
            f.write("\n")
            print('X',i,str2)  
f.close()




#with open('iir_top.v', 'r') as f:
#    f_contents = f.readlines()
#for i in range(len(f_contents)):
#    if re.match('module iir', f_contents[i]):
#        start_index = i
#    if re.match('endmodule', f_contents[i]):
#        end_index = i
#write_list = f_contents[start_index: end_index+1]


#base_number  = 32
#inp_number = 96
#rem = inp_number/base_number
#str1 = "data"
#f=open("shit.txt", "w+")
#if(int(rem)>=1):
#    for i in range(int(rem)):
#        
#        str2 = f"data[{base_number*(i+1)-1}:{base_number*(i)}]"
#        f.write(str2)
#        f.write("\n")
#        print("str", str2)
#f.close()
