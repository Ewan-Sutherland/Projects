# Creating the event classes

# Parent class
class Event:
    pass

# Child classes

# Market event class
class MarketEvent(Event):
    def __init__(self):
        self.type = 'MARKET'

# Signal event class
class SignalEvent(Event):
    def __init__(self, symbol, datetime, signal_type):
        self.type = 'SIGNAL'
        self.symbol = symbol
        self.datetime = datetime
        self.signal_type = signal_type

# Order event class
class OrderEvent(Event):
    def __init__(self, symbol, order_type, quantity, direction):
        self.type = 'ORDER'
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction

# Fill event class
class FillEvent(Event):
    def __init__(self, timeindex, symbol, quantity, direction, fill_cost, commission=None):
        self.type = 'FILL'
        self.timeindex = timeindex
        self.symbol = symbol
        self.quantity = quantity
        self.direction = direction
        self.fill_cost = fill_cost