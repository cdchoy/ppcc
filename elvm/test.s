	.text
main:
	mov D, SP
	add D, -1
	store BP, D
	mov SP, D
	mov BP, SP
	sub SP, 2
	.file 1 "./toy_c/test.c"
	.loc 1 9 0
	# }
	.loc 1 6 0
	#
	.loc 1 2 0
	#         int a = 2;
	mov A, 1
	jeq .L0, A, 0
	.loc 1 3 0
	#
	mov A, 0
	mov B, SP
	mov B, BP
	add B, 63
	mov A, 2
	store A, B
	jmp .L1
	.L0:
	.loc 1 6 0
	#
	mov A, 0
	mov B, SP
	mov B, BP
	add B, 62
	mov A, 3
	store A, B
	.L1:
	.loc 1 9 0
	# }
	mov A, 1
	mov B, A
	exit
	exit
