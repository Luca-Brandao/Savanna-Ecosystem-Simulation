import random as r

def is_drought():
    return r.random() < 0.1

def is_famine():
    return r.random() < 0.01

def is_baby_boom():
    return r.random() < 0.05