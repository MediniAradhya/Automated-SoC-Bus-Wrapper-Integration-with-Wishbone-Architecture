import re
#with open('iir_top.v', 'r') as t:
#    t_contents = t.readlines()
#
#for i in range(len(t_contents)):
#    if re.match('IIR_filter', t_contents[i]) or re.match('FIR_filter ', t_contents[i]):
#        print("(               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
#
#    elif re.match('dft_top ', t_contents[i]) or re.match('module idft_top ', t_contents[i]):
#        print("(            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),\n            .X0(dataIn[15:0]),\n            .X1(dataIn[31:16]),\n            .X2(dataIn[47:32]),\n            .X3(dataIn[63:48]),\n            .Y0(dataOut[15:0]),\n            .Y1(dataOut[31:16]),\n            .Y2(dataOut[47:32]),\n            .Y3(dataOut[63:48]));")
#
#t.close()


# IMPORTING FILE NAME 
file_name = input("Enter Dsp_block name: ")
#print(file_name)
with open( file_name, 'r') as t:
    t_contents = t.readlines()

# PRINTING TOP MODULE CODE -PART 1
#with open('file_name', 'r') as f:
#   f_contents = f.readlines()
for i in range(len(t_contents)):
    if re.match('module ', t_contents[i]):
        start_index = i
    if re.match('    end // always', t_contents[i]):
        end_index = i
write_list = t_contents[start_index: end_index+1]
print(write_list)
t.close()

# Instantiating partivular DSP IP block parameter.     
for i in range(len(t_contents)):
    if re.match('IIR_filter', t_contents[i]):
        print("IIR_filter IIR_filter(\n               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
    elif re.match('FIR_filter ', t_contents[i]):
        print("FIR_filter FIR_filter(\n               .clk(wb_clk_i),\n               .reset(~wb_rst_i),\n               .inData(dataIn),\n               .outData(dataOut));")
    elif re.match('dft_top ', t_contents[i]):
        print("dft_top dft_top(\n            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),\n            .X0(dataIn[15:0]),\n            .X1(dataIn[31:16]),\n            .X2(dataIn[47:32]),\n            .X3(dataIn[63:48]),\n            .Y0(dataOut[15:0]),\n            .Y1(dataOut[31:16]),\n            .Y2(dataOut[47:32]),\n            .Y3(dataOut[63:48]));")
    elif re.match('module idft_top ', t_contents[i]):
        print("idft_top idft_top(\n            .clk(wb_clk_i),\n            .reset(wb_rst_i),\n            .next(next_posedge),\n            .next_out(next_out),\n            .X0(dataIn[15:0]),\n            .X1(dataIn[31:16]),\n            .X2(dataIn[47:32]),\n            .X3(dataIn[63:48]),\n            .Y0(dataOut[15:0]),\n            .Y1(dataOut[31:16]),\n            .Y2(dataOut[47:32]),\n            .Y3(dataOut[63:48]));")
#t.close()

# PRINTING TOP MODULE CODE -PART 2
#with open('file_name', 'r') as f:
#   f_contents = f.readlines()
for i in range(len(t_contents)):
    if re.match('reg data_In_write_r;', t_contents[i]):
        start_index = i
    if re.match('endmodule', t_contents[i]):
        end_index = i
write_list = t_contents[start_index: end_index+1]
print(write_list)
t.close()
