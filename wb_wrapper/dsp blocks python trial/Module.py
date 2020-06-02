# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:22:24 2020

@author: medin
"""
import re
base_number  = 32
inp_number = 96
rem = inp_number/base_number
str1 = "data"


# IMPORTING FILE NAME 
file_name = input("Enter Dsp_block name: ")
#print(file_name)
with open( file_name, 'r') as t:
    t_contents = t.readlines()
# Instantiating partivular DSP IP block parameter.     
#for i in range(len(t_contents)):
#    if re.match('IIR_filter', t_contents[i]):
#        print("IIR_filter IIR_filter(\n               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
#    elif re.match('FIR_filter ', t_contents[i]):
#        print("FIR_filter FIR_filter(\n               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
#    elif re.match('dft_top ', t_contents[i]):
#        print("dft_top dft_top(\n            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),\n            .X0(dataIn[15:0]),\n            .X1(dataIn[31:16]),\n            .X2(dataIn[47:32]),\n            .X3(dataIn[63:48]),\n            .Y0(dataOut[15:0]),\n            .Y1(dataOut[31:16]),\n            .Y2(dataOut[47:32]),\n            .Y3(dataOut[63:48]));")
#    elif re.match('module idft_top ', t_contents[i]):
#        print("idft_top idft_top(\n            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),\n            .X0(dataIn[15:0]),\n            .X1(dataIn[31:16]),\n            .X2(dataIn[47:32]),\n            .X3(dataIn[63:48]),\n            .Y0(dataOut[15:0]),\n            .Y1(dataOut[31:16]),\n            .Y2(dataOut[47:32]),\n            .Y3(dataOut[63:48]));")
#t.close()


# Instantiating partivular DSP IP block parameter.     
#for i in range(len(t_contents)):
#    if re.match('IIR_filter', t_contents[i]):
#        print("IIR_filter IIR_filter(\n               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
#    elif re.match('FIR_filter ', t_contents[i]):
#        print("FIR_filter FIR_filter(\n               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));") 
#    
#    elif re.match('dft_top ', t_contents[i]):
#        print("dft_top dft_top(\n            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),\n            .X0(dataIn[15:0]),")
##        f=open("IO.txt", "w+")
#        if(int(rem)>=1):
#            for i in range(0,int(rem)):
#                str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
##                f.write(str2)
##                f.write("\n")
#                print('            .X',i,str2,',')  
##        f.close() 
##        f=open("IO.txt", "w+")
#        if(int(rem)>=1):
#            for i in range(0,int(rem)):
#                str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
##                f.write(str2)
##                f.write("\n")
#                print('            .Y',i,str2,',')  
#        print(')')   
#       
#    elif re.match('module idft_top ', t_contents[i]):
#        print("idft_top idft_top(\n            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),")
##        f=open("IO.txt", "w+")
#        if(int(rem)>=1):
#            for i in range(0,int(rem)):
#                str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
##                f.write(str2)
##                f.write("\n")
#                print('            .X',i,str2,',')  
##        f.close() 
##        f=open("IO.txt", "w+")
#        if(int(rem)>=1):
#            for i in range(0,int(rem)):
#                str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
##                f.write(str2)
##                f.write("\n")
#                print('            .Y',i,str2,',')  
#        print(')')   
#            
#t.close()

# Instantiating partivular DSP IP block parameter.     
for i in range(len(t_contents)):
    if re.match('IIR_filter', t_contents[i]):
        print("IIR_filter IIR_filter(\n")
    elif re.match('FIR_filter ', t_contents[i]):
        print("FIR_filter FIR_filter(\n")  
    elif re.match('dft_top ', t_contents[i]):
        print("dft_top dft_top(\n")     
    elif re.match('idft_top ', t_contents[i]):
        print("idft_top idft_top(\n")

#for i in range(len(t_contents)):
    if re.match('IIR_filter', t_contents[i]) or re.match('FIR_filter', t_contents[i]):
        print("               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
    elif re.match('dft_top ', t_contents[i]) or re.match('idft_top ', t_contents[i]):
        print("            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),")
        
        if(int(rem)>=1):
          for i in range(0,int(rem)):
             str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
             print('            .X',i,str2,',')
        if(int(rem)>=1):
          for i in range(0,int(rem)):
             str2 = f"(dataIn[{base_number*(i+1)-1}:{base_number*(i)}])"
             print('            .Y',i,str2,',')  
        print(');')   
            
t.close()