from bus import Bus

class BusStop:

    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return len(self.queue)
    
    def clear(self):
        self.queue.clear()

    def pick_up_from_stop(self, bus_stop):
        for self.passengers in bus_stop:
            Bus.pick_up()
        self.queue.clear()