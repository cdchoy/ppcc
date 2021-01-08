# PPSuite
Presenting the future of software development: Powerpoint.  

[Uncommon Hacks Hackathon](https://uncommonhacks.com/) 2019 Submission. See the Devpost project here: https://devpost.com/software/ppcc.
Awarded "Most Technically Impressive 2019"

## Abstract

What if you could execute your C code in Powerpoint?

At Carnegie Mellon's 11th annual [SIGBOVIK](http://sigbovik.org/) in 2017, Tom Wildenhain unveiled the [Powerpoint Turing Machine](https://www.andrew.cmu.edu/user/twildenh/PowerPointTM/Paper.pdf) (aka PPTXTM), a [Turing Machine](https://en.wikipedia.org/wiki/Turing_machine) that could function entirely in Powerpoint. The implications? Groundbreaking. The usability? Lacking. To operate the PPTXTM, one needs to write executable punch cards; a technique made obsolete in the **1960s**.

And so in 2019, we are proud to introduce the PPSuite, a collection of software engineered to greatly improve your Powerpoint programming experience.

* PPCPU: a cpu built on Turing Machines that function entirely in Powerpoint. This includes 256 bytes of memory, 8 registers, an instruction code heap, and several Arithmetic Logic Units implemented on Turing Machines.  

* PPAPI: a collection of functions for interfacing with Powerpoint and our PPTXTMs

* PPCC: a compiler that will convert a .c file to a .ppasm file, out own ASM format

* PPEXE: an executor to handle read/writes as well as instruction decoding, loading, and execution. All meaningful computation and storage is still performed on PPCPU.

* PPASM: our custom assembly language

## Motivations

* no one tried to stop us
* good memes
* we're trying to remove powerpoint from the App Store

## The Team

* [Kevin He](https://github.com/echowisp)  
* [Chris Choy](https://github.com/cchoy96)  
* [Dawson Whitehead](https://github.com/dwahme)  
* [April Wang](https://github.com/aprilyw)  

## Architecture

C -> ELVM -> PPASM -> PPEXE <-> PPAPI <-> PPCPU

We convert C language to PPASM, our custom assembly language for interfacing with PPCPU. To bridge these 2 languages, we utilized a personally modified version of the Esoteric Language Virtual Machine, [ELVM](https://github.com/shinh/elvm/blob/master/ELVM.md?fbclid=IwAR2fsBSlkAFs3sTNRWkGrZycb_oATt_ElK7se8vLm4k5gPK8r2bCVOelR2k), to produce PPASM. From here, PPEXE loads the instructions into PPCPU using PPAPI.

Next, we decode through the instructions using PPEXE, a Python executor that functions solely to make ordered calls to our PPAPI. PPAPI utilizes [AutoHotKey](https://www.autohotkey.com/) to abstract out the human clicker required for manually executing our PPTXTM cycles.

## Usage

To use our PPSuite, a user will need to write a C file, say foo.c, and then compile it to PPASM with:
```
$ python3 ppsuite/ppcc <some c file>
```

Next, open the PPCPU PowerPoint. Make sure your default screen is 1920x1080, or else the screen detection and autohotkey input won't work (TODO- detect resolution and auto adjust)

Next, run the program with
```
$ python3 ppsuite/ppexe <some .ppasm file>
```

### Virtualization

Want to develop on the PPCPU but don't meet the dependency requirements? There's a virtual machine option in the PPAPI class that should be able to run a virtual PPCPU with basically no dependencies. It'll run everything on a PPCPU simulator instead of a real powerpoint. (We know it kinda defeats the purpose, but 2 second runtime makes testing significantly easier than a 5 minute one.)

To do so, you'll need to make a `PPEXE` object with the `ppt` specified as `None`. Then, you'll need to update the `if __name__ == "__main__"` section in `ppexe.py`. Then, you should be able to remove the win32* dependencies as well as anything to do with window management (just try removing stuff until it breaks).

TODO- make virtualization usage more streamlined

## Challenges

1) We had no a priori knowledge on how Turing Machines or Punch Cards actually worked...

2) While it is theoretically possible to reduce all programming languages to Turing Machine language, it has been *neither proven nor implemented*. And so our initial plan to convert C -> [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) -> Turing Machine -> PPTXTM Punch Cards, was immediately established as both nontrivial and night impossible given our time and resources. Thus, we aimed to produce a CPU that could execute all meaningful computation in Powerpoint rather than a C->PPTXTM compiler (formally known as PPCC).  

3) PPTXTM's tape length is unfortunately finite. In this implementation, we wrote all code to function on a Turing Machine with a relatively small 8 bits and 8 states. Since 1600+ animations are required to run this, and  Since our tape was not long enough to support reading and writing, we utilized Python for reading and writing to our PPT memory/registers/tape.

## Code Dependencies

* Microsoft Powerpoint
* Python 3.7
* AutoHotKey
* win32COM
* 1920x1080 aspect ratio (we wish we were joking; all the input values are hardcoded to this size)

## Acknowledgements

We'd like to thank Tom Wildenhain for their work in creating and distributing PPTXTM, Uncommon Hacks for hosting this Hackathon, and Microsoft for creating **the** omnipotent software, Powerpoint.
