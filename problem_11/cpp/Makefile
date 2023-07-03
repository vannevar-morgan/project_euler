OBJS_P11 = problem_11.o
CC = g++
CFLAGS = -c -Wall -Werror -pedantic -std=c++20

all : test_p11

test_p11 : $(OBJS_P11)
	$(CC) $(OBJS_P11) -o test_p11

problem_11.o : problem_11.cpp
	$(CC) $(CFLAGS) problem_11.cpp

clean:
	\rm -rf *.o
