Simulation Path : 

cd /mnt/d/Academics/SEM4/AVLSI/Project/wb_wrapper/SoCCom_v1.0/cores

Python Auto Top module Generation Path :

cd  /mnt/d/Academics/SEM4/AVLSI/Project/wb_wrapper/DSP


md5 (pancham  512 128) :

:pancham  pancham(.clk(wb_clk_i),.rst(wb_rst_i),.msg_padded(bigData),.msg_in_valid(startHash && ~startHash_r),.msg_output(hash),.msg_out_valid(hashValid),.ready(ready));

sha256 (sha256 , 512 , 256):

sha256 sha256(
           .clk(wb_clk_i),
           .rst(wb_rst_i),
           .init(startHash && ~startHash_r),
           .next(newMessage && ~newMessage_r),
           .block(bigData),
           .digest(hash),
           .digest_valid(hashValid),
           .ready(ready));

dft_top : 

dft_top dft_top(
            .clk(wb_clk_i),
            .reset(wb_rst_i),
            .next(next_posedge),
            .next_out(next_out),
            .X0(dataIn[15:0]),
            .X1(dataIn[31:16]),
            .X2(dataIn[47:32]),
            .X3(dataIn[63:48]),
            .Y0(dataOut[15:0]),
            .Y1(dataOut[31:16]),
            .Y2(dataOut[47:32]),
            .Y3(dataOut[63:48]));

