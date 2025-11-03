from controller.pid import PID
from controller.utils import get_sim_data, send_control_command

class FlightController:
    def __init__(self):
        self.altitude_pid = PID(1.0, 0.1, 0.05)
        self.target_altitude = 10.0

    def control_loop(self):
        pass

if __name__ == '__main__':
    fc = FlightController()
    fc.control_loop()
