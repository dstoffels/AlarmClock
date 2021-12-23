import helpers

class AlarmClock:
  def __init__(self) -> None:
      self.set_time()
      self.alarm_time = self.current_time
      self.alarm_is_on = False

  def get_time(self):
    print(f'\nThe time is: {self.current_time}')
  
  def set_time(self):
    self.current_time = input('Set Time: ')
    print(f'\nTime set to: {self.current_time}')
  
  def set_alarm_time(self):
    self.alarm_time = input('Set Alarm: ')
    self.alarm_is_on = True
    print(f'\nAlarm set for: {self.alarm_time}')
  
  def toggle_alarm(self):
    self.alarm_is_on = not self.alarm_is_on
    helpers.alarm_toggled(self.alarm_is_on)
  