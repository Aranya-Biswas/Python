details={}
def contact(name,ph1,ph2=102):
    details[name]=[ph1,ph2]

contact('python',999999999)
contact(100,'dsp')
print(details)