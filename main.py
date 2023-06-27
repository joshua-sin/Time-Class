class Time(object):
  #the basic function for defining a class. Each object has an hours and a minutes property
  #it is possible to specify an object in minutes only, like 0:70 (70 minutes) being equal to 1:10 (1 hour 10 minutes)
  def __init__(self,hours,minutes):
    self.hours = int(hours)
    self.minutes = int(minutes)
    
  #defining getter methods
  def get_h(self):
    return self.hours
  def get_m(self):
    return self.minutes
    # *no setter methods were necessary for the app this was built for
  
  #To add 2 timestamps together, we need to add both hours and minutes. 
  #then we update the new time so that minutes < 60
  #self can be interpreted as the current timestamp / amount of time, while new will be the amount of time you want to add
  def __add__(self,new):
    a = self.get_h() + new.get_h()
    b = self.get_m() + new.get_m()
    #if minutes is >= 60, it will adjust so that every 60 minutes is converted to an hour.
    a += b//60
    b = b%60
    return Time(a,b)

  #to subtract one time from another
  def __sub__(self,new):
    a = self.get_h() - new.get_h()
    b = self.get_m() - new.get_m()
    #returns the subtracted time if both hours and minutes > 0. Also adjusts so that minutes < 60
    if a >= 0 and b >= 0:
      a += b//60
      b = b%60
      return Time(a,b)
    #if hours is less than 0 but minutes is more than 60...
    elif a < 0 and b >= 60:
      #we will check if the number of minutes is enough to make up the number of 'negative' hours.
      #e.g.  -1 hours and 60 minutes would altogether result in 0 hours and 0 minutes.
      #-2 hours and 60 minutes would result in -1 hours
      #-1 hours and 120 minutes would result in 60 min = 1 hour
      a += abs(b//60)
      b = abs(b%60)
      #if hours is still less than 0 even after adding all the 'hours'
      if a < 0:
        return 0
      #but if the Time is valid and both hours and minutes are positive, it returns the time
      else:
        return Time(a,b)
    #if a < 0 and b < 60, there is no possibility that the time is valid and real
    elif a < 0:
      return 0
    #if minutes < 0 and hours == 0, since you cannot have negative minutes only return 0
    elif a == 0 and b < 0:
      return 0
    #if minutes < 0 BUT hours > 0, it is possible that the hours, when converted to minutes...
    #would make the minutes positive
    #e.g. 2 hours and -100 minutes = 20 minutes
    elif a > 0 and b < 0:
      b += (a*60)
      a //= 60
      if b < 0:
        return 0
      else:
        return Time(a,b)
        
  #to print a Time object
  def __str__(self):
    return str(self.hours).zfill(2) + ':' + str(self.minutes).zfill(2)
    
  #to return a Time object
  def __repr__(self):
    return str(self.hours).zfill(2) + ':' + str(self.minutes).zfill(2)

  #to check if two Time objects are equal or not. Both hours and minutes need to be equal.
  #we ensure that minutes < 60 and the appropriate number of hours is added.
  def __eq__(self,new):
    a = Time(self.get_h() + (self.get_m()//60), self.get_m()%60)
    b = Time(new.get_h() + (new.get_m()//60), new.get_m()%60)
    return ((a.get_h() == b.get_h()) and (a.get_m() == b.get_m()))
    
  #to check if two Time objects are not equal to each other.
  #if either the hours or the minutes are different, the two Times are different
  #we ensure that minutes < 60 and the appropriate number of hours is added.
  def __ne__(self,new):
    a = Time(self.get_h() + (self.get_m()//60), self.get_m()%60)
    b = Time(new.get_h() + (new.get_m()//60), new.get_m()%60)
    return ((a.get_h() != b.get_h()) or (a.get_m() != b.get_m()))
  
  def __lt__(self,new):
    a = new - self
    if type(a) != int:
      return 1
    else:
      return 0
