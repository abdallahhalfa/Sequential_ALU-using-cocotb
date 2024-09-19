module SEQ_ALU ( input clk,rst,en,
                 input signed [3:0] A,B,
		 input [1:0] opcode,
                 output reg signed [4:0] C );
always@(posedge clk, negedge rst)
 begin
  if(!rst)
   begin
    C<=0;
   end
  else if(en)
   begin
    case(opcode)
     2'b00:
       begin
      	C<=A+B;
       end
     2'b01:
       begin
      	C<=A-B;     
       end
     2'b10:
       begin
      	C<=A&B;      
       end
     2'b11:
       begin
      	C<=A|B;      
       end
     default:
       begin
      	C<=0;      
       end
    endcase
   end
 end 
endmodule