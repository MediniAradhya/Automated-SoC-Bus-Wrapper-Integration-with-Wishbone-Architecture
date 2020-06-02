module wishbone_top(
           wb_adr_i, wb_cyc_i, wb_dat_i, wb_sel_i,
           wb_stb_i, wb_we_i,
           wb_ack_o, wb_err_o, wb_dat_o,
           wb_clk_i, wb_rst_i, int_o
       );
parameter dw = 32;
parameter aw = 32;
input [aw-1:0]      wb_adr_i;
input               wb_cyc_i;
input [dw-1:0]      wb_dat_i;
input [3:0]         wb_sel_i;
input               wb_stb_i;
input               wb_we_i;
output              wb_ack_o;
output              wb_err_o;
output reg [dw-1:0] wb_dat_o;
output              int_o;
input               wb_clk_i;
input               wb_rst_i;
assign wb_ack_o = 1'b1;
assign wb_err_o = 1'b0;
assign int_o = 1'b0;
// Internal registers
reg next, next_r, next_out_r;
reg data_valid, data_In_write, data_In_write_r;
wire next_out, next_posedge;
reg [15:0] i;
wire next_out_posedge = next_out & ~next_out_r;
wire next_out_posedge = next_out & ~next_out_r;
wire next_posedge = next & ~next_r;
wire data_In_write_posedge = data_In_write & ~data_In_write_r;
reg [63:0] dataX [0:31];
reg [63:0] dataY [0:31];
wire [63:0] dataIn;
wire [63:0] dataOut, data_Out;
reg [63:0] data_In_data, data_In_addr;
reg [63:0] data_Out_addr;

// Implement MD5 I/O memory map interface
// Write side
always @(posedge wb_clk_i)
    begin
        if(wb_rst_i)
            begin
                next          <= 0;
                data_In_write <= 0;
                data_In_addr  <= 0;
                data_In_data  <= 0;
            end
        else if(wb_stb_i & wb_we_i)
            case(wb_adr_i[5:2])
                0:
                    next          <= wb_dat_i[0];
                1:
                    data_In_write <= wb_dat_i[0];
                2:
                    data_In_addr  <= wb_dat_i;
				3:
					data[31:0]  <= wb_dat_i;
				4:
					data[63:32]  <= wb_dat_i;
				5:
					data_Out_addr      <= wb_dat_i;
                default:
                    ;
            endcase
    end // always @ (posedge wb_clk_i)

// Implement MD5 I/O memory map interface
// Read side
always @(*)
    begin
        case(wb_adr_i[5:2])
            0:
                wb_dat_o = {31'b0, next};
            1:
                wb_dat_o = {31'b0, data_In_write};
            2:
                wb_dat_o = data_In_addr;
			3:
				wb_dat_0 = data_In_data[31:0];
			4:
				wb_dat_0 = data_In_data[63:32];
			5:
				data_Out_addr <= wb_dat_i;
			6:
				wb_dat_0 = data_Out[31:0];
			7:
				wb_dat_0 = data_Out[63:32];
            default:
                wb_dat_o = 32'b0;
        endcase
    end //
dft_top dft_top(
				. clk(connect to wishbone),
				. reset(connect to wishbone),
				. next(connect to wishbone),
				. next_out(connect to wishbone),
				.X0(connect to wishbone),
				. Y0(connect to wishbone),
				.X1(connect to wishbone),
				. Y1(connect to wishbone),
				.X2(connect to wishbone),
				. Y2(connect to wishbone));
always @ (posedge wb_clk_i)
	begin
            data_In_write_r <= data_In_write;
    end
always @ (posedge wb_clk_i)
	begin
            dataX[data_In_addr] <= data_In_data;
    end
assign data_Out = dataY[data_Out_addr];
always @ (posedge wb_clk_i)
	begin
            next_r      <= next;
    end
always @ (posedge wb_clk_i)
	begin
		if(next_posedge)
            xSel    <= 6'h00;
        else if(xSel<6'b100000)
            xSel    <= xSel + 1;
    end
assign dataIn = (xSel<6'b100000) ? dataX[xSel] : 32'b0;
always @ (posedge wb_clk_i)
	begin
            next_out_r <= next_out;
    end
always @ (posedge wb_clk_i)
	begin
		if(next_out_posedge)
            begin
                ySel <= 6'h00;
            end
        else if(ySel<6'b100000)
            begin
                ySel <= ySel +1;
                dataY[ySel] = dataOut;
            end
    end
always @ (posedge wb_clk_i)
	begin
		if(next_posedge)
            begin
                data_valid <= 0;
            end
        else if(next_out_posedge)
            begin
                data_valid <= 1;
            end
    end
endmodule
in
                data_valid <= 1;
            end
    end
endmodule
