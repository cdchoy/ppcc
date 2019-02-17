	.text
main:
	mov D, SP
	add D, -1
	store BP, D
	mov SP, D
	mov BP, SP
	.file 1 "../elvm/toy_c/test.c"
	.loc 1 8 0
	# }
	.loc 1 5 0
	#     }
	.loc 1 2 0
	#         6 + 3;
	mov A, 1
	jeq .L0, A, 0
	.loc 1 3 0
	#     } else {
	mov A, 6
	mov D, SP
	add D, -1
	store A, D
	mov SP, D
	mov A, 3
	mov B, A
	load A, SP
	add SP, 1
	add A, B
	jmp .L1
	.L0:
	.loc 1 5 0
	#     }
	mov A, 6
	mov D, SP
	add D, -1
	store A, D
	mov SP, D
	mov A, 4
	mov B, A
	load A, SP
	add SP, 1
	add A, B
	.L1:
	.loc 1 7 0
	#     return 1;
	mov A, 5
	mov D, SP
	add D, -1
	store A, D
	mov SP, D
	mov A, 3
	mov B, A
	load A, SP
	add SP, 1
	add A, B
	.loc 1 8 0
	# }
	mov A, 1
	mov B, A
	exit
	exit
