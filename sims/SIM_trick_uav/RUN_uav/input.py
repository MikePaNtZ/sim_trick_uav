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

#-------------------------------------------------------------
# Print events to terminal as they activate
#-------------------------------------------------------------
trick.set_event_info_msg_on()

#-------------------------------------------------------------
# END OF INPUT FILE
#-------------------------------------------------------------
