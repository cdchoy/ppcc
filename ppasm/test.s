	.text
main:
	mov D, SP
	add D, -1
	store BP, D
	mov SP, D
	mov BP, SP
	.file 1 "./elvm/toy_c/test.c"
	.loc 1 3 0
	# }
	.loc 1 2 0
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
	mov D, SP
	add D, -1
	store C, D
	mov SP, D
	mov C, 0
	binopAdd0:
	add A, 1
	add C, 1
	 jne binopAdd0, C, B
	.loc 1 3 0
	# }
	mov A, 1
	mov B, A
	exit
	exit
