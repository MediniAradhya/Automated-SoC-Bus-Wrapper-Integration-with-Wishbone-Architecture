import re

i = 0
j = 0
jj = 0
line1 = []
line2 = []
data_req = []
in_out = []
kk = []
in_out_g = []

file_name = input("name of the file to read ")

# opening the file
with open(file_name + '.v') as f:
    data = f.readlines()

for line in data:
    i = i + 1
    if re.match("module", line):
        line1.append(i)
    if re.match("endmodule", line):
        line2.append(i)

for line in data:
    j = j + 1
    if line1[0] < j < line2[0]:
        data_req.append(line.strip())

# print(data_req)

for line in data_req:
    if re.match('(input|output)', line):
        print(line)
        if ';' in line:
            kk.append(line.split(';'))
        if ',' and not '//' in line:
            kk.append(line.split(','))

for xx in range(0, len(kk)):
    if '[' in kk[xx][-1]:
        del kk[xx][-1]
print(kk)
print('gg')

for xx in range(0, len(kk)):
    in_out_g.append(kk[xx][0].split())

print(in_out_g)

for aa in range(0, len(in_out_g)):
    in_out.append([in_out_g[aa][0], in_out_g[aa][-1]])
print('gg')
print(in_out)

data_length_input = int(input("data input length "))
output_length = int(input("output length "))
req_length = int(data_length_input / 32)
out_length = int(output_length / 32)


def write_infile(inp_file, out_file):
    with open(inp_file, 'r') as read_file, open(out_file, 'a') as write_file:
        for line in read_file:
            write_file.write(line)
            write_file.write("\n")


def data_transfer(variable1, variable2, operator, out_file):
    if operator == '<=':
        with open(out_file, 'a') as write_file:
            gg = variable1 + '<=' + variable2
            write_file.write(gg)
            write_file.write("\n")
    if operator == '=':
        with open(out_file, 'a') as write_file:
            gg = variable1 + '=' + variable2
            write_file.write(gg)
            write_file.write("\n")

    return


def data_transfer_case(num, variable1, variable2, operator, out_file):
    if operator == '<=':
        with open(out_file, 'a') as write_file:
            gg = num + ':' + variable1 + '<=' + variable2
            write_file.write(gg)
            write_file.write("\n")
    if operator == '=':
        with open(out_file, 'a') as write_file:
            gg = num + ':' + variable1 + '=' + variable2
            write_file.write(gg)
            write_file.write("\n")

    return


with open('top_gg.v', 'a') as f:
    f.write('module ' + file_name + '_top(')

write_infile('intro.txt', 'top_gg.v')

with open('top_gg.v', 'a') as f:
    f.write('reg [31:0] data ' + '[0:' + str(req_length - 1) + '];' + '\n')
    f.write('wire [' + str(output_length - 1) + ':0] hash;' + '\n')
    f.write('wire [' + str(data_length_input - 1) + ':0] bigData = {')

    for i in range((req_length - 1), -1, -1):
        if i == 0:
            f.write('data[' + str(i) + ']')
        else:
            f.write('data[' + str(i) + '],')

with open('top_gg.v', 'a') as f:
    f.write('};' + '\n')

write_infile('write_case_start.txt', 'top_gg.v')

for i in range(0, req_length):
    data_transfer('data[' + str(i) + ']', '0;', '<=', 'top_gg.v')

write_infile('write_side.txt', 'top_gg.v')

for i in range(0, req_length):
    data_transfer_case(str(i + 1), 'data[' + str(i) + ']', 'wb_dat_i;', '<=', 'top_gg.v')
write_infile('read_side.txt', 'top_gg.v')

for i in range(0, req_length):
    data_transfer_case(str(i + 1), 'wb_dat_o', 'data[' + str(i) + '];', '=', 'top_gg.v')

data_transfer_case(str(i + 2), 'wb_dat_o', "{31'b0, hashValid};", '=', 'top_gg.v')

for i in range(i + 2, i + 2 + out_length):
    data_transfer_case(str(i + 1), 'wb_dat_o', 'hash[' + str(jj + 31) + ':' + str(jj) + '];'
                                                                                        '', '=', 'top_gg.v')
    jj = jj + 32

write_infile('end_case_read.txt', 'top_gg.v')
with open('top_gg.v', 'a') as f:
    module_name = file_name + '  ' + file_name + '('
    f.write(module_name)

    for i in range(0, len(in_out)):
        dot = '.' + in_out[i][1] + '()' + ','
        if i == len(in_out)-1:
            f.write(dot[:-1] + ');\nendmodule')
        else:
            f.write(dot)


