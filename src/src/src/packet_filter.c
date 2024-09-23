#include <pcap.h>
#include <stdio.h>
#include <arpa/inet.h>

void packet_handler(u_char *user_data, const struct pcap_pkthdr* pkthdr, const u_char* packet) {
    printf("Packet captured\n");
}

int main() {
    pcap_t *handle;
    char error_buffer[PCAP_ERRBUF_SIZE];
    char *device = "eth0";  // Use appropriate interface

    // Open live capture
    handle = pcap_open_live(device, BUFSIZ, 1, 1000, error_buffer);
    if (handle == NULL) {
        printf("Could not open device %s: %s\n", device, error_buffer);
        return 2;
    }

    // Capture packets indefinitely
    pcap_loop(handle, 0, packet_handler, NULL);

    // Close the handle
    pcap_close(handle);
    return 0;
}
