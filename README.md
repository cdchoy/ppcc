# ppcc
Presenting the future of software development: Powerpoint.  

Uncommon Hacks Hackathon 2019 Submission

## Abstract

What if you could execute code in Powerpoint?

Tom Wildenhain produced [PPTXTM](https://www.andrew.cmu.edu/user/twildenh/PowerPointTM/Paper.pdf), a Turing Machine that could function entirely in Powerpoint. The implications? Groundbreaking. The usability? Lacking. To operate the PPTXTM, one needs to write executable punch cards; a technique made obsolete in the **1960s**.

We introduce PPCPU, a cpu functioning entirely in Powerpoint. This includes 256 bytes of memory, 8 registers, and several Arithmetic Logic Units implemented on Turing Machines.  

## Motivations

* No one would tell us not to
* n/a

## The Team

* [Kevin He](https://github.com/echowisp)  
* [Chris Choy](https://github.com/cchoy96)  
* [April Wang](https://github.com/aprilyw)  
* [Dawson Whitehead](https://github.com/dwahme)  

## Architecture

There are 2 main phases to PPCPU:

* Generate instruction list
* Execute instruction list

Throughout this process, we utilize the following files/scripts:  
C -> PPASM -> PPEXE -> PPAPI -> Powerpoint

#### Generating the Instruction List

We convert C language to PPASM, our custom assembly language for interfacing with PPCPU. To bridge these 2 languages, we take an intermediary step to Esoteric Language Virtual Machine, [ELVM](https://github.com/shinh/elvm/blob/master/ELVM.md?fbclid=IwAR2fsBSlkAFs3sTNRWkGrZycb_oATt_ElK7se8vLm4k5gPK8r2bCVOelR2k).

#### Executing the Instruction List

We parse through custom assembly language PPASM using PPEXEC, a Python executor that functions solely to make ordered calls to our PPAPI. PPAPI utilizes [AutoHotKey](https://www.autohotkey.com/) to abstract out the human clicker required for manually executing cycles in PPTXTM.

## Challenges

PPTXTM's tape length is unfortunately finite. In this implementation, we wrote all code to function on a Turing Machine with a relatively small 8 bits and 8 states.

## Code Dependencies

* Microsoft Powerpoint
* Python 3.7
* AutoHotKey

## Acknowledgements
