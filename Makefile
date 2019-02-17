.SILENT: all
.SILENT: clean

all:
	cd elvm; \
	cd 8cc; \
	make; \
	cd ..;\
	cd ..;\

clean:
	cd elvm; \
	cd 8cc; \
	make clean; \
	cd ..;\
	cd ..;\