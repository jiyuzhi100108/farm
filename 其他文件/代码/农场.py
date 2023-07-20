global l1
l1 = 0
global l2
l2 = 0
global la
la = 0


self.robot_gpio_control(23,0)
self.robot_usbhubControl(0)
while True:
  l1 = self.robot_analogy_feedback(0)
  l2 = self.robot_analogy_feedback(1)
  la = (l1 + l2) / 2
  self.log_out_put(la)
  if la < 1000:
    self.log_out_put('光照过强，开启遮光')
    self.robot_usbhubControl(1)
    self.robot_loop_wait(10)
    self.robot_usbhubControl(0)
  elif la > 10000:
    self.log_out_put('光照过弱，开启补光')
    self.robot_gpio_control(23,1)
    self.robot_loop_wait(10)
    self.robot_gpio_control(23,0)
  else:
    pass
  if(self.stopFlag):
    break
