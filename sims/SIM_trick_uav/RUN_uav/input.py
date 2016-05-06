##############################################################
# File Description: 
#   Trick-UAV simulation top level input file.
##############################################################

#-------------------------------------------------------------
# Configure Trick and Realtime parameters
#-------------------------------------------------------------
REALTIME = True
if REALTIME :
  trick.real_time_enable()
else :
	trick.exec_set_terminate_time(10.0)
trick.exec_set_trap_sigfpe(True)
trick.exec_set_software_frame(0.1)
trick.exec_set_enable_freeze(REALTIME)
trick.exec_set_freeze_command(REALTIME)
trick.sim_control_panel_set_enabled(REALTIME)
# Set shotcuts for readability.
set_unit_val = trick.sim_services.attach_units

#-------------------------------------------------------------
# Quad model basic constants setup
#-------------------------------------------------------------
mass         = 10.0    # kg
gravity      = 9.81    # m/s2
drag_coeff   = 2.0     # kg/s
# Set the vehicle mass in kg
vehicle.model.mass = set_unit_val("kg", mass)
# Set the initial position in feet.
vehicle.model.position = set_unit_val("ft", [20.0, 0.0, 0.0])
# Set the initial velocity in feet/sec.
vehicle.model.velocity = set_unit_val("ft/s", [0.0, 0.0, 0.0])
# Set the initial acceleration in feet/sec^2.
vehicle.model.acceleration = set_unit_val("m/s2", [-gravity, 0.0, 0.0])

#-------------------------------------------------------------
# Hand controller setup
#-------------------------------------------------------------
# Nothing to do

#-------------------------------------------------------------
# Quad motor model setup
#-------------------------------------------------------------
# Set the thrust coefficient so that at thrust = 0.5 we balance
# the weight of the quad-rotor.
motors.thrust_coeff = mass * gravity * 2

#-------------------------------------------------------------
# Quad aero model setup
#-------------------------------------------------------------
aero.drag_coeff = drag_coeff

#-------------------------------------------------------------
# Dynamics model setup
#-------------------------------------------------------------
# Set the integrator 
quad_integrator.getIntegrator(trick.Runge_Kutta_4, 4)
# Set the gravitational coefficient
dynamics.grav_coeff = set_unit_val("m/s2", gravity)

#-------------------------------------------------------------
# Un-comment statements below in order to turn off a 
# particular sim object. This may be helpful in debugging.
#-------------------------------------------------------------
#trick.exec_set_sim_object_onoff("hc", 0)
#trick.exec_set_sim_object_onoff("motors", 0)
#trick.exec_set_sim_object_onoff("aero", 0)
#trick.exec_set_sim_object_onoff("dynamics", 0)

#-------------------------------------------------------------
# Set the variable server port to use. This must equal 32475
# in order to communicate with the Unreal Engine
#-------------------------------------------------------------
trick.var_server_set_port(32475)

#-------------------------------------------------------------
# Print events to terminal as they activate
#-------------------------------------------------------------
trick.set_event_info_msg_on()

#-------------------------------------------------------------
# END OF INPUT FILE
#-------------------------------------------------------------
