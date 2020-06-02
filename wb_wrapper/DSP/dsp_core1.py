import re

my_list = []
io_list = []
bit_list = []
write_list = []
dict_io = {}
dict_bit = {}
i = 0
out_size =0
string = ''
final = []
base_number = 32
name_file = input("Enter Dsp_block name: ")
in_size = int(input("Enter input size "))
in_size = out_size = 64   # 32 for fir/iir , 64 for dft/idft
rem_in = in_size / base_number
rem_out = in_size / base_number

in_size = out_size
#name_file = 'IIR_filter'
name_module = ''
name = ''
for char in name_file:
    if char != '.':
        name += char
    else:
        break
name = name.lower()
#print(name)
if name.find('iir') >-1 or name.find('fir') > -1:
    name_module = 'module '+name_file+' '   #for FIR and IIR
else:
    name_module = 'module '+name_file #for DFT and IDFT

with open(name_file+'.v', 'r') as f:
    f_contents = f.readlines()
start_index = 0
end_index = 0
for i in range(len(f_contents)):
    if re.match(name_module, f_contents[i]):
        start_index = i
for i in range(start_index, len(f_contents)):
    if re.match('endmodule', f_contents[i]):
        end_index = i
        break
#print(end_index)
my_list = f_contents[start_index: end_index + 1]
#print(my_list)
for line in my_list:
    if re.match('input',line.strip()) or re.match('output', line.strip()):
        if re.search('\[.*?\]',line):
            io_list.append(line.strip().split())
        else:
            bit_list.append(line.strip().split())
#print(io_list)
for i in range(len(io_list)):
    dict_io[i] = {'type': io_list[i][0], 'size': io_list[i][1], 'name': io_list[i][2]}
for i in range(len(bit_list)):
    dict_bit[i] = {'type': bit_list[i][0], 'name': bit_list[i][1]}
name = ''
for char in name_file:
    if char != '.':
        name += char
    else:
        break
name = name.lower()
#print(name)
if name.find('iir') >-1 or name.find('fir') > -1:
    #print('yes1')
    temp = []
    for i in range(len(dict_io)):
        temp.append(dict_io[i]['name'].strip(';'))
#print(temp)
    temp1 = []
    for i in range(len(dict_bit)):
        temp1.append(dict_bit[i]['name'].strip(';'))
else:
    #print('yes2')
    remove = 'module ' + name_file + '('
    for i in range(len(my_list)):
        if re.search(';', my_list[i]):
            break
        else:
            string = string + (my_list[i].strip())
    # print(string)
    x = string.replace(remove, ' ')
 #   print(x)
    final = (x[0:(len(x) - 1)]).split(',')
#print(temp1)
#print(io_list)
#print(bit_list)
#print(dict_io)
#print(dict_bit)
#print(dict_io[0]['size'])
f.close()

# a = ''
# nums = []
# for key,value in dict_io.items():
#     num = ''
#     a = value['size']
#     for i in range(1, len(a)):
#         if a[i] != ':':
#             num += a[i]
#         else:
#             nums.append(int(num) + 1)
#             break
#print(nums)
#print(in_size)
#print(out_size)

with open('default.v', 'r') as f:
    f_contents = f.readlines()

f1 = open("top_wrapper.v", "w+")
f1.writelines(f_contents[0:32])
f1.write('reg ['+str(in_size-1)+':0] dataX [0:31];'+'\n')
f1.write('reg ['+str(out_size-1)+':0] dataY [0:31];'+'\n')
f1.writelines('wire ['+str(in_size-1)+':0] dataIn;'+'\n')
f1.writelines('wire ['+str(out_size-1)+':0] dataOut, data_Out;'+'\n')
f1.writelines('reg ['+str(in_size-1)+':0] data_In_data, data_In_addr;'+'\n')
f1.writelines('reg ['+str(out_size-1)+':0] data_Out_addr;'+'\n')
f1.writelines(f_contents[32:52])


if int(rem_in) >= 1:
    for i in range(int(rem_in)):
        f1.write('\t\t\t\t'+str(i+3)+':\n')
        str2 = f"\t\t\t\t\tdata[{base_number * (i + 1) - 1}:{base_number * (i)}]  <= wb_dat_i;"
        f1.write(str2)
        f1.write("\n")
f1.write('\t\t\t\t'+str(i+4)+':\n\t\t\t\t\tdata_Out_addr      <= wb_dat_i;\n')
f1.writelines(f_contents[56:72])
if int(rem_in) >= 1:
    for i in range(int(rem_in)):
        f1.write('\t\t\t'+str(i+3)+':\n')
        str2 = f"\t\t\t\twb_dat_0 = data_In_data[{base_number * (i + 1) - 1}:{base_number * i}];"
        f1.write(str2)
        f1.write("\n")
f1.write('\t\t\t'+str(i+4)+':\n\t\t\t\tdata_Out_addr <= wb_dat_i;\n')
j = i+5
if int(rem_out) >= 1:
    for i in range(int(rem_out)):
        f1.write('\t\t\t'+str(i+j)+':\n')
        str2 = f"\t\t\t\twb_dat_0 = data_Out[{base_number * (i + 1) - 1}:{base_number * (i)}];"
        f1.write(str2)
        f1.write("\n")
f1.writelines(f_contents[80:84])
sens_1 = 'always @ (posedge wb_clk_i or posedge wb_rst_i)\n\tbegin\n\t\tif (wb_rst_i)\n'
sens_2 = 'always @ (posedge wb_clk_i)\n\tbegin\n'
#f1.write(sens_1)
#f1.write(sens_2)
f1.write(name+' '+name+'(\n')
# module name instantiation

#f2 = open("temp2.txt", "w+")
#print("debug", name.index('fir'))
if name.find('iir') >-1 or name.find('fir') > -1:
   # print('yes')
    for i in range(len(temp1)):
        # print(temp1[i])
        f1.write('\t\t\t\t.' + temp1[i] + '(connect to wishbone),\n')
    for i in range(len(temp) - 1):
        f1.write('\t\t\t\t.' + temp[i] + '(connect to wishbone),\n')
    z = len(temp) - 1
    f1.write('\t\t\t\t.' + temp[z] + '(connect to wishbone));\n')
    f1.write(sens_1)
    f1.write('\t\t\tdata_In_write_r <= 0;\n\t\telse\n')
    f1.writelines(f_contents[98:100])
    f1.write('reg [5:0] count;\n')
    f1.write(sens_1)
    f1.writelines(f_contents[103:109])
    f1.write(sens_1)
    f1.writelines(f_contents[112:116])
    f1.write(sens_1)
    f1.writelines(f_contents[120:127])
    f1.write(sens_1)
    f1.writelines(f_contents[131:142])
    f1.write(sens_1)
    f1.writelines(f_contents[147:151])
    f1.write(sens_1)
    f1.writelines(f_contents[155:169])
    f1.write(sens_1)
    f1.writelines(f_contents[170:184])
else:
  #  print('no')
    for i in range(len(final) - 1):
        # print(temp1[i])
        f1.write('\t\t\t\t.' + final[i] + '(connect to wishbone),\n')
    z = (len(final) - 1)
    f1.write('\t\t\t\t.' + final[z] + '(connect to wishbone));\n')
    f1.write(sens_2)
    f1.writelines(f_contents[98:100])
    f1.write(sens_2)
    f1.writelines(f_contents[106:109])
    f1.write(sens_2)
    f1.writelines(f_contents[114:116])
    f1.write(sens_2)
    f1.write('\t\tif(next_posedge)\n')
    f1.writelines(f_contents[122:127])
    f1.write(sens_2)
    f1.writelines(f_contents[149:151])
    f1.write(sens_2)
    f1.write('\t\tif(next_out_posedge)\n')
    f1.writelines(f_contents[160:169])
    f1.write(sens_2)
    f1.write('\t\tif(next_posedge)\n')
    f1.writelines(f_contents[175:184])
print('done')

