# clutchplugin by Ryan Otis

import gremlin
import threading
import time
from gremlin.user_plugin import *

mode = ModeVariable("Mode", "Mode in which to use these settings")

leftPaddle = PhysicalInputVariable(
    "Left Clutch Paddle",
    "Physical Clutch Paddle on left side of wheel",
    [gremlin.common.InputType.JoystickAxis]
)

rightPaddle = PhysicalInputVariable(
    "Right Clutch Paddle",
    "Physical Clutch Paddle on right side of wheel",
    [gremlin.common.InputType.JoystickAxis]
)

output = VirtualInputVariable(
    "Output Axis",
    "vJoy device and axis to use as the output",
    [gremlin.common.InputType.JoystickAxis]
)

bitePoint = IntegerVariable(
    "Default Bite Point",
    "Default bite point percentage",
    50,
    1,
    100
)

decBitePoint = PhysicalInputVariable(
    "Decrease Bite Point",
    "Button that decreases the current bite point",
    [gremlin.common.InputType.JoystickButton]
)

incBitePoint = PhysicalInputVariable(
    "Increase Bite Point",
    "Button that increases the current bite point",
    [gremlin.common.InputType.JoystickButton]
)

g_bitePoint = bitePoint.value
g_leftValue = 0.0
g_rightValue = 0.0

def update_axis(vjoy):
    leftPaddleTarget = g_leftValue * (g_bitePoint/100)
    value = gremlin.util.clamp(max(leftPaddleTarget,g_rightValue),-1.0,1.0)
    vjoy[output.vjoy_id].axis(output.input_id).value = value

decorator_leftPaddle = leftPaddle.create_decorator(mode.value)
decorator_rightPaddle = rightPaddle.create_decorator(mode.value)
decorator_incBitePoint = incBitePoint.create_decorator(mode.value)
decorator_decBitePoint = decBitePoint.create_decorator(mode.value)

@decorator_leftPaddle.axis(leftPaddle.input_id)
def leftPaddleAxis(event, vjoy):
    global g_leftValue
    g_leftValue = event.value
    update_axis(vjoy)

@decorator_rightPaddle.axis(rightPaddle.input_id)
def rightPaddleAxis(event, vjoy):
    global g_rightValue
    g_rightValue = event.value
    update_axis(vjoy)

@decorator_incBitePoint.button(incBitePoint.input_id)
def incBPbtn(event, vjoy):
    global g_bitePoint
    g_bitePoint += 1 if event.is_pressed else g_bitePoint
    update_axis(vjoy)

@decorator_decBitePoint.button(decBitePoint.input_id)
def decBPbtn(event, vjoy):
    global g_bitePoint
    g_bitePoint -= 1 if event.is_pressed else g_bitePoint
    update_axis(vjoy)
