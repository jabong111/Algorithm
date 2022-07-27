CC=g++
CFLAGS=-g -Wall
LDFLAGS=
LDLIBS=
OBJS=main.o
TARGET=main
 
all: $(TARGET)
 
clean:
	rm -f *.o
	rm -f $(TARGET)
 
$(TARGET): $(OBJS)
	$(CC) -o   $@ $(OBJS)
