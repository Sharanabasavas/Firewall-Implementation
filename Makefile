all: packet_filter

packet_filter: packet_filter.c
    gcc -o packet_filter packet_filter.c -lpcap

clean:
    rm -f packet_filter
