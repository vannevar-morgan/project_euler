OBJS_P12 = problem_12.o
CC = g++
CFLAGS = -c -Wall -Werror -pedantic -std=c++17

all : test_p12

test_p12 : $(OBJS_P12)
	$(CC) $(OBJS_P12) -o test_p12

problem_12.o : problem_12.cpp
	$(CC) $(CFLAGS) problem_12.cpp

clean:
	\rm -rf *.o
