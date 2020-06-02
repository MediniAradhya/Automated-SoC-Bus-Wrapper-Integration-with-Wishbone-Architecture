import re
#import matplotlib.pyplot as plt
my_list = []
io_list = []
bit_list = []
write_list = []
dict_io = {}
i = 0
count = 0
with open('IIR_filter.v', 'r') as f:
    f_contents = f.readlines()
start_index = 0
end_index = 0
for i in range(len(f_contents)):
    if re.match('module IIR_filter ', f_contents[i]):
        start_index = i
for i in range(start_index, len(f_contents)):
    if re.match('endmodule ', f_contents[i]):
        end_index = i
        break
my_list = f_contents[start_index: end_index + 1]
for line in my_list:
    if re.match('input',line.strip()) or re.match('output', line.strip()):
        if re.search('\[.*?\]',line):
            io_list.append(line.strip())
        else:
            bit_list.append(line.strip())

for i in range(len(io_list)):
    dict_io[i] = {'net': io_list[i][0], 'toggle': io_list[i][3]}
print(io_list)
print(bit_list)
f.close()

#with open('iir_top.v', 'r') as f:
#   f_contents = f.readlines()
#for i in range(len(f_contents)):
#    if re.match('module iir', f_contents[i]):
#        start_index = i
#    if re.match('endmodule', f_contents[i]):
#        end_index = i
#write_list = f_contents[start_index: end_index+1]
#print(write_list)
