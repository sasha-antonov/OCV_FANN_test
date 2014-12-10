CFFLAGS=-I/usr/local/include/
LDFLAGS=-L/usr/local/lib -lfann -ldoublefann -lfixedfann -lfloatfann -lm

reload: clean train ask run
load: train ask run

train: xor_train.o
	gcc	xor_train.o -o xor_train $(LDFLAGS)
xor_train.o: 
	gcc -v -c $(CFFLAGS) training.c -o xor_train.o

ask: fann.o
	gcc	fann.o -o fann $(LDFLAGS)
fann.o: 
	gcc -v -c $(CFFLAGS) fann.c -o fann.o

clean: 
	rm *.o xor_train fann 
	
run:
	./xor_train
	./fann

