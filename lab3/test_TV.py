import class_TV

class TestProgram:
    def test_check_IsTurnedOff(self):
        TV = class_TV.TV()
        assert TV.find_state_TV() is False

    def test_check_CantSelectChannel(self):
        TV = class_TV.TV()
        assert TV.select_channel(3) is True

    def test_check_CantSelectPrevChannel(self):
        TV = class_TV.TV()
        assert TV.select_previous_channel() is True

    def test_check_ZeroChannel(self):
        TV = class_TV.TV()
        assert TV.find_channel() == 0

    def test_check_CanTurnedOn(self):
        TV = class_TV.TV()
        TV.turn_on()
        assert TV.find_state_TV() is True

    def test_check_CanTurnedOff(self):
        TV = class_TV.TV()
        TV.turn_on()
        TV.turn_off()
        assert TV.find_state_TV() is False

    def test_check_ChannelInRange(self):
        TV = class_TV.TV()
        TV.turn_on()
        assert TV.select_channel(1) is True
        TV.select_channel(1)
        assert TV.find_channel() == 1
        assert TV.select_channel(99) is True
        TV.select_channel(99)
        assert TV.find_channel() == 99
        assert TV.select_channel(50) is True
        TV.select_channel(50)
        assert TV.find_channel() == 50
        assert TV.select_channel(0) is True
        assert TV.select_channel(100) is True

    def test_check_SelectPrevChannel(self):
        TV = class_TV.TV()
        TV.turn_on()
        TV.select_channel(1)
        TV.select_channel(99)
        assert TV.select_previous_channel() is True
        assert TV.select_previous_channel() == 1




