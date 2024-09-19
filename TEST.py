import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.handle import Force, Release, Freeze, Deposit


async def driving_stimilus(dut):
    for i in range(6):
        await FallingEdge(dut.clk)
        dut.rst.value= 0 if(i==0) else 1
        dut.en.value= 1 if(i!=5) else 0
        dut.A.value= 5 
        dut.B.value= 3
        dut.opcode.value = 0 if i == 0 else (i - 1 if i != 5 else 3)
        await RisingEdge(dut.clk)
        await ReadOnly()
        cocotb.log.info(f"rst: {dut.rst.value},en: {dut.en.value},A: {dut.A.value}, B: {dut.B.value}, opcode: {dut.opcode.value}, C: {dut.C.value}")


@cocotb.test()
async def tb_top(dut):
    cocotb.log.info(" STARTING SIMULATION ")
    CLK = Clock(dut.clk, 10, units="ns")
    dut.rst.value = 0 
    await cocotb.start(CLK.start())
    await cocotb.start_soon(driving_stimilus(dut))
    cocotb.log.info(" After Driving Stimilus")
