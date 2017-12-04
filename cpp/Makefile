OBJS_P25 = problem_25.o
OBJS_P25_BIN = problem_25_bin.o
CC = g++
CFLAGS = -c -Wall -Werror -pedantic -std=c++11
CFLAGS_P25_BIN = -DBOOST_LOG_DYN_LINK
LDLIBS_P25_BIN = -lpthread -lboost_system -lboost_log

all : test_p25 test_p25_bin

test_p25 : $(OBJS_P25)
	$(CC) $(OBJS_P25) -o test_p25

test_p25_bin : $(OBJS_P25_BIN)
	$(CC) $(OBJS_P25_BIN) -o test_p25_bin $(LDLIBS_P25_BIN)

problem_25.o : problem_25.cpp
	$(CC) $(CFLAGS) problem_25.cpp

problem_25_bin.o : problem_25_bin.cpp
	$(CC) $(CFLAGS) $(CFLAGS_P25_BIN) problem_25_bin.cpp

clean:
	\rm -rf *.o
