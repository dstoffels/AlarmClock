import helpers
from alarmClock import AlarmClock

alarm_clock = AlarmClock()

while True:
  options = f'''
1) Current Time
2) Set Time
3) Set Alarm
4) {helpers.toggle_alarm_prompt_str_bldr(alarm_clock.alarm_is_on)}
5) Exit
'''

  userInput = helpers.validate_int_input(options)

  match userInput:
    case 1:
      alarm_clock.get_time()
    case 2:
      alarm_clock.set_time()
    case 3:
      alarm_clock.set_alarm_time()
    case 4:
      alarm_clock.toggle_alarm()
    case 5:
      print('Goodbye!')
      exit()