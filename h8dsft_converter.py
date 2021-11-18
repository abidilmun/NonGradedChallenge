def k2c(kelvin_temprature):
    '''
    this function will convert from kelvin to celcius
    :params:kelvin_temprature|float/int
    '''
    celcius = kelvin_temprature-273.15
    return celcius
def c2k(celcius_temprature):
    '''
    this function will convert from celcius to kelvin
    :params:celcius_temprature|float/int
    '''
    kelvin = celcius_temprature+273.15
    return kelvin
def KorC2fahr(initial_temprature,temprature):
    '''
    this function will convert kelvin or celcius temprature to fahrenheit
    :params:initial_temprature|kelvin\celcius|string
           :temprature|float/int
    '''
    if initial_temprature == 'kelvin':
        res = (k2c(temprature)*9/5)+32
    elif initial_temprature == 'celcius':
        res = (temprature*9/5)+32
    return res
def fahr2KorC(output_temprature,temprature):
    '''
    this function will convert temprature to kelvin or celcius
    :params:output_temprature|kelvin\celcius|string
           :temprature|float/int
    '''
    if output_temprature == 'kelvin':
        res = ((temprature-32)*5/9)+273.15
    elif output_temprature == 'celcius':
        res = (temprature - 32) * 5/9
    return res
