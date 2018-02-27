#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RobotARM_RTC.py
 @brief ModuleDescription
 @date $Date$


"""
from __future__ import division
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import os
_FILE_DIR=os.path.abspath(os.path.dirname(__file__))

import time
import sys
sys.path.append(_FILE_DIR+'/..')
from lib import ARM


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
robotarm_rtc_spec = ["implementation_id", "RobotARM_RTC",
		 "type_name",         "RobotARM_RTC",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "GClue",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class RobotARM_RTC
# @brief ModuleDescription
#
#
class RobotARM_RTC(OpenRTM_aist.DataFlowComponentBase):
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)


	def onInitialize(self):

		print("oninitialize values")
		self.HUMAN_INPUT = False
		self.AUTO = True
		self.arm_cls = ARM()
		self.arm=arm_cls.arm1

		return RTC.RTC_OK

	def move_servo(self, ANGLE = 90):
		try:
			while True:
				if self.HUMAN_INPUT:
					value = arm.get_angle()
					print(value)
					ANGLE = float(raw_input('Enter angle: '))
					ARM_ANGLE = ANGLE
					arm.set_angle(ARM_ANGLE)

					if self.AUTO:
						self.arm_cls.start("catch put empty")
						# while to stop moving
						while not self.arm_cls.checkCallback():
							time.sleep(1)

		except:
			import traceback
			traceback.print_exc()

		finally:
			#arm_cls.stop()
			#arm_cls.arm_empty()
			#arm_cls.wait()
			pass

def RobotARM_RTCInit(manager):
	print("RobotARM init")
	profile = OpenRTM_aist.Properties(defaults_str=robotarm_rtc_spec)
	manager.registerFactory(profile,
                            RobotARM_RTC,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
	print("Mymodule init")
	RobotARM_RTCInit(manager)

    # Create a component
	comp = manager.createComponent("RobotARM_RTC")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()
	ARM = RobotARM_RTC()
	ARM.onInitialize()
