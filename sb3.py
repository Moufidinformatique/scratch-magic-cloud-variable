while True:
  while True:
    from scratch2py import Scratch2Py
    from random import randint
    from time import sleep
    try:
      x=Scratch2Py("moufidali","marjane400").scratchConnect("1062091782")
    except:
      break
    while True:
      try:
        x.setCloudVar("magic variable" , randint(0,100))
        sleep(2)
        project = s2py.project('1063833656')
        print(project.getStats())
      except:
        break