class LeapYear():

    def is_leap_year_v1(self, year):
        if (year%4==0):
            return True
        else:
            return False

            
    def is_leap_year_v2(self, year):
        if (year%4==0 and year%100!=0 or year%400==0):
            return True
        else:
            return False
