
def validate_int_input(prompt):
  while True:
    try:
      response = int(input(prompt))
      return response
    except:
      prompt = 'Please enter a number'

def toggle_alarm_prompt_str_bldr(alarm_on) -> str:
  if(alarm_on):
    return 'Deactivate alarm'
  else:
    return 'Activate Alarm'

def alarm_toggled(alarm_on) -> str:
  if(alarm_on):
    print('Alarm ON')
  else:
    print('Alarm OFF')