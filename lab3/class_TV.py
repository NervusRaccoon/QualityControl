class TV:
    def __init__(self):
        self._is_on = False
        self._channel = 0
        self._prev_channel = 0
        self._MIN_CHANNEL = 1
        self._MAX_CHANNEL = 99

    def turn_on(self):
        self._is_on = True
        return True

    def turn_off(self):
        self._is_on = False
        return True

    def find_state_TV(self):
        return self._is_on

    def find_channel(self):
        if self._is_on == True:
            return self._channel
        return 0

    def is_channel_in_range_channel(self, number_channel):
        return self._MIN_CHANNEL <= number_channel <= self._MAX_CHANNEL
		
    def is_prev_channel_in_range_channel(self):
        return self._MIN_CHANNEL <= self._prev_channel <= self._MAX_CHANNEL

    def select_channel(self, number_channel):
        if self._is_on and self.is_channel_in_range_channel(number_channel):
            self._prev_channel = self._channel
            self._channel = number_channel
        return True

    def select_previous_channel(self):
        if self.is_prev_channel_in_range_channel() and self.is_channel_in_range_channel(self._channel):
            if self._prev_channel != self._channel:
                self._prev_channel, self._channel = self._channel, self._prev_channel
        return True